.. sip:method-description::
    :status: todo
    :pysig: 47bc384ef78158df7bdc68df0f06aef9
    :realsig: (int)
    :digest: b747aaa9e24d8b260897ac4d66cee0ba

Blocks until new data is available for reading and the :sip:ref:`~PyQt6.QtCore.QIODevice.readyRead` signal has been emitted, or until *msecs* milliseconds have passed. If msecs is -1, this function will not time out.

Returns ``true`` if new data is available for reading; otherwise returns false (if the operation timed out or if an error occurred).

This function can operate without an event loop. It is useful when writing non-GUI applications and when performing I/O operations in a non-GUI thread.

If called from within a slot connected to the :sip:ref:`~PyQt6.QtCore.QIODevice.readyRead` signal, :sip:ref:`~PyQt6.QtCore.QIODevice.readyRead` will not be reemitted.

Reimplement this function to provide a blocking API for a custom device. The default implementation does nothing, and returns ``false``.

**Warning:** Calling this function from the main (GUI) thread might cause your user interface to freeze.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.waitForBytesWritten`.
