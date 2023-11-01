.. sip:method-description::
    :status: todo
    :pysig: b877d74319a03fb0b6bbf6bf0140f48d
    :realsig: (const QString&, int, QObject*)
    :digest: 9cbdb12a1d08608504305e434e381dec

Constructs a library object with the given *parent* that will load the library specified by *fileName* and major version number *verNum*. Currently, the version number is ignored on Windows.

We recommend omitting the file's suffix in *fileName*, since :sip:ref:`~PyQt6.QtCore.QLibrary` will automatically look for the file with the appropriate suffix in accordance with the platform, e.g. ".so" on Unix, ".dylib" on macOS and iOS, and ".dll" on Windows. (See :sip:ref:`~PyQt6.QtCore.QLibrary.fileName`.)
