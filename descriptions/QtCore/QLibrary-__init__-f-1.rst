.. sip:method-description::
    :status: todo
    :pysig: be4cf29ba73c5c1c9c66cbed303bedcd
    :realsig: (const QString&,QObject*)
    :digest: 35930d516bde947dcc2cff71b4f2d205

Constructs a library object with the given *parent* that will load the library specified by *fileName*.

We recommend omitting the file's suffix in *fileName*, since :sip:ref:`~PyQt6.QtCore.QLibrary` will automatically look for the file with the appropriate suffix in accordance with the platform, e.g. ".so" on Unix, ".dylib" on macOS and iOS, and ".dll" on Windows. (See :sip:ref:`~PyQt6.QtCore.QLibrary.fileName`.)
