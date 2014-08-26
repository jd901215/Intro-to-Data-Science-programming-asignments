__author__ = 'juanda'

import MapReduce as MR
import sys

mr = MR.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: text of the document

    key = record[0]
    value = record[1]
    words = value.split()

    for w in words:
      mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of document identifiers

    total = []
    for v in list_of_values:
      if v not in total:
        total.append(v)
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
