.. sip:signal-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (qint64)
    :digest: 390eb66924ca7ca70d5e39e027882a69

This signal is emitted every time a payload of data has been written to the device's current write channel. The *bytes* argument is set to the number of bytes that were written in this payload.

bytesWritten() is not emitted recursively; if you reenter the event loop or call :sip:ref:`~PyQt6.QtCore.QIODevice.waitForBytesWritten` inside a slot connected to the bytesWritten() signal, the signal will not be reemitted (although :sip:ref:`~PyQt6.QtCore.QIODevice.waitForBytesWritten` may still return true).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.readyRead`.
