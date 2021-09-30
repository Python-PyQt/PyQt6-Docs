.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 460cc2e2e0ab236ff1c93fe4511706a9

This function writes as much as possible from the internal write buffer to the underlying serial port without blocking. If any data was written, this function returns ``true``; otherwise returns ``false``.

Call this function for sending the buffered data immediately to the serial port. The number of bytes successfully written depends on the operating system. In most cases, this function does not need to be called, because the :sip:ref:`~PyQt6.QtSerialPort.QSerialPort` class will start sending data automatically once control is returned to the event loop. In the absence of an event loop, call :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.waitForBytesWritten` instead.

**Note:** The serial port has to be open before trying to flush any buffered data; otherwise returns ``false`` and sets the :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.SerialPortError.NotOpenError` error code.

.. seealso:: write(), :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.waitForBytesWritten`.
