.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: d6d6a88067662fd518df3f62b4c80c7e

Redirects the process' standard input to the file indicated by *fileName*. When an input redirection is in place, the :sip:ref:`~PyQt6.QtCore.QProcess` object will be in read-only mode (calling write() will result in error).

To make the process read EOF right away, pass :sip:ref:`~PyQt6.QtCore.QProcess.nullDevice` here. This is cleaner than using :sip:ref:`~PyQt6.QtCore.QProcess.closeWriteChannel` before writing any data, because it can be set up prior to starting the process.

If the file *fileName* does not exist at the moment :sip:ref:`~PyQt6.QtCore.QProcess.start` is called or is not readable, starting the process will fail.

Calling setStandardInputFile() after the process has started has no effect.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.setStandardOutputFile`, :sip:ref:`~PyQt6.QtCore.QProcess.setStandardErrorFile`, :sip:ref:`~PyQt6.QtCore.QProcess.setStandardOutputProcess`.
