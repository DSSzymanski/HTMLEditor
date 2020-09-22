import file_handler as fh
from os.path import exists
cdur = "C:\\Users\\Daniel\\Desktop\\programming\\work\\switchboard\\code_website"
ddur = "C:\\Users\\Daniel\\Desktop\\stuff"
ext = ".html"
if exists(cdur):
    fh.copy_to_new_dir(cdur, ddur)
    fh.DFS(ddur, ext)