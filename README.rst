OSX GCC Installer
=================

The osx-gcc-installer allows you to install the essential compilers from either pre-built binary packages or helps you create your own installer.

For Lion and above users, **Apple now provides an official Command Line Tools for Xcode package** that you can install without needing to install Xcode itself! You can install it with ``xcode-select --install`` on Mavericks and Yosemite or download it from `Apple's developer site <https://developer.apple.com/downloads/>`_ (free registration required) and search for "Command Line Tools" on Lion and Mountain Lion.

If you still need gcc-4.2, and you use Homebrew, you can install it using the apple-gcc42 package from homebrew/dupes.

Option 1: Downloading Pre-Built Binaries
----------------------------------------

You can download the installers on the
`Releases page <https://github.com/kennethreitz/osx-gcc-installer/releases>`_ or use the links below:

* OS X 10.7 Lion: `GCC-10.7-v0.3.pkg <https://github.com/kennethreitz/osx-gcc-installer/releases/download/v0.3/GCC-10.7-v0.3.zip>`_
* OS X 10.6 Snow Leopard: `GCC-10.6-v0.3.pkg <https://github.com/kennethreitz/osx-gcc-installer/releases/download/v0.3/GCC-10.6-v0.3.zip>`_

Option 2: Build Your Own
------------------------

To create your own package, place the Xcode Installer for your OS version
(``Install Xcode.app``) in the root directory of the repository, and edit the
packages_list.txt file to include the packages you want. Then run the build.py script::

        python build.py

it will produce a build_essentials.pkg file by default, containing all the
desired packages. For example, if you want to include all the default packages
but want to add the 10.6 SDK, the file would look as follows::

        DevSDK.pkg
        DeveloperToolsCLI.pkg
        MacOSX10.6.pkg
        clang.pkg
        llvm-gcc4.2.pkg
        gcc4.2.pkg


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
installing osx-gcc-installer.
