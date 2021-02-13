.. sip:class-description::
    :status: todo
    :brief: Authentication data for pre shared keys (PSK) ciphersuites
    :digest: 4093c8738b639779d15d0f93f67d5f74

The :sip:ref:`~PyQt6.QtNetwork.QSslPreSharedKeyAuthenticator` class provides authentication data for pre shared keys (PSK) ciphersuites.

The :sip:ref:`~PyQt6.QtNetwork.QSslPreSharedKeyAuthenticator` class is used by an SSL socket to provide the required authentication data in a pre shared key (PSK) ciphersuite.

In a PSK handshake, the client must derive a key, which must match the key set on the server. The exact algorithm of deriving the key depends on the application; however, for this purpose, the server may send an *identity hint* to the client. This hint, combined with other information (for instance a passphrase), is then used by the client to construct the shared key.

The :sip:ref:`~PyQt6.QtNetwork.QSslPreSharedKeyAuthenticator` provides means to client applications for completing the PSK handshake. The client application needs to connect a slot to the :sip:ref:`~PyQt6.QtNetwork.QSslSocket.preSharedKeyAuthenticationRequired` signal:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_ssl_qsslpresharedkeyauthenticator.py
    :lines: 43-44

The signal carries a :sip:ref:`~PyQt6.QtNetwork.QSslPreSharedKeyAuthenticator` object containing the identity hint the server sent to the client, and which must be filled with the corresponding client identity and the derived key:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_ssl_qsslpresharedkeyauthenticator.py
    :lines: 48-54

**Note:** PSK ciphersuites are supported only when using OpenSSL 1.0.1 (or greater) as the SSL backend.

**Note:** PSK is currently only supported in OpenSSL.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket`.
