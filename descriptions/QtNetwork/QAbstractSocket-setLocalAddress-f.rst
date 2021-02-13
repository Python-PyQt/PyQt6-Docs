.. sip:method-description::
    :status: todo
    :pysig: b21af316e8fe4b5a829510e730325475
    :realsig: (const QHostAddress&)
    :digest: 29ff82a35d07ac218875fd6b3313daca

Sets the address on the local side of a connection to *address*.

You can call this function in a subclass of :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` to change the return value of the :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.localAddress` function after a connection has been established. This feature is commonly used by proxy connections for virtual connection settings.

Note that this function does not bind the local address of the socket prior to a connection (e.g., :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.bind`).

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.localAddress`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.setLocalPort`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.setPeerAddress`.
