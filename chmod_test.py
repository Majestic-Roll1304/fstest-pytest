import pytest
from regular import regular
from fifo import fifo
from directory import directory
from namegen import namegen
import os

os.umask(0)

common_args=("filetype,fname,lname",[[regular(),namegen(),namegen()],[fifo(),namegen(),namegen()],[directory(),namegen(),namegen()]])
@pytest.mark.parametrize(*common_args)
class Testchmod:

    def test_creat(self,filetype,fname,lname):
        assert filetype.create_file(fname) > 0

    def test_chmod_1(self,filetype,fname,lname):
        assert filetype.change_perm(fname,0o111) == 0

    def test_stat_1(self,filetype,fname,lname):
        assert filetype.file_stat(fname) == 0o111

    def test_symlink(self,filetype,fname,lname):
        assert filetype.make_symlink(fname,lname) == 0

    def test_chmod_2(self,filetype,fname,lname):
        assert filetype.change_perm(fname,0o222) == 0

    def test_stat_2(self,filetype,fname,lname):
        assert filetype.file_stat(fname) == 0o222

    def test_stat_3(self,filetype,fname,lname):
        assert filetype.file_stat(lname) == 0o222

    #writing stat of linkwithout changing its permissions checks if the file is created with given permission or not

    def test_lstat(self,filetype,fname,lname):
        assert filetype.link_stat(lname) == 0o777

    def test_rmlink(self,filetype,fname,lname):
        assert filetype.removelink(lname) == 0

    def test_rm(self,filetype,fname,lname):
        assert filetype.remove(fname) == 0