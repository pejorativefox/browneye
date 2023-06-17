
import glob

class Package(object):
    def __init__(self, name, path, spec_file):
        self.name = name
        self.path = path
        self.spec_file = spec_file
        self.has_sources = True
        self.needs_root = False

    def get_full_spec_path(self):
        return self.path + "/" + self.spec_file
    
    def get_full_sources_path(self):
        return self.path + "/sources"
    
    def get_files_path(self):
        return self.path + "/files"

def check_has_sources(path):
    return True

def check_needs_root(path):
    return False

def discover_packages(path="package_specs/"):
    packages = []
    package_glob = glob.glob(path + "*")
    for package_path in package_glob:
        print("- Found Package Path: ", package_path)
        for spec in glob.glob("{}/*.spec".format(package_path)): # TODO: check multiple and warn
            print("    Found spec: ", spec)
            spec_file = spec.split("/")[-1]
            package_name = spec.split(".")[0].split("/")[-1]
            # TODO: check needs root and has sources
            packages.append(Package(package_name, package_path, spec_file))
    return packages

 
if __name__ == "__main__":
    for p in discover_packages():
        print(p.get_full_spec_path())