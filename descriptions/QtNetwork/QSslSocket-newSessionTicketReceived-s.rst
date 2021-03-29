.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 56451a777c093c7189000f28c9008e15

If TLS 1.3 protocol was negotiated during a handshake, :sip:ref:`~PyQt6.QtNetwork.QSslSocket` emits this signal after receiving NewSessionTicket message. Session and session ticket's lifetime hint are updated in the socket's configuration. The session can be used for session resumption (and a shortened handshake) in future TLS connections.

**Note:** This functionality enabled only with OpenSSL backend and requires OpenSSL v 1.1.1 or above.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.sslConfiguration`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.sessionTicket`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.sessionTicketLifeTimeHint`.
