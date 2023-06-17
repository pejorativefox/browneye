import subprocess
import os
from urllib.parse import urlparse
from process import run_process

def get_md5(filename):
    """Get an md5 for a file on the filesystem by running the md5sum tool.

    Args:
        param1 (str) filename: the full path of the file

    Returns:
        str: the md5sum of the specified file.

    """
    md5 = subprocess.check_output(["md5sum", filename]).rstrip().decode('ascii').split(" ")[0]
    return md5


def parse_sources(sources_filename):
    """Parse a 'sources' file to get a list of files that need to be downloaded
    for a package.

    Args:
        param1 (str) sources_filename: the full path to a valid sources file

    Returns:
        list of (str:md5sum, str:url, str:override_filename) 
                or 
                (str:md5sum, str:url, bool:has_override)
    
    """
    fbuff = ""
    with open(sources_filename, "r") as fd:
        fbuff = fd.readlines()
    sources = []
    for line in fbuff:
        split_line = line.rstrip().split(" ")
        line_length = len(split_line)
        if line_length == 2 or line_length == 3:
            pass
        else:
            print("{} appears to have a mangled line...".format(sources_filename))
            exit()
        md5 = split_line[0]
        url = split_line[1]
        if len(split_line) == 3:
            filename = split_line[2]
        else:
            filename = None
        sources.append([md5, url, filename])
    return sources


BASE_PATH = os.path.expanduser('~') # TODO: maybe not best location

def fetch_sources(sources, override_filename=None):
    return_code = True
    for source in sources:
        md5, url, override_filename = source
        filename = ""
        if override_filename:
            filename = override_filename
        else:
            filename = os.path.basename(urlparse(url).path)
        out_file = BASE_PATH + "/rpmbuild/SOURCES/{}".format(filename)
        if os.path.isfile(out_file):
            print("  + Already present (cached)")
        else:
            print("Downloading {} to {}".format(url, BASE_PATH + "/rpmbuild/SOURCES/{}".format(filename)))
            cmd = ["curl", "-fL", "-o", out_file, url]
            #cmd = ["wget", "-N", "-c", "-O", out_file, url]
            if os.getenv("USE_PROXYCHAINS"):
                cmd = ["proxychains4"] + cmd
            # use runprocess and check return code
            return_code = run_process(cmd)
            #subprocess.call(cmd)

        target_md5 = get_md5(BASE_PATH + "/rpmbuild/SOURCES/{}".format(filename))
        if md5 == target_md5:
            print("  + md5 good")
        else:
            print("Bad md5: {}".format(target_md5))
            # return false here as issues with md5
            return False