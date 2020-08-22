from os import curdir
import click
import pkg_resources
import shutil
import string
import os

from .helper import copytree


@click.group("project")
def project_group():
    """
    Command untuk membuat project kivy.
    """


@project_group.command("create")
@click.argument("name")
@click.option("--curdir", is_flag=True)
def create_project(name, curdir):
    """
    Membuat project.
    """

    if not curdir and os.path.isdir(name):
        click.echo("Maaf, project telah tersedia :'(")
        exit(1)

    click.echo("Membuat project dengan nama %r..." % name)
    project_dir = name if not curdir else os.getcwd()
    tmpl = pkg_resources.resource_filename("kvuilder", "data/templates")
    copytree(tmpl, project_dir)
    main_py = os.path.join(project_dir, "main.py")
    with open(main_py) as fp:
        main_t = string.Template(fp.read())
        main_data = main_t.safe_substitute(nama_program=name)

    with open(main_py, "w") as fp:
        fp.write(main_data)

    program_py = os.path.join(project_dir, "program.py")
    os.rename(program_py, os.path.join(project_dir, name + ".py"))

    pyi_file = os.path.join(project_dir, "pyinstaller.spec")
    with open(pyi_file) as fp:
        data_tmp = string.Template(fp.read())
        data = data_tmp.safe_substitute(nama_program=name)

    with open(pyi_file, "w") as fp:
        fp.write(data)

    os.rename(pyi_file, os.path.join(project_dir, name + ".spec"))
    click.echo("Project %r berhasil dibuat!" % name)


@project_group.group("screen")
def project_screen_group():
    """
    Mengelola screen pada spesifik project.
    """


@project_screen_group.command("create")
@click.option("--name", required=True, help="Nama screen.")
def create_screen(name):
    """
    Membuat screen pada project.
    """

    dst = os.path.join("libs", "screens", name)
    if os.path.isdir(dst):
        click.echo("Screen %r telah dibuat!" % name)
        exit(1)

    click.echo("Membuat screen %r ..." % name)
    tmpl = pkg_resources.resource_filename("kvuilder", "data/screen")
    copytree(tmpl, dst)
    view_py = os.path.join(dst, "view.py")
    with open(view_py) as fp:
        t_view = string.Template(fp.read())
        view_data = t_view.safe_substitute(nama_screen=name)

    with open(view_py, "w") as fp:
        fp.write(view_data)

    dst = os.path.join("libs", "stylesheet", name)
    if not os.path.isdir(dst):
        tmpl = pkg_resources.resource_filename("kvuilder", "data/stylesheet")
        copytree(tmpl, dst)

    click.echo("Screen %r berhasil dibuat!" % name)


@project_screen_group.command("remove")
@click.option("--name", required=True, help="Nama screen.")
def remove_screen(name):
    """
    Hapus screen dari project.
    """

    dst = os.path.join("libs", "screens", name)
    if os.path.isdir(dst):
        click.echo("Menghapus screen %r..." % name)
        shutil.rmtree(dst)
        dst = os.path.join("libs", "stylesheet", name)
        if os.path.isdir(dst):
            shutil.rmtree(dst)
        click.echo("Screen %r berhasil dihapus!" % name)
    else:
        click.echo("Screen %r tidak ditemukan!" % name)
