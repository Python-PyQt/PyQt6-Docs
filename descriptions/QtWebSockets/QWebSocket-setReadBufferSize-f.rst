.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (qint64)
    :digest: 4931d8d88ddec77f936b95eaa4f7be46

Sets the size of :sip:ref:`~PyQt6.QtWebSockets.QWebSocket`'s internal read buffer to be *size* bytes.

If the buffer size is limited to a certain size, :sip:ref:`~PyQt6.QtWebSockets.QWebSocket` won't buffer more than this size of data. Exceptionally, a buffer size of 0 means that the read buffer is unlimited and all incoming data is buffered. This is the default. This option is useful if you only read the data at certain points in time (for example, in a real-time streaming application) or if you want to protect your socket against receiving too much data, which may eventually cause your application to run out of memory.

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.readBufferSize`.
