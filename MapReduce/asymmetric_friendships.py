__author__ = 'juanda'
import MapReduce
import sys



mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    mr.emit_intermediate((record[0],record[1]), 1)
    mr.emit_intermediate((record[1],record[0]), -1)


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #mr.emit((key, total))
    list_asimetrical = []
    if sum(list_of_values) == 1:
        if key not in list_asimetrical:
            list_asimetrical.append(key)
        if (key[1],key[0]) not in list_asimetrical:
            list_asimetrical.append((key[1],key[0]))

    for element in list_asimetrical:
        mr.emit(element)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
