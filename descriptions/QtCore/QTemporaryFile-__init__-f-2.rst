.. sip:method-description::
    :status: todo
    :pysig: 2b9057d9b4a06375acf76e6922f506e2
    :realsig: (QObject*)
    :digest: e61cc02572c87861fc1754f0a57766f2

Constructs a :sip:ref:`~PyQt6.QtCore.QTemporaryFile` with the given *parent*.

The default file name template is determined from the application name as returned by :sip:ref:`~PyQt6.QtCore.QCoreApplication.applicationName` (or ``"qt_temp"`` if the application name is empty), followed by ``".XXXXXX"``. The file is stored in the system's temporary directory, as returned by :sip:ref:`~PyQt6.QtCore.QDir.tempPath`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTemporaryFile.setFileTemplate`.
