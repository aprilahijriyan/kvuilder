import click
import pkg_resources
import shutil
import string
import os

@click.group("project")
def project_group():
    """
    Command untuk membuat project kivy.
    """

@project_group.command("create")
@click.argument("name")
def create_project(name):
    """
    Membuat project.
    """

    if os.path.isdir(name):
        click.echo("Maaf, project telah tersedia :'(")
        exit(1)

    click.echo("Membuat project dengan nama %r..." % name)
    tmpl = pkg_resources.resource_filename("kvuilder", "data/templates")
    shutil.copytree(tmpl, name)
    main_py = os.path.join(name, "main.py")
    with open(main_py) as fp:
        main_t = string.Template(fp.read())
        main_data = main_t.safe_substitute(nama_program=name)

    with open(main_py, "w") as fp:
        fp.write(main_data)

    program_py = os.path.join(name, "program.py")
    os.rename(program_py, os.path.join(name, name + ".py"))
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
    shutil.copytree(tmpl, dst)
    view_py = os.path.join(dst, 'view.py')
    with open(view_py) as fp:
        t_view = string.Template(fp.read())
        view_data = t_view.safe_substitute(nama_screen=name.capitalize())

    with open(view_py, "w") as fp:
        fp.write(view_data)

    dst = os.path.join("libs", "stylesheet", name)
    if not os.path.isdir(dst):
        tmpl = pkg_resources.resource_filename("kvuilder", "data/stylesheet")
        shutil.copytree(tmpl, dst)

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
