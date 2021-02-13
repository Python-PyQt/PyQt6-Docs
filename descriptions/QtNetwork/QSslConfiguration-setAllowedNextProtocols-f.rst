.. sip:method-description::
    :status: todo
    :pysig: 8851e0acc2178e167ff6e8b5fa63298c
    :realsig: (const QList<QByteArray>&)
    :digest: a70596af8d8ac919224a2fad783e950c

This function sets the allowed *protocols* to be negotiated with the server through the Next Protocol Negotiation (NPN) or Application-Layer Protocol Negotiation (ALPN) TLS extension; each element in *protocols* must define one allowed protocol. The function must be called explicitly before connecting to send the NPN/ALPN extension in the SSL handshake. Whether or not the negotiation succeeded can be queried through :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.nextProtocolNegotiationStatus`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.nextNegotiatedProtocol`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.nextProtocolNegotiationStatus`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.allowedNextProtocols`, QSslConfiguration::NextProtocolHttp1_1.
