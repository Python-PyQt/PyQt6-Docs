.. sip:method-description::
    :status: todo
    :pysig: 409ec1108091fa787eb7950c1f720008
    :realsig: () const
    :digest: 211f52afd6cd428e7021c06150adc3ac

This function returns the status of the Next Protocol Negotiation (NPN) or Application-Layer Protocol Negotiation (ALPN). If the feature has not been enabled through :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setAllowedNextProtocols`, this function returns :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.NextProtocolNegotiationStatus.NextProtocolNegotiationNone`. The status will be set before emitting the encrypted() signal.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setAllowedNextProtocols`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.allowedNextProtocols`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.nextNegotiatedProtocol`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.NextProtocolNegotiationStatus`.
