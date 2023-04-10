.. sip:class-description::
    :status: todo
    :brief: Provides information about existing serial ports
    :digest: ffe597b30eaee7fdc8e7de9278bc7866

Provides information about existing serial ports.

Use the static :sip:ref:`~PyQt6.QtSerialPort.QSerialPortInfo.availablePorts` function to generate a list of :sip:ref:`~PyQt6.QtSerialPort.QSerialPortInfo` objects. Each :sip:ref:`~PyQt6.QtSerialPort.QSerialPortInfo` object in the list represents a single serial port and can be queried for the :sip:ref:`~PyQt6.QtSerialPort.QSerialPortInfo.portName`, :sip:ref:`~PyQt6.QtSerialPort.QSerialPortInfo.systemLocation`, :sip:ref:`~PyQt6.QtSerialPort.QSerialPortInfo.description`, :sip:ref:`~PyQt6.QtSerialPort.QSerialPortInfo.manufacturer`, and some other hardware parameters. The :sip:ref:`~PyQt6.QtSerialPort.QSerialPortInfo` class can also be used as an input parameter for the :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.setPort` method of the :sip:ref:`~PyQt6.QtSerialPort.QSerialPort` class.

.. _qserialportinfo-example-usage:

Example Usage
-------------

The example code enumerates all available serial ports and prints their parameters to console:

.. literalinclude:: ../../../snippets/qtserialport-src-serialport-doc-snippets-doc_src_serialport.py
    :lines: 14-30

.. seealso:: :sip:ref:`~PyQt6.QtSerialPort.QSerialPort`.
