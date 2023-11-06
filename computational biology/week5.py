# ---------------------------------------------------------------------------#
# ---------------------------------------------------------------------------#
# ----------------------- BIOPYTHON PAIRWISE ALIGN --------------------------#
# ---------------------------------------------------------------------------#
# ---------------------------------------------------------------------------#

from Bio import Align, pairwise2
from Bio.Seq import Seq
from Bio.pairwise2 import format_alignment

# FROM BIOPYTHON DOCUMENTATION
def pairwise_aligner():
    aligner = Align.PairwiseAligner()
    alignments = aligner.align("GAACT", "GAT")
    alignment = alignments[0]
    print(alignment)

# IN CLASS DEMONSTRATION
def pairwise():
    seq1 = Seq("AGCGGTTT")
    seq2 = Seq("ACGT")

    print("--- LOCAL --- ")
    for a in pairwise2.align.localxx(seq1, seq2):
        print(format_alignment(*a))

    print("--- GLOBAL ---")
    for a in pairwise2. align.globalxx(seq1, seq2):
        print(format_alignment(*a))

# ---------------------------------------------------------------------------#
# ---------------------------------------------------------------------------#
# ------------------------------- PYMSAVIZ MSA ------------------------------#
# ---------------------------------------------------------------------------#
# ---------------------------------------------------------------------------#

from pymsaviz import MsaViz, get_msa_testdata

msa_file = get_msa_testdata("HIGD2A.fa")
mv = MsaViz(msa_file, wrap_length=70, show_count=True)
mv.savefig("example1.png")

mv = MsaViz(msa_file, color_scheme="Taylor", wrap_length=80, show_grid=True, show_consensus=True)
mv.savefig("example2.png")