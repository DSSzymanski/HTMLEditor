import file_handler as fh
from os.path import exists
from shutil import make_archive
cdur = "C:\\Users\\Daniel\\Desktop\\programming\\work\\switchboard\\code_website"
ddur = "C:\\Users\\Daniel\\Desktop\\code_website"
template = "C:\\Users\\Daniel\\Desktop\\programming\\work\\switchboard\\code_website\\template.txt"
ext = ".html"

if exists(cdur):
    fh.copy_to_new_dir(cdur, ddur)
    #TODO: remove once template is fixed.
    fh.DFS(ddur + "\\codes_html", ext, template)
    make_archive("C:\\Users\\Daniel\\Desktop\\code_website", 'zip', "C:\\Users\\Daniel\\Desktop\\code_website")
    fh.delete_new_dir(ddur)