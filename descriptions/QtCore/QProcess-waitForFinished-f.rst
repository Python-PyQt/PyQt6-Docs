.. sip:method-description::
    :status: todo
    :pysig: 4ebcca4b876ddf43aac5582e04e14a68
    :realsig: (int)
    :digest: 084a35a2bd574b794f353c1638a46a49

Blocks until the process has finished and the :sip:ref:`~PyQt6.QtCore.QProcess.finished` signal has been emitted, or until *msecs* milliseconds have passed.

Returns ``true`` if the process finished; otherwise returns ``false`` (if the operation timed out, if an error occurred, or if this `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ is already finished).

This function can operate without an event loop. It is useful when writing non-GUI applications and when performing I/O operations in a non-GUI thread.

**Warning:** Calling this function from the main (GUI) thread might cause your user interface to freeze.

If msecs is -1, this function will not time out.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.finished`, :sip:ref:`~PyQt6.QtCore.QProcess.waitForStarted`, :sip:ref:`~PyQt6.QtCore.QProcess.waitForReadyRead`, :sip:ref:`~PyQt6.QtCore.QProcess.waitForBytesWritten`.
