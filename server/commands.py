import json
import os
import platform
import re

class Commands:

    # def list_devices(self):
    #     devices = {}
    #     devices["drive1"] = "C"
    #     devices["drive2"] = "D"
    #     return json.dumps(devices)

    def get_environment(self):
        environment = {}
        environment['sysinfo'] = {}
        environment['sysinfo']['platform'] = platform.platform()
        environment['sysinfo']['node'] = platform.node()
        environment['sysinfo']['processor'] = platform.processor()
        environment['sysinfo']['python_compiler'] = platform.python_compiler()
        environment['sysinfo']['python_version'] = platform.python_version()
        return json.dumps(environment)

    def scan_dir(self, dir, search_term):
        listing = {}
        listing['files'] = {}

        for direntry in os.scandir(path=dir):

            result = re.match(search_term+'+', direntry.name)
            if result or search_term == "ALL":
                listing['files'][direntry.name] = {}
                listing['files'][direntry.name]['name'] = direntry.name
                listing['files'][direntry.name]['path'] = direntry.path
                listing['files'][direntry.name]['is_dir'] = direntry.is_dir()
        return json.dumps(listing)

    def download_file(self, filename):
        with open(filename, mode='rb') as f:
            file_content = f.read()
            self.server.send(file_content)
        f.close()
        print("Done sending {}".format(filename))
        return file_content


