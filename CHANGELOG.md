v0.3.1

- Connect to database as user 'django'
- Change how restarts happen now that we're using uwsgi in emperor
  mode

v0.3

- Add config files for nginx, uwsgi and supervisord
- Use Fabric for deployment

v0.2

- Add search and precinct pagination
- Improve setup.py
    - Include SQL init scripts in share/
    - Include sample uwsgi config in etc/
- Refactor Voter search
- Handle empty cities better
- Don't display voters on index page

v0.1

- Initial release
