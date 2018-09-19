from commandlib import python_bin, Command, CommandError
from hitchrun import DIR, expected
from pathquery import pathq
import patoolib
import shutil

hugo_dir = DIR.gen / "hugo"

def install():
    """
    Set up hugo.
    """
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
def buildprojectdocs(projectdir, projectname):
    """
    Build documentation from a project.
    """
    Command("hk", "docgen").in_dir(DIR.project.parent/projectdir).run()
    project_docs = DIR.project.parent/projectdir/"hitch"/"gen"/"docs"

    DIR.project.joinpath("content", projectname).rmtree(ignore_errors=True)

    for document in list(project_docs.walkfiles()):
        relative_path = document.replace(project_docs, "")
        content_path = DIR.project.joinpath("content", projectname)
        write_path = content_path.joinpath(relative_path[1:])
        write_path_md = write_path.dirname().joinpath("{0}.md".format(write_path.namebase))

        if not write_path_md.dirname().exists():
            write_path_md.dirname().makedirs()
        if write_path_md.exists():
            write_path_md.remove()
        document.copy(write_path_md)

def buildall():
    """
    Build all docs for all projects.
    """
    buildprojectdocs("strictyaml", "strictyaml")
    buildprojectdocs("story", "hitchstory")
    buildprojectdocs("seleniumdirector", "seleniumdirector")


def test():
    """
    Build all docs for all projects and run a test hugo server.
    """
    buildall()
    hugo("serve")


@expected(CommandError)
def publish():
    """
    Copy changes to hitchdev.com directory.
    """
    html_in = DIR.project / "public"
    html_in.rmtree(ignore_errors=True)
    html_in.mkdir()
    print("Building...")
    buildall()
    hugo()
    print("Moving...")
    for filepath in list(pathq(html_in)):
        dest = DIR.project.parent.joinpath("hitchdev.github.io", filepath.relpath(html_in))
        if not dest.dirname().exists():
            dest.dirname().makedirs()
        if not filepath.isdir():
            filepath.copy(dest.dirname())
        print(dest)


@expected(CommandError)
def push():
    """
    Push changes in hitchdev.github.com.
    """
    git = Command("git").in_dir(DIR.project/".."/"hitchdev.github.io")
    git("add", ".").run()
    git("commit", "-m", "Updates").run()
    git("push").run()
