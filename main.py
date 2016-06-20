import sys,csvsplitter

def main(argv):
    #print argv[0]
    #print argv[1]
    csvsplitter.do_split(argv[0],int(argv[1]))

if __name__ == "__main__":
    main(sys.argv[1:])