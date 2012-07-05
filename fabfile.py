from fabric.api import *

env.hosts = ["transparentnevada.com:4789"]
env.user = "django"

def pack(commit="HEAD"):
    """
    Create an archive from the given commit.

    Returns the basename of the file (so deploy can `put` the file
    easily).
    """
    output = local("git describe %s" % commit, capture=True)
    local("git archive --format=tar.gz --prefix=littlebrother/ -o /tmp/littlebrother-%(output)s.tar.gz %(commit)s" %
          dict(commit=commit, output=output))
    return "littlebrother-%s.tar.gz" % output

def deploy(commit="HEAD", upgrade=False):
    output = pack(commit)
    put("/tmp/%s" % output, "/tmp")
    with cd("/srv/environments/littlebrother"):
        run("tar xf /tmp/%s" % output)
        # If upgrade=True, upgrade even the deps
        if upgrade:
            run("bin/pip install -U ./littlebrother/")

        # otherwise, reinstall littlebrother but don't worry about
        # checking the deps
        else:
            run("bin/pip install -U --no-deps ./littlebrother/")
            run("bin/pip install ./littlebrother/")

        run("rm -rf littlebrother")
        run("rm -f /tmp/%s" % output)
