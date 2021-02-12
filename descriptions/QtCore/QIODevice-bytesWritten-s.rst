.. sip:signal-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (qint64)
    :digest: 51181940f5e3ab7330f49a0c77c8ff85

This signal is emitted every time a payload of data has been written to the device's current write channel. The *bytes* argument is set to the number of bytes that were written in this payload.

is not emitted recursively; if you reenter the event loop or call :sip:ref:`~PyQt6.QtCore.QIODevice.waitForBytesWritten` inside a slot connected to the  signal, the signal will not be reemitted (although :sip:ref:`~PyQt6.QtCore.QIODevice.waitForBytesWritten` may still return true).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.readyRead`.
