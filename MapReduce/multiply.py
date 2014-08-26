__author__ = 'juanda'
import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
A = 5
B = 5
def mapper(record):
    # key: document identifier
    # value: document contents
    if str(record[0].decode('ascii','ignore'))=='a':
        for idx in range(0,5):
            mr.emit_intermediate((record[1],idx),(record[2],record[3]))

    if str(record[0].decode('ascii','ignore'))=='b':
        for idx in range(0,5):
            mr.emit_intermediate((idx,record[2]),(record[1],record[3]))

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    d = {}
    for element in list_of_values:
        if element[0] not in d:
            d[element[0]]=[1,element[1]]
        else:
            d[element[0]][0]+=1
            d[element[0]].append(element[1])
    result = 0

    for k,v in d.iteritems():

        if v[0]==2:
            result += v[1]*v[2]
    mr.emit((key[0],key[1],result))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
