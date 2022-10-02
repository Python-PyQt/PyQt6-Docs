.. sip:signal-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 86535272e1aa7506c6c3894a3eee289e

This signal is emitted when new data is available for reading from the device. The *channel* argument is set to the index of the read channel on which the data has arrived. Unlike :sip:ref:`~PyQt6.QtCore.QIODevice.readyRead`, it is emitted regardless of the :sip:ref:`~PyQt6.QtCore.QIODevice.currentReadChannel`.

channelReadyRead() can be emitted recursively - even for the same channel.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.readyRead`, :sip:ref:`~PyQt6.QtCore.QIODevice.channelBytesWritten`.
