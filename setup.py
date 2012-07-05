try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

data_files = {'etc/littlebrother': ['etc/littlebrother-uwsgi.ini'],
              'share/littlebrother': ['share/create_voters_table.sql',
                                      'share/create_search_indexes.sql']}
setup(
    name = "littlebrother",
    version = "0.2",
    description = "Quickly search through Nevada voters",
    author = "Eric Davis",
    author_email = "ed@npri.org",
    url = "https://github.com/edavis/littlebrother",
    packages = ["littlebrother"],
    install_requires = open('etc/requirements.txt').readlines(),
    include_package_data=True,
    zip_safe=False,
    data_files=data_files.items(),
)
