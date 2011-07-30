OSX GCC Installer
=================

Downloading and installing the *massive* Xcode installer is a huge hassle
if you just want GCC and related tools.

So, here's the PackageMaker files for creating a minimal installer,
extracted from the Xcode packages yourself!

To create the package, place the appropriate Xcode Installer package
(``Install Xcode.app``) in the root directory of the repository, then open
the appropriate ``.pmdoc`` to build!

Downloads
---------

You can download the pre-made installers on the
`Downloads page <https://github.com/kennethreitz/osx-gcc-installer/downloads>`_.

* `GCC-10.7.pkg <https://github.com/downloads/kennethreitz/osx-gcc-installer/GCC-10.7.pkg>`_
* `GCC-10.6.pkg <https://github.com/downloads/kennethreitz/osx-gcc-installer/GCC-10.6.pkg>`_

Includes
--------

* GCC
* LLVM
* Clang
* Developer CLI Tools (purge, etc)
* DevSDK (headers, etc)