from pythontasks.utils.entrez_efetch import fetch_transcript_record
from pythontasks.modules.transcribe_dna import transcribe_dna_to_mrna
from pythontasks.modules.translate_dna import translate_dna_to_AAseq
from pythontasks.modules.reverse_complement import reverse_complement_dna
from pythontasks.modules.GC_content import calculate_gc_content
from pythontasks.modules.nucleotide_count import nucleotide_count
from pythontasks.modules.chunk_dna import chunk_dna
from pythontasks.modules.genbank_chunk_dna import genbank_chunk_dna
from pythontasks.modules.framed_translation import six_frame_translation


class Transcript:
    """
    A class to represent a transcript record fetched from GenBank via the Entrez EFetch API.
    On initialisation, this class:
    - Validates and passes a RefSeq transcript accesstion to the 'fetch_transcript_record()' function.
    - 'fetch_transcript_record()' uses Entrez Efetch to download the treanscripts GenBank record, then parses the XML into a Python dictionary.
    - This transcript class then extracts key biological fields from the dictionary.
    - Provides utility methods to analyse and format sequences.
    """
    
    def __init__(self, accession_id: str):
        """
        Initialise the Transcript object with a RefSeq accession ID.
        """
        record = fetch_transcript_record(accession_id) # Verifies the accession ID is valid, sends request to NCBI Entrez EFetch, parses the XML result into a python dict.

        # Extract high level information from the record
        self.transcript_id = record.get("GBSeq_accession-version") # Unique RefSeq accession number with version
        self.definition = record.get("GBSeq_definition") # Descriptive text for the transcript
        self.dna_sequence = (record.get("GBSeq_sequence") or "").upper() # Raw DNA sequence in uppercase for consistency
        self.rna_sequence = transcribe_dna_to_mrna(self.dna_sequence) or "" # mRNA conversion from my module (transcribe_dna)
    
        # Prepare placeholders for additional metadata. These will be populated by parsing the GenBank feature table
        self.gene_symbol = None
        self.hgnc_id = None
        self.protein_id = None
        self.protein_sequence = None

        # Parse the feature table to extract gene symbol, HGNC ID, protein ID, and protein sequence
        feature_table = record.get("GBSeq_feature-table", {}).get("GBFeature", [])

        # If there is only one feature, the API may return it as a single dict, not a list. This ensures it is parsed as a list to loop over
        if not isinstance(feature_table, list):
            feature_table = [feature_table]
        
        # For each feature (like "gene" or "CDS"), we extract the type of feature and a list of qualifiers (smal key-value pairs)
        for feature in feature_table:
            feature_type = feature.get("GBFeature_key")
            qualifiers = feature.get("GBFeature_quals", {}).get("GBQualifier", [])

            # This again ensures that, if only a single qualifier is present in a feature, it is returned as a list, not a single dict
            if not isinstance(qualifiers, list):
                qualifiers = [qualifiers]

            # Extracts the gene name and associated symbol (e.g. Gene: PTEN)
            if feature_type == "gene":
                for qual in qualifiers:
                    if qual.get("GBQualifier_name") == "gene":
                        self.gene_symbol = qual.get("GBQualifier_value")

                    # Gets the HGNC ID (e.g. HGNC: HGNC:9588 )
                    if qual.get("GBQualifier_name") == "db_xref":
                        val = qual.get("GBQualifier_value")
                        if "HGNC" in val:
                            self.hgnc_id = val.replace("HGNC:HGNC:", "HGNC:")

            # Extracts CDS data (protein ID and amino acid sequence)
            elif feature_type == "CDS":
                for qual in qualifiers:
                    if qual.get("GBQualifier_name") == "protein_id":
                        self.protein_id = qual.get("GBQualifier_value")
                    if qual.get("GBQualifier_name") == "translation":
                        self.protein_sequence = qual.get("GBQualifier_value")

    

    # Utility methods for sequence manipulation using functions in my 'modules'
    # Returned as strings where necessary as results will currently only be printed to the terminal
    def reverse_complement(self) -> str:
        return reverse_complement_dna(self.dna_sequence)

    def gc_content(self) -> str:
        return calculate_gc_content(self.dna_sequence)

    def nucleotide_counts(self):
        return nucleotide_count(self.dna_sequence)

    def six_frame_translation_report(self) -> str:
        return six_frame_translation(self.dna_sequence)


    # Further formatting using functions in my 'modules'

    def to_fasta(self, sequence_type: str = "dna") -> str:
        """
        Return a FASTA-formatted string using 'chunk_dna()'
        """

        # If user wants DNA FASTA
        if sequence_type == "dna": 
            sequence = self.dna_sequence # Retrieve the DNA sequence stored in the object
            header = self.transcript_id # Use transcript ID as FASTA header

        # If user wants RNA FASTA
        elif sequence_type == "rna":
            sequence = self.rna_sequence # Retrieve the already transcribed RNA sequence
            header = f"{self.transcript_id}_RNA" # Append "_RNA" to distinguish it in the header

        # If user wants protein FASTA
        elif sequence_type == "protein":
            sequence = self.protein_sequence # Retrieves the amino acid sequence
            header = self.protein_id or f"{self.transcript_id or 'UNKNOWN'}_PROT" # Use the protein ID, if available. If not, fallback to transcript ID and "_prot"

        # For amino acid sequences, format by wrapping lines at 60 characters
        if sequence_type == "protein":
            lines = [sequence[i:i+60] for i in range(0, len(sequence), 60)]
            body = "\n".join(lines)

        # For DNA/RNA sequences, format using 'chunk_dna()' and wrap 6 chunks per line
        else:
            blocks = chunk_dna(sequence, block_size=10).split()
            lines = []
            for i in range(0, len(blocks), 6):
                lines.append("".join(blocks[i:i+6]))
            body = "\n".join(lines)
        return f">{header}\n{body}" # join all lines together with line breaks


    def to_genbank_format(self, sequence_type: str = "dna") -> str:
        """
        Returns a GenBank-style formatted string, including:
           - LOCUS line (transcript ID, length, molecule type)
           - DEFINITION line (gene description)
           - ORIGIN block (formatted sequence)
        """
        
        # Case 1: DNA sequence
        if sequence_type == "dna":
            sequence = self.dna_sequence # Retrieve the DNA sequence stored in the object
            molecule = "DNA" # Label the molecule type as DNA
            locus = self.transcript_id # Use transcript ID as locus name
            origin_block = genbank_chunk_dna(sequence, block_size=10, blocks_per_row=6) # Utilise the genbank_chunk_dna function to format the DNA sequence

        # Case 2: RNA sequence
        elif sequence_type == "rna":
            sequence = self.rna_sequence # Retrieve the already transcribed RNA sequence
            molecule = "RNA" # Label the molecule type as RNA
            locus = self.transcript_id # Use transcript ID as locus name
            origin_block = genbank_chunk_dna(sequence, block_size=10, blocks_per_row=6) # Utilise the genbank_chunk_dna function to format the RNA sequence

        # Case 3: Protein sequence. This only uses genbank-style annotations for the header, not the sequence formatting
        elif sequence_type == "protein":
            sequence = self.protein_sequence # Retrieves the amino acid sequence
            molecule = "AA" # Label the molecule type as Amino Acid
            locus = self.protein_id # Use the protein ID as locus name
            lines = [sequence[i:i+60] for i in range(0, len(sequence), 60)] # Wrap lines at 60 characters
            origin_block = "\n".join(lines)

        # Construct and return the final GenBank-style formatted string
        return (
            f"LOCUS {locus} {len(sequence)} bp {molecule}\n"
            f"DEFINITION {self.definition or ''}\n"
            f"ORIGIN\n{origin_block}\n//"
        )