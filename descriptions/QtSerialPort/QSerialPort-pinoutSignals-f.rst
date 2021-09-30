.. sip:method-description::
    :status: todo
    :pysig: 48732dc5ed03ee3a44a513f3652edf2a
    :realsig: ()
    :digest: e6a36bd5df24d541af5c9d49b3d5e017

Returns the state of the line signals in a bitmap format.

From this result, it is possible to allocate the state of the desired signal by applying a mask "AND", where the mask is the desired enumeration value from QSerialPort::PinoutSignals.

**Note:** This method performs a system call, thus ensuring that the line signal states are returned properly. This is necessary when the underlying operating systems cannot provide proper notifications about the changes.

**Note:** The serial port has to be open before trying to get the pinout signals; otherwise returns :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.PinoutSignal.NoSignal` and sets the :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.SerialPortError.NotOpenError` error code.

.. seealso:: QSerialPort::dataTerminalReady, QSerialPort::requestToSend.
