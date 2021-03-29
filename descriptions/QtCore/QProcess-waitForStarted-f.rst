.. sip:method-description::
    :status: todo
    :pysig: 4ebcca4b876ddf43aac5582e04e14a68
    :realsig: (int)
    :digest: 36a4c1eab34fb25e536b5d2d6cad7258

Blocks until the process has started and the :sip:ref:`~PyQt6.QtCore.QProcess.started` signal has been emitted, or until *msecs* milliseconds have passed.

Returns ``true`` if the process was started successfully; otherwise returns ``false`` (if the operation timed out or if an error occurred).

This function can operate without an event loop. It is useful when writing non-GUI applications and when performing I/O operations in a non-GUI thread.

**Warning:** Calling this function from the main (GUI) thread might cause your user interface to freeze.

If msecs is -1, this function will not time out.

**Note:** On some UNIX operating systems, this function may return true but the process may later report a :sip:ref:`~PyQt6.QtCore.QProcess.ProcessError.FailedToStart` error.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.started`, :sip:ref:`~PyQt6.QtCore.QProcess.waitForReadyRead`, :sip:ref:`~PyQt6.QtCore.QProcess.waitForBytesWritten`, :sip:ref:`~PyQt6.QtCore.QProcess.waitForFinished`.
