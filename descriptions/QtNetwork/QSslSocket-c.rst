.. sip:class-description::
    :status: todo
    :brief: SSL encrypted socket for both clients and servers
    :digest: f182058bc3afdadad8ae93cf1e2c15f7

The :sip:ref:`~PyQt6.QtNetwork.QSslSocket` class provides an SSL encrypted socket for both clients and servers.

:sip:ref:`~PyQt6.QtNetwork.QSslSocket` establishes a secure, encrypted TCP connection you can use for transmitting encrypted data. It can operate in both client and server mode, and it supports modern SSL protocols, including SSL 3 and TLS 1.2. By default, :sip:ref:`~PyQt6.QtNetwork.QSslSocket` uses only SSL protocols which are considered to be secure (\ :sip:ref:`~PyQt6.QtNetwork.QSsl.SslProtocol.SecureProtocols`), but you can change the SSL protocol by calling :sip:ref:`~PyQt6.QtNetwork.QSslSocket.setProtocol` as long as you do it before the handshake has started.

SSL encryption operates on top of the existing TCP stream after the socket enters the :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.ConnectedState`. There are two simple ways to establish a secure connection using :sip:ref:`~PyQt6.QtNetwork.QSslSocket`: With an immediate SSL handshake, or with a delayed SSL handshake occurring after the connection has been established in unencrypted mode.

The most common way to use :sip:ref:`~PyQt6.QtNetwork.QSslSocket` is to construct an object and start a secure connection by calling :sip:ref:`~PyQt6.QtNetwork.QSslSocket.connectToHostEncrypted`. This method starts an immediate SSL handshake once the connection has been established.

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_ssl_qsslsocket.py
    :lines: 54-57

As with a plain :sip:ref:`~PyQt6.QtNetwork.QTcpSocket`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket` enters the :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.HostLookupState`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.ConnectingState`, and finally the :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.ConnectedState`, if the connection is successful. The handshake then starts automatically, and if it succeeds, the :sip:ref:`~PyQt6.QtNetwork.QSslSocket.encrypted` signal is emitted to indicate the socket has entered the encrypted state and is ready for use.

Note that data can be written to the socket immediately after the return from :sip:ref:`~PyQt6.QtNetwork.QSslSocket.connectToHostEncrypted` (i.e., before the :sip:ref:`~PyQt6.QtNetwork.QSslSocket.encrypted` signal is emitted). The data is queued in :sip:ref:`~PyQt6.QtNetwork.QSslSocket` until after the :sip:ref:`~PyQt6.QtNetwork.QSslSocket.encrypted` signal is emitted.

An example of using the delayed SSL handshake to secure an existing connection is the case where an SSL server secures an incoming connection. Suppose you create an SSL server class as a subclass of :sip:ref:`~PyQt6.QtNetwork.QTcpServer`. You would override :sip:ref:`~PyQt6.QtNetwork.QTcpServer.incomingConnection` with something like the example below, which first constructs an instance of :sip:ref:`~PyQt6.QtNetwork.QSslSocket` and then calls :sip:ref:`~PyQt6.QtNetwork.QSslSocket.setSocketDescriptor` to set the new socket's descriptor to the existing one passed in. It then initiates the SSL handshake by calling :sip:ref:`~PyQt6.QtNetwork.QSslSocket.startServerEncryption`.

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_ssl_qsslsocket.py
    :lines: 62-72

If an error occurs, :sip:ref:`~PyQt6.QtNetwork.QSslSocket` emits the :sip:ref:`~PyQt6.QtNetwork.QSslSocket.sslErrors` signal. In this case, if no action is taken to ignore the error(s), the connection is dropped. To continue, despite the occurrence of an error, you can call :sip:ref:`~PyQt6.QtNetwork.QSslSocket.ignoreSslErrors`, either from within this slot after the error occurs, or any time after construction of the :sip:ref:`~PyQt6.QtNetwork.QSslSocket` and before the connection is attempted. This will allow :sip:ref:`~PyQt6.QtNetwork.QSslSocket` to ignore the errors it encounters when establishing the identity of the peer. Ignoring errors during an SSL handshake should be used with caution, since a fundamental characteristic of secure connections is that they should be established with a successful handshake.

Once encrypted, you use :sip:ref:`~PyQt6.QtNetwork.QSslSocket` as a regular :sip:ref:`~PyQt6.QtNetwork.QTcpSocket`. When readyRead() is emitted, you can call read(), :sip:ref:`~PyQt6.QtNetwork.QSslSocket.canReadLine` and readLine(), or getChar() to read decrypted data from :sip:ref:`~PyQt6.QtNetwork.QSslSocket`'s internal buffer, and you can call write() or putChar() to write data back to the peer. :sip:ref:`~PyQt6.QtNetwork.QSslSocket` will automatically encrypt the written data for you, and emit :sip:ref:`~PyQt6.QtNetwork.QSslSocket.encryptedBytesWritten` once the data has been written to the peer.

As a convenience, :sip:ref:`~PyQt6.QtNetwork.QSslSocket` supports :sip:ref:`~PyQt6.QtNetwork.QTcpSocket`'s blocking functions :sip:ref:`~PyQt6.QtNetwork.QSslSocket.waitForConnected`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.waitForReadyRead`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.waitForBytesWritten`, and :sip:ref:`~PyQt6.QtNetwork.QSslSocket.waitForDisconnected`. It also provides :sip:ref:`~PyQt6.QtNetwork.QSslSocket.waitForEncrypted`, which will block the calling thread until an encrypted connection has been established.

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_ssl_qsslsocket.py
    :lines: 77-86

:sip:ref:`~PyQt6.QtNetwork.QSslSocket` provides an extensive, easy-to-use API for handling cryptographic ciphers, private keys, and local, peer, and Certification Authority (CA) certificates. It also provides an API for handling errors that occur during the handshake phase.

The following features can also be customized:

* The socket's cryptographic cipher suite can be customized before the handshake phase with :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setCiphers` and QSslConfiguration::setDefaultCiphers().

