Developing
----------

* create a virtualenv
  ```mkvirtualenv --system-site-packages dev_show_geom```
* install the plugin
  ```python setup.py develop```
* use the virtualenv python binary to launch fview so it finds the plugin
  installed in the virtualenv
  ```~/.virtualenvs/new_show_geom/bin/python /usr/bin/fview```
