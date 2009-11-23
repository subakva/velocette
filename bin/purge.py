#!/usr/bin/env python

#   Copyright (c) 2003-2006 Open Source Applications Foundation
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


# from os import curdir, path, walk, unlink, removedirs
from os import path as os_path
from os import walk as os_walk
from os import unlink as os_unlink
from os import curdir as os_curdir
from os import removedirs as os_removedirs
import sys

def purgeDirs(path=os_curdir, verbose=True, dry_run=False):
    """Purge orphaned .pyc/.pyo files and remove emptied directories"""

    for dirname, dirs, files in os_walk(path, topdown=False):
        to_purge = [
            f for f in files
            if (f.endswith('.pyc') or f.endswith('.pyo'))
            and f[:-1] not in files     # don't purge if it has a .py
        ]
        for f in to_purge:
            filename = os_path.join(dirname, f)
            if verbose:
                print "deleting", filename
            if not dry_run:
                os_unlink(filename)

        if to_purge and files==to_purge:
            for d in dirs:
                # Do any of the subdirectories still exist?
                if os_path.exists(os_path.join(dirname, d)):
                    # If so, we've done all we can
                    break
            else:
                # Go ahread and remove the current directory
                if verbose:
                    print "removing ", dirname
                if not dry_run:
                    os_removedirs(dirname)

if __name__ == '__main__':
    from optparse import OptionParser

    parser = OptionParser(usage="usage: %prog [options] directory")
    parser.add_option(
        "-n", "--dry-run", dest="dry_run", action="store_true", default=False, 
        help="don't actually delete anything"
    )
    parser.add_option("-q", "--quiet", 
        action="store_false", dest="verbose", default=True, 
        help="don't display the files/dirs being removed"
    )

    (options, args) = parser.parse_args()

    if options.dry_run and not options.verbose:
        print "Using both -n and -q makes no sense.  Use --help for options."
        sys.exit(2)

    if not args:
        print "No directories specified.  Use --help for options."
        sys.exit(2)

    for path in args:
        purgeDirs(path, options.verbose, options.dry_run)

