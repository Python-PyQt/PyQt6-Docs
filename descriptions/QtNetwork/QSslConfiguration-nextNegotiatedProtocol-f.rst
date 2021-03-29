.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: () const
    :digest: a9776052e5febab18e602187e07de770

This function returns the protocol negotiated with the server if the Next Protocol Negotiation (NPN) or Application-Layer Protocol Negotiation (ALPN) TLS extension was enabled. In order for the NPN/ALPN extension to be enabled, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setAllowedNextProtocols` needs to be called explicitly before connecting to the server.

If no protocol could be negotiated or the extension was not enabled, this function returns a :sip:ref:`~PyQt6.QtCore.QByteArray` which is null.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setAllowedNextProtocols`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.nextProtocolNegotiationStatus`.
