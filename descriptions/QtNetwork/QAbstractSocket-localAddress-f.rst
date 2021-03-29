.. sip:method-description::
    :status: todo
    :pysig: ec82a7f8c43ec9633e2975527eb9f362
    :realsig: () const
    :digest: bd3fe8211eda647421f77b15e3309e2b

Returns the host address of the local socket if available; otherwise returns :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress.Null`.

This is normally the main IP address of the host, but can be :sip:ref:`~PyQt6.QtNetwork.QHostAddress.SpecialAddress.LocalHost` (127.0.0.1) for connections to the local host.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.localPort`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.peerAddress`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.setLocalAddress`.
