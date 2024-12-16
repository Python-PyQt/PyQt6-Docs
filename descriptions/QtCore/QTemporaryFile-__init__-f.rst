.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 1a66b76c004380a77fe62fbdfff62179

Constructs a :sip:ref:`~PyQt6.QtCore.QTemporaryFile`.

The default file name template is determined from the application name as returned by :sip:ref:`~PyQt6.QtCore.QCoreApplication.applicationName` (or ``"qt_temp"`` if the application name is empty), followed by ``".XXXXXX"``. The file is stored in the system's temporary directory, as returned by :sip:ref:`~PyQt6.QtCore.QDir.tempPath`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTemporaryFile.setFileTemplate`, :sip:ref:`~PyQt6.QtCore.QTemporaryFile.fileTemplate`, :sip:ref:`~PyQt6.QtCore.QTemporaryFile.fileName`, :sip:ref:`~PyQt6.QtCore.QDir.tempPath`.
