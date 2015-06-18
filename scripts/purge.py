#!/usr/bin/python
# removes any files in <targetdir> older than <purgeperiod> days

import os, sys, time, getopt

def get_filepaths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths

def usage():
    print 'purgebackup.py -d -p <purgeperiod> -t <targetdir>'
    print ''
    print '  -d, --dryrun         do not purge anything'
    print '  -p, --purgeperiod    purge files older than this period (of days)'
    print '  -t, --targetdir      directory under which files are purged'

def main(argv):
    targetdir = ''
    purgeperiod = ''
    dryrun = False

    try:
        opts, args = getopt.getopt(argv,"hdp:t:",["purgeperiod=","targetdir="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            usage()            
            sys.exit()
        elif opt in ("-t", "--targetdir"):
            targetdir = arg
        elif opt in ("-p", "--purgeperiod"):
            purgeperiod = int(arg)
        elif opt in ("-d", "--dryrun"):
            dryrun = True

    now = time.time()
    cutoff = now - (purgeperiod * 86400)
    file_paths = get_filepaths(targetdir)

    for targetfile in file_paths:
        if os.path.isfile(targetfile):
            t = os.stat(targetfile)
            c = t.st_mtime
            if c < cutoff:
                if dryrun:
	            print "File would be purged: " + targetfile
                else:
                    os.remove(targetfile)
                    print "Removed: " + targetfile


if __name__ == "__main__":
    main(sys.argv[1:])
