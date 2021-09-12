#!/usr/bin/env python

from zensols.cli import ApplicationFactory
from io import StringIO

CONFIG = """
[cli]
class_name = zensols.cli.ActionCliManager
apps = list: pkg_cli, log_cli, app
default_action = install

[pkg_cli]
class_name = zensols.cli.PackageInfoImporter

[log_cli]
class_name = zensols.cli.LogConfigurator
log_name = ${package:name}
format = %%(asctime)s[%%(levelname)s]:%%(name)s %%(message)s
level = info

[import]
files = install.conf

[app]
class_name = app.Application
installer = instance: installer
"""


if __name__ == '__main__':
    cli = ApplicationFactory('app', StringIO(CONFIG))
    cli.invoke()
