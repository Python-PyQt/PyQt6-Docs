.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (qint64)
    :digest: af89befac2605b11656b0536ca5539c1

Sets the size of :sip:ref:`~PyQt6.QtSerialPort.QSerialPort`'s internal write buffer to be *size* bytes.

Sending the data over serial port is relatively slow, so in practice, when write() is called, the data is not sent immediately. It is first stored in an intermediate buffer and later written in chunks.

Thus, an attempt to write too much data or write data at a higher rate than the underlying serial port can handle, can lead to a situation when the internal buffer will grow. This can eventually cause the application to run out of memory, specially on a device with low memory resources.

This method allows to limit the internal buffer to a certain size. If the next write attempt exceeds the capacity of the buffer, the write() method will return the amount of bytes that were actually stored in the buffer. It's the user's responsibility to repeat the write attempt with the rest of the bytes after the bytesWritten() signal was received, or after the :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.waitForBytesWritten` method returns ``true``.

Passing ``0`` to this method means that the input buffer is not limited, and all the incoming data is buffered. This is the default.

.. seealso:: :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.writeBufferSize`, write().
