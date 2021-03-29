.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 9b282421ec11501794e83b6f98907901

Redirects the process' standard input to the file indicated by *fileName*. When an input redirection is in place, the `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ object will be in read-only mode (calling write() will result in error).

To make the process read EOF right away, pass :sip:ref:`~PyQt6.QtCore.QProcess.nullDevice` here. This is cleaner than using :sip:ref:`~PyQt6.QtCore.QProcess.closeWriteChannel` before writing any data, because it can be set up prior to starting the process.

If the file *fileName* does not exist at the moment :sip:ref:`~PyQt6.QtCore.QProcess.start` is called or is not readable, starting the process will fail.

Calling  after the process has started has no effect.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.setStandardOutputFile`, :sip:ref:`~PyQt6.QtCore.QProcess.setStandardErrorFile`, :sip:ref:`~PyQt6.QtCore.QProcess.setStandardOutputProcess`.
