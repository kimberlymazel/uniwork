# ---------------------------------------------------------------------------#
# ---------------------------------------------------------------------------#
# ------------------------ CHECK IF DNA IS VALID ----------------------------#
# ---------------------------------------------------------------------------#
# ---------------------------------------------------------------------------#

def validate_dna(dna_seq):
    seqm = dna_seq.upper()
    valid = seqm.count("A") + seqm.count("T") + seqm.count("G") + seqm.count("C")

    if valid == len(seqm):
        # print("Valid")
        return True
    else:
        # print("Invalid")
        return False

# validate_dna("atagagaatctcg") # Valid
# validate_dna("ATAGAXTAGAT") # Invalid

# ---------------------------------------------------------------------------#
# ---------------------------------------------------------------------------#
# ----------------------- CHECK FREQUENCY OF DNA ----------------------------#
# ---------------------------------------------------------------------------#
# ---------------------------------------------------------------------------#

def frequency(seq):
    dic = {}

    for s in seq.upper():
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
    
    # print(dic)
    return dic

# frequency("atagataactcgcatag")

# ---------------------------------------------------------------------------#
# ---------------------------------------------------------------------------#
# --------------------- PERCENTAGE OF NUCLEOTIDES ---------------------------#
# ---------------------------------------------------------------------------#
# ---------------------------------------------------------------------------#

def percentage(dna):
    if validate_dna(dna) == True:
        dna_dic = frequency(dna)
        
        string_length = len(dna)
        
        # CALCULATE PERCENTAGE
        a_perc = (dna_dic["A"]/string_length)*100
        t_perc = (dna_dic["T"]/string_length)*100
        g_perc = (dna_dic["G"]/string_length)*100
        c_perc = (dna_dic["C"]/string_length)*100

        # PRINTING STATEMENTS
        print("DNA = " + dna)
        print("DNA Length = " + str(string_length))
        print("A = " + str(a_perc) + "%")
        print("T = " + str(t_perc) + "%")
        print("G = " + str(g_perc) + "%")
        print("C = " + str(c_perc) + "%")

# percentage("ataccgatta")

# ---------------------------------------------------------------------------#
# ---------------------------------------------------------------------------#
# ------------------------- REVERSE COMPLEMENT  -----------------------------#
# ---------------------------------------------------------------------------#
# ---------------------------------------------------------------------------#

def reverse_complement(dna):
    assert validate_dna(dna), "Invalid"
    rev = ""

    for c in dna.upper():
        if c == "A":
            rev += "U" # For RNA
            # rev += "T" # For complement

        elif c == "T":
            rev += "A"

        elif c == "G":
            rev += "C"

        elif c == "C":
            rev += "G"
    
    print(rev)
    return rev

reverse_complement("ataccgatta")

# ---------------------------------------------------------------------------#
# ---------------------------------------------------------------------------#
# --------------------------- TRANSLATE CODON -------------------------------#
# ---------------------------------------------------------------------------#
# ---------------------------------------------------------------------------#

def translate_codon(cod):
    tc = {
        "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
        "TGT":"C", "TGC":"C",
        "GAT":"D", "GAC":"D",
        "GAA":"E", "GAG":"E",
        "TTT":"F", "TTC":"F",
        "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G",
        "CAT":"H", "CAC":"H",
        "ATA":"I", "ATT":"I", "ATC":"I",
        "AAA":"K", "AAG":"K",
        "TTA":"L", "TTG":"L", "CIT":"L", "CTA":"L", "CTG":"L",
        "ATG":"M", 
        "AAT":"N", "AAC":"N",
        "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
        "CAA":"Q", "CAG":"Q",
        "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R","AGG":"R",
        "TCT":"S", "TCC":"S",  "TCA":"S", "TCG":"S", "AGT":"S", "AGC":"S",
        "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
        "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
        "TGG":"W",
        "TAT":"Y", "TAC":"Y",
        "TAA":"_", "TAG":"_", "TGA":"_"
    }

    if cod in tc:
        return tc[cod]
    else:
        return None