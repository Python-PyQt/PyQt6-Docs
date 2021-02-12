.. sip:method-description::
    :status: todo
    :pysig: 47bc384ef78158df7bdc68df0f06aef9
    :realsig: (int)
    :digest: cd8257799479f1fe6b0f2facfe051894

For buffered devices, this function waits until a payload of buffered written data has been written to the device and the :sip:ref:`~PyQt6.QtCore.QIODevice.bytesWritten` signal has been emitted, or until *msecs* milliseconds have passed. If msecs is -1, this function will not time out. For unbuffered devices, it returns immediately.

Returns ``true`` if a payload of data was written to the device; otherwise returns ``false`` (i.e. if the operation timed out, or if an error occurred).

This function can operate without an event loop. It is useful when writing non-GUI applications and when performing I/O operations in a non-GUI thread.

If called from within a slot connected to the :sip:ref:`~PyQt6.QtCore.QIODevice.bytesWritten` signal, :sip:ref:`~PyQt6.QtCore.QIODevice.bytesWritten` will not be reemitted.

Reimplement this function to provide a blocking API for a custom device. The default implementation does nothing, and returns ``false``.

**Warning:** Calling this function from the main (GUI) thread might cause your user interface to freeze.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.waitForReadyRead`.
