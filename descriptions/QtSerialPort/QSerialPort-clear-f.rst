.. sip:method-description::
    :status: todo
    :pysig: 1e8bd0e7a417916053ca01ac22fe7479
    :realsig: (QSerialPort::Directions)
    :digest: 8fc88a55e7afc5dff308f5617cdc25d4

Discards all characters from the output or input buffer, depending on given directions *directions*. This includes clearing the internal class buffers and the UART (driver) buffers. Also terminate pending read or write operations. If successful, returns ``true``; otherwise returns ``false``.

**Note:** The serial port has to be open before trying to clear any buffered data; otherwise returns ``false`` and sets the :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.SerialPortError.NotOpenError` error code.
