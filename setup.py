try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = "littlebrother",
    version = "0.1",
    description = "Quickly search through Nevada voters",
    author = "Eric Davis",
    author_email = "ed@npri.org",
    url = "https://github.com/edavis/littlebrother",
    packages = ["littlebrother"],
    install_requires = open('etc/requirements.txt').readlines(),
    include_package_data=True,
    zip_safe=False,
)
