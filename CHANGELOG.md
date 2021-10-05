# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).


## [Unreleased]


### Changed
- Rename `Install.installs` to `Install.resources`.
- Switch `Resource.is_compressed` from a property to an attribute to make it
  overridable.
- Changed many cached `dict` to type `frozendict` to guard against
  unintentional modification of immutable data structures.
- Make base package relative to the ~/.cache directory if it exists.


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
[Unreleased]: https://github.com/Paul Landes/install/compare/v0.0.6...HEAD
[0.0.6]: https://github.com/Paul Landes/install/compare/v0.0.5...v0.0.6
[0.0.5]: https://github.com/Paul Landes/install/compare/v0.0.4...v0.0.5
[0.0.4]: https://github.com/Paul Landes/install/compare/v0.0.3...v0.0.4
[0.0.3]: https://github.com/Paul Landes/install/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/Paul Landes/install/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/Paul Landes/install/compare/v0.0.0...v0.0.1
