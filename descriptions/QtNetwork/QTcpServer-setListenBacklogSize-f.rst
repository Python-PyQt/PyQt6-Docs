.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 9efd35ad981eece82f79d1db2211b7d2

Sets the backlog queue size of to be accepted connections to *size*. The operating system might reduce or ignore this value. By default, the queue size is 50.

**Note:** This property must be set prior to calling :sip:ref:`~PyQt6.QtNetwork.QTcpServer.listen`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QTcpServer.listenBacklogSize`.
