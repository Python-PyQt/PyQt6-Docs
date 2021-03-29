.. sip:method-description::
    :status: todo
    :pysig: 2b9057d9b4a06375acf76e6922f506e2
    :realsig: (QObject*)
    :digest: 21c736bf4c29b61c91fe1877d4d1f41e

Constructs a :sip:ref:`~PyQt6.QtCore.QTemporaryFile` (with the given *parent*) using as file template the application name returned by :sip:ref:`~PyQt6.QtCore.QCoreApplication.applicationName` (otherwise ``qt_temp``) followed by ".XXXXXX". The file is stored in the system's temporary directory, :sip:ref:`~PyQt6.QtCore.QDir.tempPath`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTemporaryFile.setFileTemplate`.
