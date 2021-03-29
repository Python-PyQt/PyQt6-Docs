.. sip:class-description::
    :status: todo
    :brief: This class represents Online Certificate Status Protocol response
    :digest: a57c261b8886e8a1430add3b7709a6c7

This class represents Online Certificate Status Protocol response.

The :sip:ref:`~PyQt6.QtNetwork.QOcspResponse` class represents the revocation status of a server's certficate, received by the client-side socket during the TLS handshake. :sip:ref:`~PyQt6.QtNetwork.QSslSocket` must be configured with OCSP stapling enabled.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.ocspResponses`, :sip:ref:`~PyQt6.QtNetwork.QOcspResponse.certificateStatus`, :sip:ref:`~PyQt6.QtNetwork.QOcspResponse.revocationReason`, :sip:ref:`~PyQt6.QtNetwork.QOcspResponse.responder`, :sip:ref:`~PyQt6.QtNetwork.QOcspResponse.subject`, QOcspCertificateStatus, QOcspRevocationReason, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setOcspStaplingEnabled`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.ocspStaplingEnabled`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.peerCertificate`.
