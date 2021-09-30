.. sip:signal-description::
    :status: todo
    :pysig: 7e9fe7e96e744aa55dd6d3c9ec39fbd4
    :realsig: (QAbstractSocket::SocketState)
    :digest: 83c011f76f3fe18778db548ad861479a

This signal is emitted whenever :sip:ref:`~PyQt6.QtWebSockets.QWebSocket`'s state changes. The *state* parameter is the new state.

**Note:** :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.ConnectedState` is emitted after the handshake with the server has succeeded.

:sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState` is not a registered metatype, so for queued connections, you will have to register it with Q_REGISTER_METATYPE() and qRegisterMetaType().

.. seealso:: :sip:ref:`~PyQt6.QtWebSockets.QWebSocket.state`.
