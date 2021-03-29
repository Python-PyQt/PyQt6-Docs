.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: a37a45392ead75613364dafe27c7b334

Sets the maximum number of pending accepted connections to *numConnections*. :sip:ref:`~PyQt6.QtNetwork.QTcpServer` will accept no more than *numConnections* incoming connections before :sip:ref:`~PyQt6.QtNetwork.QTcpServer.nextPendingConnection` is called. By default, the limit is 30 pending connections.

Clients may still able to connect after the server has reached its maximum number of pending connections (i.e., :sip:ref:`~PyQt6.QtNetwork.QTcpSocket` can still emit the connected() signal). :sip:ref:`~PyQt6.QtNetwork.QTcpServer` will stop accepting the new connections, but the operating system may still keep them in queue.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QTcpServer.maxPendingConnections`, :sip:ref:`~PyQt6.QtNetwork.QTcpServer.hasPendingConnections`.
