from regular import regular
import os

class directory(regular):
    def create_file(self,file_name):
        if os.mkdir(file_name) is None:
            return 1
    def remove(self,file_name):
        if os.rmdir(file_name) is None:
            return 0
