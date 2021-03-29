.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: ba9c97ebe1bb63674758a26b51163810

Constructs a :sip:ref:`~PyQt6.QtCore.QTemporaryFile` using as file template the application name returned by :sip:ref:`~PyQt6.QtCore.QCoreApplication.applicationName` (otherwise ``qt_temp``) followed by ".XXXXXX". The file is stored in the system's temporary directory, :sip:ref:`~PyQt6.QtCore.QDir.tempPath`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTemporaryFile.setFileTemplate`, :sip:ref:`~PyQt6.QtCore.QDir.tempPath`.
