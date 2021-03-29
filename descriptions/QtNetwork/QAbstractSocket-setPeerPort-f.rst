.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (quint16)
    :digest: ad596619258821f7ee866d887f33e8eb

Sets the port of the remote side of the connection to *port*.

You can call this function in a subclass of :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` to change the return value of the :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.peerPort` function after a connection has been established. This feature is commonly used by proxy connections for virtual connection settings.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.peerPort`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.setPeerAddress`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.setLocalPort`.
