.. sip:method-description::
    :status: todo
    :pysig: b21af316e8fe4b5a829510e730325475
    :realsig: (const QHostAddress&)
    :digest: bfaeef4401cec3ea27120faffaba1e27

Sets the address of the remote side of the connection to *address*.

You can call this function in a subclass of :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` to change the return value of the :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.peerAddress` function after a connection has been established. This feature is commonly used by proxy connections for virtual connection settings.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.peerAddress`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.setPeerPort`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.setLocalAddress`.
