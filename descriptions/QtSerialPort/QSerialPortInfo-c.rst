.. sip:class-description::
    :status: todo
    :brief: Provides information about existing serial ports
    :digest: 04448e43b549f07a5534283186724cc0

Provides information about existing serial ports.

Use the static :sip:ref:`~PyQt6.QtSerialPort.QSerialPortInfo.availablePorts` function to generate a list of :sip:ref:`~PyQt6.QtSerialPort.QSerialPortInfo` objects. Each :sip:ref:`~PyQt6.QtSerialPort.QSerialPortInfo` object in the list represents a single serial port and can be queried for the :sip:ref:`~PyQt6.QtSerialPort.QSerialPortInfo.portName`, :sip:ref:`~PyQt6.QtSerialPort.QSerialPortInfo.systemLocation`, :sip:ref:`~PyQt6.QtSerialPort.QSerialPortInfo.description`, :sip:ref:`~PyQt6.QtSerialPort.QSerialPortInfo.manufacturer`, and some other hardware parameters. The :sip:ref:`~PyQt6.QtSerialPort.QSerialPortInfo` class can also be used as an input parameter for the :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.setPort` method of the :sip:ref:`~PyQt6.QtSerialPort.QSerialPort` class.

.. _qserialportinfo-example-usage:

Example Usage
-------------

The example code enumerates all available serial ports and prints their parameters to console:

.. literalinclude:: ../../../snippets/qtserialport-src-serialport-doc-snippets-doc_src_serialport.py
    :lines: 14-30

.. _qserialportinfo-port-enumeration-on-linux:

Port enumeration on Linux
-------------------------

By default Linux uses ``libudev`` to enumerate the available serial ports. If the library is not available, it falls back to reading files in the ``/sys/class/tty`` directory.

It is known that some versions of ``libudev`` have a bug and incorrectly report VID and PID of a USB hub instead of the actual device. In such cases, define the ``QT_SERIALPORT_SKIP_UDEV_LOOKUP`` environment variable to skip the ``libudev`` lookup and only use the information from the ``/sys/class/tty`` directory.

.. seealso:: :sip:ref:`~PyQt6.QtSerialPort.QSerialPort`.
