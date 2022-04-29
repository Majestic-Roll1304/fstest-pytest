import os
class regular():
    def create_file(self,file_name):
        return os.open(file_name,os.O_CREAT)

    def change_perm(self,file_name,mode):
        if os.chmod(file_name,mode) is None:
            return 0

    def file_stat(self,file_name):
        return (os.stat(file_name).st_mode & 0o777)

    def stat_ctime(self,file_name):
        return os.stat(file_name).ctime

    def make_symlink(self,file_name,link_name):
        if os.symlink(file_name,link_name) is None:
            return 0

    def link_stat(self,link_name):
        return (os.lstat(link_name).st_mode & 0o777)

    def remove(self,file_name):
        if os.unlink(file_name) is None:
            return 0

    def removelink(self,link_name):
        if os.unlink(link_name) is None:
            return 0


