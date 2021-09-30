.. sip:method-description::
    :status: todo
    :pysig: 4b5df69213eeb325fb253e866010b51a
    :realsig: (QWebSocketProtocol::CloseCode,const QString&)
    :digest: aed90a61fb3d92c32e149a2528aeb315

Gracefully closes the socket with the given *closeCode* and *reason*.

Any data in the write buffer is flushed before the socket is closed. The *closeCode* is a :sip:ref:`~PyQt6.QtWebSockets.QWebSocketProtocol.CloseCode` indicating the reason to close, and *reason* describes the reason of the closure more in detail. All control frames, including the Close frame, are limited to 125 bytes. Since two of these are used for *closeCode* the maximum length of *reason* is 123! If *reason* exceeds this limit it will be truncated.
