OSX GCC Installer
=================

Downloading and installing the *massive* Xcode installer is a huge hassle
if you just want GCC and related tools.

The osx-gcc-installer allows you to install the essential compilers from either pre-built binary packages or helps you create your own installer.

For Lion and Mountain Lion users, **Apple now provides an official Command Line Tools for Xcode package** that you can install without needing to install Xcode itself! You can download it from `Apple's developer site <https://developer.apple.com/downloads/>`_ (free registration required) and search for "Command Line Tools".

If you still need gcc-4.2, and you use Homebrew, you can install it using the apple-gcc42 package from homebrew/dupes.

Option 1: Downloading Pre-Built Binaries
----------------------------------------

You can download the installers on the
`Downloads page <https://github.com/kennethreitz/osx-gcc-installer/downloads>`_ or use the links below:

* OS X 10.8 Mountain Lion: `GCC-10.7.pkg <https://github.com/downloads/kennethreitz/osx-gcc-installer/GCC-10.7-v2.pkg>`_ (Includes 10.7 Headers, so use with caution).
* OS X 10.7 Lion: `GCC-10.7.pkg <https://github.com/downloads/kennethreitz/osx-gcc-installer/GCC-10.7-v2.pkg>`_
* OS X 10.6 Snow Leopard: `GCC-10.6.pkg <https://github.com/downloads/kennethreitz/osx-gcc-installer/GCC-10.6.pkg>`_

Option 2: Build Your Own
------------------------

To create your own package, place the Xcode Installer for your OS version
(``Install Xcode.app``) in the root directory of the repository, then open
the matching ``.pmdoc`` to build!

What's Included?
----------------

* GCC
* LLVM
* Clang
* Developer CLI Tools (purge, etc)
* DevSDK (headers, etc)

References
----------

The source code from Apple for these packages is available here:

- http://www.opensource.apple.com/release/developer-tools-41/


Troubleshooting
---------------

*Do not install this if you already have Xcode installed!* Mixing Xcode and osx-gcc-installer
is known to cause various difficult-to-diagnose problems and is not recommended.

If you intend to only use command line tools you should first uninstall Xcode entirely before
installing osx-gcc-installer, or see below for other options.

