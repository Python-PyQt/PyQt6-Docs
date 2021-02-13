.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: a502ba4a204f30fe51aa8c22e2ec35b1

Loads the root QML file located at *filePath*. *filePath* must be a path to a local file. If *filePath* is a relative path, it is taken as relative to the application's working directory. The object tree defined by the file is instantiated immediately.

If an error occurs, error messages are printed with :sip:ref:`~PyQt6.QtCore.qWarning`.
