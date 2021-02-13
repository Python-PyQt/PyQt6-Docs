.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 97341c001c1d35657cfa6d3dd6d06e97

Returns ``true`` if the socket is valid and ready for use; otherwise returns ``false``.

**Note:** The socket's state must be :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.LocalSocketState.ConnectedState` before reading and writing can occur.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.state`, :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.connectToServer`.
