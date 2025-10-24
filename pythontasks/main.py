from pythontasks.utils.gb_transcript import Transcript # Import the transcript class which handles fetching and processing of transctipt records
from pythontasks.modules.chunk_dna import chunk_dna # Used again to format DNA reverse complement into FASTA style

# Menu displayed to the user for interactive choices
MENU = """
Choose an option:
 1) Summary
 2) Raw attributes
 3) DNA FASTA
 4) RNA FASTA
 5) Protein FASTA
 6) DNA (GenBank-style)
 7) RNA (GenBank-style)
 8) Protein (GenBank-style)
 9) Six-frame translation
10) DNA reverse complement (FASTA)
11) DNA GC%
12) DNA nucleotide counts
13) Change transcript
 0) Quit
> """

def ask_transcript() -> Transcript:
    """
    Prompt the user to enter a transctipt accession ID
    Keeps asking until a valid transcript object is created
    """
    while True:
        acc = input("Enter RefSeq transcript (e.g., NM_000546.6): ").strip()
        try:
            return Transcript(acc) # Attempt to fetch and initialise a transcript object
        except Exception as e: # Catch any errors raised during Transcript creation (e.g., invalid format, network failure, XML parsing issues, etc.)
            print(f"Error: {e}\nTry another accession.\n")

# For otion 1
def show_summary(t: Transcript):
    print("\n--- Summary ---")
    print("ID:", t.transcript_id)
    print("Gene:", t.gene_symbol)
    print("HGNC:", t.hgnc_id)
    print("Protein ID:", t.protein_id)

# For option 2
def show_attrs(t: Transcript):
    print("\n--- Attributes ---")
    print("definition:", t.definition)
    print("dna_len   :", len(t.dna_sequence))
    print("rna_len   :", len(t.rna_sequence))
    print("protein_id:", t.protein_sequence)
    print("protein_len:", 0 if not t.protein_sequence else len(t.protein_sequence))

# Main execution loop
def run():
    t = ask_transcript() # Load initial transctipt ID from user input
    while True:
        c = input(MENU).strip() # Prompt user for a menu selection
        if   c == "1": show_summary(t)
        elif c == "2": show_attrs(t)
        elif c == "3": print("\n" + t.to_fasta("dna"))
        elif c == "4": print("\n" + t.to_fasta("rna"))
        elif c == "5": print("\n" + t.to_fasta("protein"))
        elif c == "6": print("\n" + t.to_genbank_format("dna"))
        elif c == "7": print("\n" + t.to_genbank_format("rna"))
        elif c == "8": print("\n" + t.to_genbank_format("protein")) 
        elif c == "9": print("\n" + t.six_frame_translation_report())
        elif c == "10":
            rc = t.reverse_complement()
            body = "\n".join("".join(chunk_dna(rc, 10).split())[i:i+60] for i in range(0, len(rc), 60))
            print("\n>RC_" + (t.transcript_id) + "\n" + body)
        elif c == "11":
            print("\nGC%:", t.gc_content())
        elif c == "12":
            mono, di, tri = t.nucleotide_counts()
            print("\nCounts:\n mono:", mono, "\n di  :", di, "\n tri :", tri)
        elif c == "13": t = ask_transcript()
        elif c == "0": break
        else: print("Invalid choice.\n")

if __name__ == "__main__":
    run()