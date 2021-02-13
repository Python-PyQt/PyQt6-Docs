.. sip:class-description::
    :status: todo
    :brief: Holds the configuration and state of an SSL connection
    :digest: 1edbd196e23de86f24e5a2facaafec09

The :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration` class holds the configuration and state of an SSL connection.

:sip:ref:`~PyQt6.QtNetwork.QSslConfiguration` is used by Qt networking classes to relay information about an open SSL connection and to allow the application to control certain features of that connection.

The settings that :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration` currently supports are:

* The SSL/TLS protocol to be used

* The certificate to be presented to the peer during connection and its associated private key

* The ciphers allowed to be used for encrypting the connection

* The list of Certificate Authorities certificates that are used to validate the peer's certificate

These settings are applied only during the connection handshake. Setting them after the connection has been established has no effect.

The state that :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration` supports are:

* The certificate the peer presented during handshake, along with the chain leading to a CA certificate

* The cipher used to encrypt this session

The state can only be obtained once the SSL connection starts, but not necessarily before it's done. Some settings may change during the course of the SSL connection without need to restart it (for instance, the cipher can be changed over time).

State in :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration` objects cannot be changed.

:sip:ref:`~PyQt6.QtNetwork.QSslConfiguration` can be used with :sip:ref:`~PyQt6.QtNetwork.QSslSocket` and the Network Access API.

Note that changing settings in :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration` is not enough to change the settings in the related SSL connection. You must call setSslConfiguration on a modified :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration` object to achieve that. The following example illustrates how to change the protocol to TLSv1_0 in a :sip:ref:`~PyQt6.QtNetwork.QSslSocket` object:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_ssl_qsslconfiguration.py
    :lines: 54-56

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSsl.SslProtocol`, :sip:ref:`~PyQt6.QtNetwork.QSslCertificate`, :sip:ref:`~PyQt6.QtNetwork.QSslCipher`, :sip:ref:`~PyQt6.QtNetwork.QSslKey`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.sslConfiguration`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.setSslConfiguration`.
