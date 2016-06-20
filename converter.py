#!/usr/bin/env python
 
import chardet,codecs,os,sys,shutil
 
def convert_to_utf8(filename):
    # gather the encodings you think that the file may be
    # encoded inside a tuple
    encodings = ( 'utf-8', 'utf-8-sig', 'windows-1253', 'iso-8859-7', 'macgreek')
 
    # try to open the file and exit if some IOError occurs
    try:
        f = open(filename, 'r').read()
    except Exception:
        sys.exit(1)
 
    # now start iterating in our encodings tuple and try to
    # decode the file
    for enc in encodings:
        try:
            # try to decode the file with the first encoding
            # from the tuple.
            # if it succeeds then it will reach break, so we
            # will be out of the loop (something we want on
            # success).
            # the data variable will hold our decoded text
            data = f.decode(enc)
            break
        except Exception:
            # if the first encoding fail, then with the continue
            # keyword will start again with the second encoding
            # from the tuple an so on.... until it succeeds.
            # if for some reason it reaches the last encoding of
            # our tuple without success, then exit the program.
            print enc
            if enc == encodings[-1]:
                sys.exit(1)
            continue
 
    # now get the absolute path of our filename and append .bak
    # to the end of it (for our backup file)
    #fpath = os.path.abspath(filename)
    #newfilename = fpath + '.bak'
    # and make our backup file with shutil
    #shutil.copy(filename, newfilename)
 
    # and at last convert it to utf-8
    f = open(filename, 'w')
    try:
        f.write(data.encode('utf-8-sig'))
    except Exception, e:
        print e
    finally:
        f.close()

def utf8_converter(file_path, universal_endline=True):
    '''
    Convert any type of file to UTF-8 without BOM
    and using universal endline by default.

    Parameters
    ----------
    file_path : string, file path.
    universal_endline : boolean (True),
                        by default convert endlines to universal format.
    '''

    # Fix file path
    file_path = os.path.realpath(os.path.expanduser(file_path))

    # Read from file
    file_open = open(file_path)
    raw = file_open.read()
    file_open.close()

    # Decode
    raw = raw.decode(chardet.detect(raw)['encoding'])
    # Remove windows end line
    if universal_endline:
        raw = raw.replace('\r\n', '\n')
    # Encode to UTF-8
    raw = raw.encode('utf8')
    # Remove BOM
    if raw.startswith(codecs.BOM_UTF8):
        raw = raw.replace(codecs.BOM_UTF8, '', 1)

    # Write to file
    file_open = open(file_path, 'w')
    file_open.write(raw)
    file_open.close()
    return 0