* The socket's local certificate and private key can be customized before the handshake phase with :sip:ref:`~PyQt6.QtNetwork.QSslSocket.setLocalCertificate` and :sip:ref:`~PyQt6.QtNetwork.QSslSocket.setPrivateKey`.

* The CA certificate database can be extended and customized with :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.addCaCertificate`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.addCaCertificates`.

To extend the list of *default* CA certificates used by the SSL sockets during the SSL handshake you must update the default configuration, as in the snippet below:

::

    QList<QSslCertificate> certificates = getCertificates();
    QSslConfiguration configuration = QSslConfiguration::defaultConfiguration();
    configuration.addCaCertificates(certificates);
    QSslConfiguration::setDefaultConfiguration(configuration);

**Note:** If available, root certificates on Unix (excluding macOS) will be loaded on demand from the standard certificate directories. If you do not want to load root certificates on demand, you need to call either :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.defaultConfiguration`.setCaCertificates() before the first SSL handshake is made in your application (for example, via passing QSslSocket::systemCaCertificates() to it), or call :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.defaultConfiguration`::setCaCertificates() on your :sip:ref:`~PyQt6.QtNetwork.QSslSocket` instance prior to the SSL handshake.

For more information about ciphers and certificates, refer to :sip:ref:`~PyQt6.QtNetwork.QSslCipher` and :sip:ref:`~PyQt6.QtNetwork.QSslCertificate`.

This product includes software developed by the OpenSSL Project for use in the OpenSSL Toolkit (`http://www.openssl.org/ <http://www.openssl.org/>`_).

**Note:** Be aware of the difference between the bytesWritten() signal and the :sip:ref:`~PyQt6.QtNetwork.QSslSocket.encryptedBytesWritten` signal. For a :sip:ref:`~PyQt6.QtNetwork.QTcpSocket`, bytesWritten() will get emitted as soon as data has been written to the TCP socket. For a :sip:ref:`~PyQt6.QtNetwork.QSslSocket`, bytesWritten() will get emitted when the data is being encrypted and :sip:ref:`~PyQt6.QtNetwork.QSslSocket.encryptedBytesWritten` will get emitted as soon as data has been written to the TCP socket.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslCertificate`, :sip:ref:`~PyQt6.QtNetwork.QSslCipher`, :sip:ref:`~PyQt6.QtNetwork.QSslError`.
