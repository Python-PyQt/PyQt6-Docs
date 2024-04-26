.. sip:method-description::
    :status: todo
    :pysig: 4ebcca4b876ddf43aac5582e04e14a68
    :realsig: (int)
    :digest: 64b42afe932be4a706860d8e762091ba

Blocks until the process has started and the :sip:ref:`~PyQt6.QtCore.QProcess.started` signal has been emitted, or until *msecs* milliseconds have passed.

Returns ``true`` if the process was started successfully; otherwise returns ``false`` (if the operation timed out or if an error occurred). If the process had already started successfully before this function, it returns immediately.

This function can operate without an event loop. It is useful when writing non-GUI applications and when performing I/O operations in a non-GUI thread.

**Warning:** Calling this function from the main (GUI) thread might cause your user interface to freeze.

If msecs is -1, this function will not time out.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.started`, :sip:ref:`~PyQt6.QtCore.QProcess.waitForReadyRead`, :sip:ref:`~PyQt6.QtCore.QProcess.waitForBytesWritten`, :sip:ref:`~PyQt6.QtCore.QProcess.waitForFinished`.
