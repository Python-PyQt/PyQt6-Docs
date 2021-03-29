.. sip:method-description::
    :status: todo
    :pysig: 4913b7f41d155f3f2c358feda901791b
    :realsig: (const QString&,const QString&,QObject*)
    :digest: 3f11768efe60369ccd99a7b12833b04e

Constructs a library object with the given *parent* that will load the library specified by *fileName* and full version number *version*. Currently, the version number is ignored on Windows.

We recommend omitting the file's suffix in *fileName*, since :sip:ref:`~PyQt6.QtCore.QLibrary` will automatically look for the file with the appropriate suffix in accordance with the platform, e.g. ".so" on Unix, ".dylib" on macOS and iOS, and ".dll" on Windows. (See :sip:ref:`~PyQt6.QtCore.QLibrary.fileName`.)
