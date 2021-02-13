.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 3744573b9be81c3d5ec2b479128b62db

Returns the size of the internal read buffer. This limits the amount of data that the client can receive before you call read() or readAll(). A read buffer size of 0 (the default) means that the buffer has no size limit, ensuring that no data is lost.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.setReadBufferSize`, read().
