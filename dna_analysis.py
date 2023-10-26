# Project 1: DNA analysis

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq
# 
# This program is based on Michael Ernt's assignment on DNA Analysis 

###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print ("You must supply a file name as an argument when running this program.")
    sys.exit(2)


# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0

# Problem 2b
# Number of G nucleotides seen so far.
g_count = 0
# Number of C neucleotides seen so far.
c_count = 0
# Number of A nucleotides seen so far.
a_count = 0
# Number of T nucleotides seen so far.
t_count = 0

# Number of G and C nucleotides seen so far.
gc_count = 0

# Problem 2a
# Number of A and T nucleotides seen so far.
at_count = 0

# for each base pair in the string,
for bp in seq:

    total_count = total_count + 1
    
    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1

    # Problem 2a
    # if the np is an A or a T, 
    if bp == 'A' or bp == 'T': 
        # increment the count of AT
        at_count = at_count + 1

    # Problem 2b
    # next, if the nucleotide is a G, C, A, or T
    if bp == 'G':
        g_count = g_count + 1
    
    if bp == 'C':
        c_count = c_count + 1
       
    if bp == 'A':
        a_count = a_count + 1

    if bp == 'T':
        t_count = t_count + 1

# divide the gc_count by the total_count
gc_content = float(gc_count / (g_count + c_count + a_count + t_count))

#Problem 2a
# divide the at_count by the total_count
at_content = float(at_count / (g_count + c_count + a_count + t_count))

# Problem 2d
# Compute the AT/GC ratio
atgc_ratio = (at_count) / (gc_count)

# Print the problem number, such as 2a
print("Problem Number: 2e")

# Print the answer
print ("GC-content:", gc_content)

# Problem 2a
# Print AT content
print ("AT-content:", at_content)

# Problem 2b
# Print nucleotide count
print ("G-count:", g_count)
print ("C-count:", c_count)
print ("A-count:", a_count)
print ("T-count:", t_count)

# Problem 2c
# Compare metrics
print('Sum count: ', (g_count + c_count + a_count + t_count))
print('Total count: ', total_count)
print('Seq length: ', len(seq))

# Problem 2d
# Print AT/GC ratio
print('AT/GC ratio: ', atgc_ratio)

# Problem 2e
# Print out a classification of the organism
if gc_content > 0.60:
    print('GC Classification: high GC content ')
elif gc_content < 0.40:
    print('GC Classification: low GC content ')
else:
    print('GC Classification: moderate GC content ')



