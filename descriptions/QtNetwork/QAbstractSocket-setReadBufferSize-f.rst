.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (qint64)
    :digest: c73dd95ccdb34d56007bf9479b643e4e

Sets the size of :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket`'s internal read buffer to be *size* bytes.

If the buffer size is limited to a certain size, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` won't buffer more than this size of data. Exceptionally, a buffer size of 0 means that the read buffer is unlimited and all incoming data is buffered. This is the default.

This option is useful if you only read the data at certain points in time (e.g., in a real-time streaming application) or if you want to protect your socket against receiving too much data, which may eventually cause your application to run out of memory.

Only :sip:ref:`~PyQt6.QtNetwork.QTcpSocket` uses :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket`'s internal buffer; :sip:ref:`~PyQt6.QtNetwork.QUdpSocket` does not use any buffering at all, but rather relies on the implicit buffering provided by the operating system. Because of this, calling this function on :sip:ref:`~PyQt6.QtNetwork.QUdpSocket` has no effect.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.readBufferSize`, read().
