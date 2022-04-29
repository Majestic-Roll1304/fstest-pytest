import os
from regular import regular

class fifo(regular):
    def create_file(self,file_name):
        if os.mkfifo(file_name) is None:
            return 1

