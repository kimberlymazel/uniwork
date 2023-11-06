# ---------------------------------------------------------------------------#
# ---------------------------------------------------------------------------#
# ----------------------- FIND PATTERN IN SEQUENCE --------------------------#
# ---------------------------------------------------------------------------#
# ---------------------------------------------------------------------------#

def find_pattern(pattern, seq):
    pat_len = len(pattern)
    n = len(seq)
    pat_result = []

    for i in range(n-pat_len + 1):
        j = 0

        while(j < pat_len):
            if(seq[i+j] != pattern[j]):
                break
            j += 1

        if(j == pat_len):
            pat_result.append(i)

    print("Pattern found at index = ", pat_result)

dna = "ATGAACACGAATAAGAA"
pattern = "GAA"

# find_pattern(pattern, dna)

# ---------------------------------------------------------------------------#
# ---------------------------------------------------------------------------#
# ----------------------- MATCH STRING USING REGEX --------------------------#
# ---------------------------------------------------------------------------#
# ---------------------------------------------------------------------------#

import re 

def regex_match(): 
    str = "TGAAGTATGAGA"
    print(str)

    mo = re.search("TAT", str)
    print("Group = ", mo.group())
    print("Span = ", mo.span())

    mo2 = re.search("TG.", str)
    print("Group = ", mo2.group())
    print("Span = ", mo2.span())

    print("Find TA = ", re.findall("TA", str))
    print("Find TG = ", re.findall("TG", str))

    mos = re.finditer("TG.", str)

    for x in mos:
        print(x.group())
        print(x.span())

# regex_match()

# ---------------------------------------------------------------------------#
# ---------------------------------------------------------------------------#
# ------------------------ CURRENT AND PEAK MEMORY --------------------------#
# ---------------------------------------------------------------------------#
# ---------------------------------------------------------------------------#

import tracemalloc

def memory():
    dna = "actggacta"

    tracemalloc.start()
    result = re.search("^[CAGTcagt]+$", dna)
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()

# memory()

# ---------------------------------------------------------------------------#
# ---------------------------------------------------------------------------#
# ---------------------- ENHANCED LOWER MEMORY USAGE ------------------------#
# ---------------------------------------------------------------------------#
# ---------------------------------------------------------------------------#

def lower_memory():
    dna = "actggacta"

    tracemalloc.start()
    better = re.search("[^CAGTcagt]+$", dna)
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()

    print(better)

    if better == None:
        print("negated - match")
    else:
        print("negated - not match")

lower_memory()