.. sip:method-description::
    :status: todo
    :pysig: 7f7efeca02d72c35dfd231a41f8373a3
    :realsig: (const QString&,QIODeviceBase::OpenMode)
    :digest: ee979bb8b85b02816c9ea0180998eb85

Redirects the process' standard error to the file *fileName*. When the redirection is in place, the standard error read channel is closed: reading from it using read() will always fail, as will :sip:ref:`~PyQt6.QtCore.QProcess.readAllStandardError`. The file will be appended to if *mode* is Append, otherwise, it will be truncated.

See :sip:ref:`~PyQt6.QtCore.QProcess.setStandardOutputFile` for more information on how the file is opened.

Note: if :sip:ref:`~PyQt6.QtCore.QProcess.setProcessChannelMode` was called with an argument of :sip:ref:`~PyQt6.QtCore.QProcess.ProcessChannelMode.MergedChannels`, this function has no effect.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.setStandardInputFile`, :sip:ref:`~PyQt6.QtCore.QProcess.setStandardOutputFile`, :sip:ref:`~PyQt6.QtCore.QProcess.setStandardOutputProcess`.
