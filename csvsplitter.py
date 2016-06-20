import sys,os
import py2 as csv
import converter,iohelper
from itertools import groupby

result = {}
header=[]
iohelper.dir_clean('splitted/')
with open('novels.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, encoding='utf-8')
    header=csvreader.next()
    for row in csvreader:
        if row[33] in result:
            result[row[33]].append(row)
            if(len(result[row[33]])>100000):
                print 'start---%s' % row[33]
                with open("splitted/%s.csv" % row[33], "ab") as output:
                    wr = csv.writer(output, encoding='utf-8')
                    if os.path.getsize("splitted/%s.csv" % row[33])==0:
                        wr.writerow(header)
                        converter.convert_to_utf8("splitted/%s.csv" % row[33])
                    for line in result[row[33]]:
                        wr.writerow(line)
                    print 'end---%s' %row[33]
                result[row[33]]=[]
        else:
            result[row[33]] = [row]
    for attr, value in result.iteritems():
        if attr!='-' and attr!='':
            print 'start---%s' %attr
            with open("splitted/%s.csv" %attr, "ab") as output:
                wr = csv.writer(output, quoting=csv.QUOTE_ALL)
                if os.path.getsize("splitted/%s.csv" % attr)==0:
                    wr.writerow(header)
                    converter.convert_to_utf8("splitted/%s.csv" % attr)
                for line in value:
                    wr.writerow(line)
                print 'end---%s' %attr
            value=[]