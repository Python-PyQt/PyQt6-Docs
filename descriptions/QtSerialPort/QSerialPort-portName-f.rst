.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: a6892ad925c8e01ac7e3f51eca7839bf

Returns the name set by :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.setPort` or passed to the :sip:ref:`~PyQt6.QtSerialPort.QSerialPort` constructor. This name is short, i.e. it is extracted and converted from the internal variable system location of the device. The conversion algorithm is platform specific:

+-----------+----------------------------------------------------------------------------------------------------------+
| Platform  | Brief Description                                                                                        |
+===========+==========================================================================================================+
| Windows   | Removes the prefix "\\\\.\\" or "//./" from the system location and returns the remainder of the string. |
+-----------+----------------------------------------------------------------------------------------------------------+
| Unix, BSD | Removes the prefix "/dev/" from the system location and returns the remainder of the string.             |
+-----------+----------------------------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.setPortName`, :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.setPort`, :sip:ref:`~PyQt6.QtSerialPort.QSerialPortInfo.portName`.
