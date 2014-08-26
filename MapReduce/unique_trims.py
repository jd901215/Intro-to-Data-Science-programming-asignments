__author__ = 'juanda'
import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    dna = record[1][:-10]
    scores_dict = {'A':1,'C':2,'G':3,'N':4,'T':5}
    score = 0
    for letter in dna:
        score += scores_dict[str(letter.decode('ascii','ignore'))]

    mr.emit_intermediate(score, dna)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    mr.emit(list_of_values[0])

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
