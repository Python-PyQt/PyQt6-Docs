.. sip:signal-description::
    :status: todo
    :pysig: 71d06f3b9098dee6b0c54e0375ee433f
    :realsig: (QWebSocketCorsAuthenticator*)
    :digest: da74f236390fe58fc497a8653951c495

This signal is emitted when a new connection is requested. The slot connected to this signal should indicate whether the origin (which can be determined by the origin() call) is allowed in the *authenticator* object (by issuing :sip:ref:`~PyQt6.QtWebSockets.QWebSocketCorsAuthenticator.setAllowed`).

If no slot is connected to this signal, all origins will be accepted by default.

**Note:** It is not possible to use a QueuedConnection to connect to this signal, as the connection will always succeed.
