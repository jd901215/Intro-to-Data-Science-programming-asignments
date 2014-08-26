__author__ = 'juanda'

__author__ = 'juanda'

import MapReduce as MR
import sys
import json

mr = MR.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: Order_id
    # value: (String that identifies the table the record originates from. line_item, order, everything else)

    key = record[1]
    mr.emit_intermediate(key, [record[0].encode('ascii','replace'),record])

def reducer(key, list_of_values):
    # key: order_id
    # value: everything else
    base = []
    for element in list_of_values:

        if element[0]=='order':
            base = element[1]

        if element[0]=='line_item' and len(base)!=0:

            mr.emit( base + element[1])

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
