.. sip:method-description::
    :status: todo
    :pysig: 72027f48b9d878c3a64e8f2588649c1d
    :realsig: (const QString&,QObject*)
    :digest: cf10155d60f186629a0efad29689745c

Constructs a :sip:ref:`~PyQt6.QtCore.QTemporaryFile` with a template filename of *templateName* and the specified *parent*. Upon opening the temporary file this will be used to create a unique filename.

If the *templateName* does not contain XXXXXX it will automatically be appended and used as the dynamic portion of the filename.

If *templateName* is a relative path, the path will be relative to the current working directory. You can use :sip:ref:`~PyQt6.QtCore.QDir.tempPath` to construct *templateName* if you want use the system's temporary directory.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTemporaryFile.open`, :sip:ref:`~PyQt6.QtCore.QTemporaryFile.fileTemplate`.
