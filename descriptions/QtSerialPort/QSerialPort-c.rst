.. sip:class-description::
    :status: todo
    :brief: Provides functions to access serial ports
    :digest: be26e94d2f8760bd4744ae0de26792f4

Provides functions to access serial ports.

You can get information about the available serial ports using the :sip:ref:`~PyQt6.QtSerialPort.QSerialPortInfo` helper class, which allows an enumeration of all the serial ports in the system. This is useful to obtain the correct name of the serial port you want to use. You can pass an object of the helper class as an argument to the :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.setPort` or :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.setPortName` methods to assign the desired serial device.

After setting the port, you can open it in read-only (r/o), write-only (w/o), or read-write (r/w) mode using the :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.open` method.

**Note:** The serial port is always opened with exclusive access (that is, no other process or thread can access an already opened serial port).

Use the :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.close` method to close the port and cancel the I/O operations.

Having successfully opened, :sip:ref:`~PyQt6.QtSerialPort.QSerialPort` tries to determine the current configuration of the port and initializes itself. You can reconfigure the port to the desired setting using the :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.setBaudRate`, :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.setDataBits`, :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.setParity`, :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.setStopBits`, and :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.setFlowControl` methods.

There are a couple of properties to work with the pinout signals namely: QSerialPort::dataTerminalReady, QSerialPort::requestToSend. It is also possible to use the :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.pinoutSignals` method to query the current pinout signals set.

Once you know that the ports are ready to read or write, you can use the read() or write() methods. Alternatively the readLine() and readAll() convenience methods can also be invoked. If not all the data is read at once, the remaining data will be available for later as new incoming data is appended to the :sip:ref:`~PyQt6.QtSerialPort.QSerialPort`'s internal read buffer. You can limit the size of the read buffer using :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.setReadBufferSize`.

:sip:ref:`~PyQt6.QtSerialPort.QSerialPort` provides a set of functions that suspend the calling thread until certain signals are emitted. These functions can be used to implement blocking serial ports:

* :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.waitForReadyRead` blocks calls until new data is available for reading.

* :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.waitForBytesWritten` blocks calls until one payload of data has been written to the serial port.

See the following example:

::

    int numRead = 0, numReadTotal = 0;
    char buffer[50];

    for (;;) {
        numRead  = serial.read(buffer, 50);

        // Do whatever with the array

        numReadTotal += numRead;
        if (numRead == 0 && !serial.waitForReadyRead())
            break;
    }

If :sip:ref:`~PyQt6.QtCore.QIODevice.waitForReadyRead` returns ``false``, the connection has been closed or an error has occurred.

If an error occurs at any point in time, :sip:ref:`~PyQt6.QtSerialPort.QSerialPort` will emit the :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.errorOccurred` signal. You can also call :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.error` to find the type of error that occurred last.

Programming with a blocking serial port is radically different from programming with a non-blocking serial port. A blocking serial port does not require an event loop and typically leads to simpler code. However, in a GUI application, blocking serial port should only be used in non-GUI threads, to avoid freezing the user interface.

For more details about these approaches, refer to the `example <https://doc.qt.io/qt-6/qtserialport-examples.html>`_ applications.

The :sip:ref:`~PyQt6.QtSerialPort.QSerialPort` class can also be used with :sip:ref:`~PyQt6.QtCore.QTextStream` and :sip:ref:`~PyQt6.QtCore.QDataStream`'s stream operators (operator<<() and operator>>()). There is one issue to be aware of, though: make sure that enough data is available before attempting to read by using the operator>>() overloaded operator.

.. seealso:: :sip:ref:`~PyQt6.QtSerialPort.QSerialPortInfo`.
