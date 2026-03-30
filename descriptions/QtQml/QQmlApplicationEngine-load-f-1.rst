.. sip:method-description::
    :status: todo
    :pysig: 464116456943d857ef223b2d24ec328b
    :realsig: (const QString&)
    :digest: a502ba4a204f30fe51aa8c22e2ec35b1

Loads the root QML file located at *filePath*. *filePath* must be a path to a local file or a path to a file in the resource file system. If *filePath* is a relative path, it is taken as relative to the application's working directory. The object tree defined by the file is instantiated immediately.

If an error occurs, error messages are printed with :sip:ref:`~PyQt6.QtCore.qWarning`.
