.. sip:signal-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int,qint64)
    :digest: 8e773989a5684834f4da6adc58f670e4

This signal is emitted every time a payload of data has been written to the device. The *bytes* argument is set to the number of bytes that were written in this payload, while *channel* is the channel they were written to. Unlike :sip:ref:`~PyQt6.QtCore.QIODevice.bytesWritten`, it is emitted regardless of the :sip:ref:`~PyQt6.QtCore.QIODevice.currentWriteChannel`.

can be emitted recursively - even for the same channel.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.bytesWritten`, :sip:ref:`~PyQt6.QtCore.QIODevice.channelReadyRead`.
