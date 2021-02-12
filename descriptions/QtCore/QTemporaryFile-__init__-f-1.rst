.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 0e45190d994af21151d5b25b963131d5

Constructs a :sip:ref:`~PyQt6.QtCore.QTemporaryFile` with a template filename of *templateName*. Upon opening the temporary file this will be used to create a unique filename.

If the *templateName* does not contain XXXXXX it will automatically be appended and used as the dynamic portion of the filename.

If *templateName* is a relative path, the path will be relative to the current working directory. You can use :sip:ref:`~PyQt6.QtCore.QDir.tempPath` to construct *templateName* if you want use the system's temporary directory.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTemporaryFile.open`, :sip:ref:`~PyQt6.QtCore.QTemporaryFile.fileTemplate`.
