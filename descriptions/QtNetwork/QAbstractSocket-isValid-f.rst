.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 5a539d7e3391184d7d21bc2d7fe05a80

Returns ``true`` if the socket is valid and ready for use; otherwise returns ``false``.

**Note:** The socket's state must be :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.ConnectedState` before reading and writing can occur.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.state`.
