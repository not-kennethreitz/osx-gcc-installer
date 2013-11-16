#! /usr/bin/env python
import optparse
import subprocess
import sys
import tempfile

import os.path as op

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    usage = "usage: %prog [options] packages_path packages_list.txt"

    parser = optparse.OptionParser(usage)
    parser.add_option("-o", dest="output_file",
                      help="Output package name (default: %(default)s",
                      default="build_essentials.pkg")
    parser.add_option("--packages-list", dest="packages_list",
                      help="File containing the list of packages to include (default %(default)s)",
                      default="packages_list.txt")
    parser.add_option("--packages-path", dest="packages_path",
                      help="Directory which contains the packages (default %(default)s)",
                      default="Install Xcode.app/Contents/Resources/Packages")

    (options, args) = parser.parse_args()
    if len(args) != 0:
        parser.print_help()
        sys.exit(0)
    
    packages_path = options.packages_path
    packages_list = options.packages_list

    with tempfile.NamedTemporaryFile(suffix=".xml") as fp:
        dist_file = fp.name
        cmd = ["productbuild", "--synthesize"]
        with open(packages_list, "rt") as fp:
            for entry in fp:
                cmd.extend(["--package", op.join(packages_path, entry.rstrip())])
            cmd += [dist_file]
        subprocess.check_call(cmd)

        cmd = ["productbuild", "--distribution", dist_file,
               "--package-path", packages_path, options.output_file]
        subprocess.check_call(cmd)
 
if __name__ == "__main__":
    main()
