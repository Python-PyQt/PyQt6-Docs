.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: e6d58b9d1b8a1a81357489e930bd6a26

If *cannotRecover* is true, and verification mode in use is :sip:ref:`~PyQt6.QtNetwork.QSslSocket.PeerVerifyMode.VerifyPeer` or :sip:ref:`~PyQt6.QtNetwork.QSslSocket.PeerVerifyMode.AutoVerifyPeer` (for a client-side socket), the missing peer's certificate would be treated as an unrecoverable error that cannot be ignored. A proper alert message will be sent to the peer before closing the connection.

**Note:** Only available if Qt was configured and built with OpenSSL backend.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.ignoreSslErrors`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.PeerVerifyMode`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.missingCertificateIsFatal`.
