from commandlib import python_bin, Command, CommandError
from hitchrun import DIR, expected
import patoolib
import shutil


hugo_cmd = Command(DIR.gen/"hugo"/"hugo").in_dir(DIR.project)

def install():
    if not DIR.gen.joinpath("hugo").exists():
        Command(
            "wget", 
            "https://github.com/gohugoio/hugo/releases/download/v0.31.1/hugo_0.31.1_Linux-64bit.tar.gz",
        ).in_dir(DIR.gen).run()
    
        DIR.gen.chdir()
        patoolib.extract_archive(DIR.gen/"hugo_0.31.1_Linux-64bit.tar.gz")
        DIR.gen.joinpath("hugo_0.31.1_Linux-64bit.tar/").move(DIR.gen.joinpath("hugo"))
        DIR.gen.joinpath("hugo_0.31.1_Linux-64bit.tar.gz").remove()

@expected(CommandError)
def hugo(*args):
    """
    Run Hugo
    """
    hugo_cmd(*args).run()
  

@expected(CommandError)
def copystrictyaml():
    """
    Copy strictyaml
    """
    import pypandoc
    Command("hk", "docgen").in_dir(DIR.project.parent/"strictyaml").run()
    strictyaml_docs = DIR.project.parent/"strictyaml"/"hitch"/"gen"/"docs"
    
    for document in list(strictyaml_docs.walkfiles()):
        relative_path = document.replace(strictyaml_docs, "")
        content_path = DIR.project.joinpath("content", "strictyaml")
        write_path = content_path.joinpath(relative_path[1:])
        write_path_md = write_path.dirname().joinpath("{0}.md".format(write_path.namebase))
        
        if not write_path_md.dirname().exists():
            write_path_md.dirname().makedirs()
        if write_path_md.exists():
            write_path_md.remove()
        document.copy(write_path_md)
        #pypandoc.convert_file(
            #str(document),
            #"markdown",
            #format="rst",
            #outputfile=str(write_path_md),
        #)
    hugo("serve")
