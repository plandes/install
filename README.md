# Downloads and installs files

[![PyPI][pypi-badge]][pypi-link]
[![Python 3.11][python311-badge]][python311-link]
[![Build Status][build-badge]][build-link]

Simple light API to download and install files.  If the file appears to be a
compressed file by ending with `zip`, `tar.gz`, `tgz` etc, then also un-compress
the file after it is downloaded.  The process flow follows:

1. Check to see if the installed file exists.  If not download it.
1. Otherwise, if the file has been downloaded uncompress it.
1. If the file could not be downloaded, uncompressed, or a file from the
   uncompressed file isn't found an error is thrown.

A destination location can be specified in the configuration.  It is also
possible to install it in the `~/.cache/<package name>` where *package name* is
the name the installed package.  For example, that would be `zensols.install`
for the package installed for this repository.


## Documentation

* [Full documentation](https://plandes.github.io/install/index.html)
* [API reference](https://plandes.github.io/install/api.html)


## Obtaining

The easiest way to install the command line program is via the `pip` installer:
```bash
pip3 install zensols.install
```

Binaries are also available on [pypi].


## Usage

The below code is given in the [example].

First create the installer configuration with each file to be installed as a
resource as a file `install.conf`:
```ini
[zip_resource]
class_name = zensols.install.Resource
url = https://github.com/plandes/zenbuild/archive/refs/tags/general_build.zip
# we have to give the name of the diretory in the zip file so the program knows
# what to unzip; otherwise it is named from the section, or file if `None`
name = zenbuild-general_build
# uncomment below to keep the `zenbuild-general_build.zip` zip file
#clean_up = False

[downloader]
class_name = zensols.install.Downloader
#use_progress_bar = False

[installer]
class_name = zensols.install.Installer
downloader = instance: downloader
# uncomment the below line, then comment out `base_directory` to use the
# package name (using the zensols.cli.ApplicationFactory--see example); using
# `package_resource` will in install a ~/.<package name> install directory
base_directory = path: install_dir
#package_resource = ${package:name}
resources = instance: list: zip_resource
```

Now use the configuration to create the installer and call it:
```python
import logging
from zensols.config import IniConfig, ImportConfigFactory
from zensols.install import Installer

logging.basicConfig(level=logging.INFO)
fac = ImportConfigFactory(IniConfig('install.conf'))
installer: Installer = fac.instance('installer')
installer.install()
```

This code creates a new directory with the un-zipped files in `install_dir`:

```readline-config
INFO:zensols.install.installer:installing zenbuild-general_build to install_dir/zenbuild-general_build
INFO:zensols.install.download:creating directory: install_dir
INFO:zensols.install.download:downloading https://github.com/plandes/zenbuild/archive/refs/tags/general_build.zip to install_dir/zenbuild-general_build.zip
general_build.zip: 16.4kB [00:00, 40.1kB/s]
INFO:zensols.install.installer:uncompressing install_dir/zenbuild-general_build.zip to install_dir
patool: Extracting install_dir/zenbuild-general_build.zip ...
patool: ... install_dir/zenbuild-general_build.zip extracted to `install_dir'.
INFO:zensols.install.installer:cleaning up downloaded file: install_dir/zenbuild-general_build.zip
```

First the program checks to see if the target directory (`name` property in the
`zip_resource` section) exists.  It then downloads it when it can't find either
the target directory or the downloaded file.

If the program is run a second time, there will be no output since the
installed directory now exists.


## Changelog

An extensive changelog is available [here](CHANGELOG.md).


## License

[MIT License](LICENSE.md)

Copyright (c) 2021 - 2025 Paul Landes


<!-- links -->
[pypi]: https://pypi.org/project/zensols.install/
[pypi-link]: https://pypi.python.org/pypi/zensols.install
[pypi-badge]: https://img.shields.io/pypi/v/zensols.install.svg
[python311-badge]: https://img.shields.io/badge/python-3.11-blue.svg
[python311-link]: https://www.python.org/downloads/release/python-3110
[build-badge]: https://github.com/plandes/install/workflows/CI/badge.svg
[build-link]: https://github.com/plandes/install/actions

[example]: https://github.com/plandes/install/tree/master/example
