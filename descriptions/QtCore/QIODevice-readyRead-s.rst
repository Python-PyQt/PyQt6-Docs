.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: d53f1d90c69cde7646f571dac47cc478

This signal is emitted once every time new data is available for reading from the device's current read channel. It will only be emitted again once new data is available, such as when a new payload of network data has arrived on your network socket, or when a new block of data has been appended to your device.

readyRead() is not emitted recursively; if you reenter the event loop or call :sip:ref:`~PyQt6.QtCore.QIODevice.waitForReadyRead` inside a slot connected to the readyRead() signal, the signal will not be reemitted (although :sip:ref:`~PyQt6.QtCore.QIODevice.waitForReadyRead` may still return true).

Note for developers implementing classes derived from :sip:ref:`~PyQt6.QtCore.QIODevice`: you should always emit readyRead() when new data has arrived (do not emit it only because there's data still to be read in your buffers). Do not emit readyRead() in other conditions.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.bytesWritten`.
