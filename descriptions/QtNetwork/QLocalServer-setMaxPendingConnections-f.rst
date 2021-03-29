.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 4219a7c7205ffa80f37428bb970551db

Sets the maximum number of pending accepted connections to *numConnections*. :sip:ref:`~PyQt6.QtNetwork.QLocalServer` will accept no more than *numConnections* incoming connections before :sip:ref:`~PyQt6.QtNetwork.QLocalServer.nextPendingConnection` is called.

Note: Even though :sip:ref:`~PyQt6.QtNetwork.QLocalServer` will stop accepting new connections after it has reached its maximum number of pending connections, the operating system may still keep them in queue which will result in clients signaling that it is connected.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalServer.maxPendingConnections`, :sip:ref:`~PyQt6.QtNetwork.QLocalServer.hasPendingConnections`.
