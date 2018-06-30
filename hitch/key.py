from commandlib import python_bin, Command, CommandError
from hitchrun import DIR, expected
from pathquery import pathq
import patoolib
import shutil

hugo_dir = DIR.gen / "hugo"

def install():
    if not hugo_dir.exists():
        Command(
            "wget", 
            "https://github.com/gohugoio/hugo/releases/download/v0.31.1/hugo_0.31.1_Linux-64bit.tar.gz",
        ).in_dir(DIR.gen).run()
    
        DIR.gen.chdir()
        patoolib.extract_archive(DIR.gen/"hugo_0.31.1_Linux-64bit.tar.gz")
        DIR.gen.joinpath("hugo_0.31.1_Linux-64bit.tar/").move(hugo_dir)
        DIR.gen.joinpath("hugo_0.31.1_Linux-64bit.tar.gz").remove()


@expected(CommandError)
def hugo(*args):
    """
    Run Hugo
    """
    Command(hugo_dir/"hugo").in_dir(DIR.project)(*args).run()
  

@expected(CommandError)
def copystrictyaml():
    """
    Copy strictyaml
    """
    Command("hk", "docgen").in_dir(DIR.project.parent/"strictyaml").run()
    strictyaml_docs = DIR.project.parent/"strictyaml"/"hitch"/"gen"/"docs"
    
    DIR.project.joinpath("content", "strictyaml").rmtree(ignore_errors=True)
    
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


def test():
    copystrictyaml()
    hugo("serve")


@expected(CommandError)
def publish():
    """
    Push changes to hitchdev.com.
    """
    html_in = DIR.project / "public"
    html_in.rmtree(ignore_errors=True)
    html_in.mkdir()
    print("Building...")
    copystrictyaml()
    hugo()
    print("Moving...")
    for filepath in list(pathq(html_in)):
        dest = DIR.project.parent.joinpath("hitchdev.github.io", filepath.relpath(html_in))
        if not dest.dirname().exists():
            dest.dirname().makedirs()
        if not filepath.isdir():
            filepath.copy(dest.dirname())
        print(dest)
