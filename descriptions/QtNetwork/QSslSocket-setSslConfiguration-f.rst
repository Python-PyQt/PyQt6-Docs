.. sip:method-description::
    :status: todo
    :pysig: 540d03d543282018ff34d52a022e932e
    :realsig: (const QSslConfiguration&)
    :digest: 027cc6d40e44c81b5605dff0acc2862d

Sets the socket's SSL configuration to be the contents of *configuration*. This function sets the local certificate, the ciphers, the private key and the CA certificates to those stored in *configuration*.

It is not possible to set the SSL-state related fields.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.sslConfiguration`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.setLocalCertificate`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.setPrivateKey`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setCaCertificates`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setCiphers`.
