.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: b002a62a4efaecc9b16e8a27979faae2

Returns the size of the internal read buffer. This limits the amount of data that the client can receive before calling the read() or readAll() methods.

A read buffer size of ``0`` (the default) means that the buffer has no size limit, ensuring that no data is lost.

.. seealso:: :sip:ref:`~PyQt6.QtSerialPort.QSerialPort.setReadBufferSize`, read().
