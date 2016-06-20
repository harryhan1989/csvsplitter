import sys,os
import py2 as csv
import converter,iohelper
from itertools import groupby

def do_split(csvfilepath,colidx):
    result = {}
    header=[]
    iohelper.delete_file_folder('splitted/')
    iohelper.dir_create('splitted/')
    with open(csvfilepath, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, encoding='utf-8')
        header=csvreader.next()
        for row in csvreader:
            if row[colidx] in result:
                result[row[colidx]].append(row)
                if(len(result[row[colidx]])>100000):
                    print 'start---%s' % row[colidx]
                    with open("splitted/%s.csv" % row[colidx], "ab") as output:
                        wr = csv.writer(output, encoding='utf-8')
                        if os.path.getsize("splitted/%s.csv" % row[colidx])==0:
                            wr.writerow(header)
                            converter.convert_to_utf8("splitted/%s.csv" % row[colidx])
                        for line in result[row[colidx]]:
                            wr.writerow(line)
                        print 'end---%s' %row[colidx]
                    result[row[colidx]]=[]
            else:
                result[row[colidx]] = [row]
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