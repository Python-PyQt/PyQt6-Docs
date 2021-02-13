.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (quint16)
    :digest: 8667871d7529f3a331daf9964d0d047b

Sets the port on the local side of a connection to *port*.

You can call this function in a subclass of :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` to change the return value of the :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.localPort` function after a connection has been established. This feature is commonly used by proxy connections for virtual connection settings.

Note that this function does not bind the local port of the socket prior to a connection (e.g., :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.bind`).

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.localPort`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.localAddress`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.setLocalAddress`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.setPeerPort`.
