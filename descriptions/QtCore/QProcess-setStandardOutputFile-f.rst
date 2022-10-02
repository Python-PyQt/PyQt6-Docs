.. sip:method-description::
    :status: todo
    :pysig: 7f7efeca02d72c35dfd231a41f8373a3
    :realsig: (const QString&,QIODeviceBase::OpenMode)
    :digest: 6ae3788df4a89f807f669bc420fbd6bd

Redirects the process' standard output to the file *fileName*. When the redirection is in place, the standard output read channel is closed: reading from it using read() will always fail, as will :sip:ref:`~PyQt6.QtCore.QProcess.readAllStandardOutput`.

To discard all standard output from the process, pass :sip:ref:`~PyQt6.QtCore.QProcess.nullDevice` here. This is more efficient than simply never reading the standard output, as no :sip:ref:`~PyQt6.QtCore.QProcess` buffers are filled.

If the file *fileName* doesn't exist at the moment :sip:ref:`~PyQt6.QtCore.QProcess.start` is called, it will be created. If it cannot be created, the starting will fail.

If the file exists and *mode* is QIODevice::Truncate, the file will be truncated. Otherwise (if *mode* is QIODevice::Append), the file will be appended to.

Calling setStandardOutputFile() after the process has started has no effect.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.setStandardInputFile`, :sip:ref:`~PyQt6.QtCore.QProcess.setStandardErrorFile`, :sip:ref:`~PyQt6.QtCore.QProcess.setStandardOutputProcess`.
