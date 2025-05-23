# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).


## [Unreleased]


## [1.2.1] - 2025-02-15
### Added
- A method (`Installer.clear`) to remove downloaded and/or installed files.


## [1.2.0] - 2025-01-11
### Removed
- Support for Python 3.10.

### Changed
- Upgraded to [zensols.util] version 1.15.


## [1.1.2] - 2024-03-05
### Changed
- Error report messages.


## [1.1.1] - 2024-01-16
### Changed
- Pin `patools` (utility used to decompress downloaded files) to version 1.12
  for older systems without file `--no-sandbox`.


## [1.1.0] - 2023-12-05
### Changed
- Relax [zensols.util] dependencies.

### Added
- Support for Python 3.11.

### Removed
- Support for Python 3.9.


## [1.0.0] - 2023-08-16
Functional and downstream moderate risk update release.

### Changed
- Add extracted file check before installing.


## [0.2.2] - 2023-06-29
### Changed
- Add extracted file check before installing.


## [0.2.1] - 2023-04-05
### Changed
- Add dependency.
- Raise error when automatic download fails.


## [0.2.0] - 2023-01-23
### Changed
- Updated [zensols.util] to 1.12.0.


## [0.1.0] - 2022-10-01
### Added
- File system update commands (GoF pattern) in `Resource`.

### Removed
- `Resource.clean_up_paths`, which has been obviated by `RemoveUpdate` file
  system update command.


## [0.0.10] - 2022-10-01
## Added
- A sub path in `Resource`.
- Installer is writable.


## [0.0.9] - 2022-08-06
### Added
- Authenticated downloads are now available.
- Download previous and new functionality tests.

### Changed
- Remove deprecated `urllib` API for `urlopen`.  This adds a buffer size that
  is configurable in the `Downloader` instance with a reasonable default.
- Robustly handle `file` protocol schemes.


## [0.0.8] - 2022-01-25
### Changed
- Allow install resource rename to follow through against target rather than a
  check path.


## [0.0.7] - 2021-10-22
### Changed
- Rename `Install.installs` to `Install.resources`.
- Switch `Resource.is_compressed` from a property to an attribute to make it
  overridable.
- Changed many cached `dict` to type `frozendict` to guard against
  unintentional modification of immutable data structures.
- Make base package relative to the` ~/.cache directory` if it exists.
- Add singleton path to make path resolution in `Installer` easier to narrow.


## [0.0.6] - 2021-10-03
### Added
- Add configuration for a sub directory to be appended to the base directory.


## [0.0.5] - 2021-10-02
### Added
- Configuration to override `Resource.remote_name`.


## [0.0.4] - 2021-09-22
### Changed
- Better uncompress semantics and factual result status.


## [0.0.3] - 2021-09-21
### Added
- An attribute of a path to check before compressing and flag to avoid renaming
  for zip files that un-compress in the relative root directory.


## [0.0.2] - 2021-09-21
### Changed
- Installer is more *Pythonic*.
- Fix variable naming error message.

### Added
- Installer is *writable*.
- Handle `.gz` and `.bz2` files.


## [0.0.1] - 2021-09-02
### Added
- Initial version.


<!-- links -->
[Unreleased]: https://github.com/Paul Landes/install/compare/v1.2.1...HEAD
[1.2.1]: https://github.com/Paul Landes/install/compare/v1.2.0...v1.2.1
[1.2.0]: https://github.com/Paul Landes/install/compare/v1.1.2...v1.2.0
[1.1.2]: https://github.com/Paul Landes/install/compare/v1.1.1...v1.1.2
[1.1.1]: https://github.com/Paul Landes/install/compare/v1.1.0...v1.1.1
[1.1.0]: https://github.com/Paul Landes/install/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/Paul Landes/install/compare/v0.2.2...v1.0.0
[0.2.2]: https://github.com/Paul Landes/install/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/Paul Landes/install/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/Paul Landes/install/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/Paul Landes/install/compare/v0.0.10...v0.1.0
[0.0.10]: https://github.com/Paul Landes/install/compare/v0.0.9...v0.0.10
[0.0.9]: https://github.com/Paul Landes/install/compare/v0.0.8...v0.0.9
[0.0.8]: https://github.com/Paul Landes/install/compare/v0.0.7...v0.0.8
[0.0.7]: https://github.com/Paul Landes/install/compare/v0.0.6...v0.0.7
[0.0.6]: https://github.com/Paul Landes/install/compare/v0.0.5...v0.0.6
[0.0.5]: https://github.com/Paul Landes/install/compare/v0.0.4...v0.0.5
[0.0.4]: https://github.com/Paul Landes/install/compare/v0.0.3...v0.0.4
[0.0.3]: https://github.com/Paul Landes/install/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/Paul Landes/install/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/Paul Landes/install/compare/v0.0.0...v0.0.1

[zensols.util]: https://github.com/plandes/util
