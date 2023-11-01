.. sip:method-description::
    :status: todo
    :pysig: 6c3abb151e246a11ae73e07fd8688c27
    :realsig: (const QString&, quint16, QIODeviceBase::OpenMode, QAbstractSocket::NetworkLayerProtocol)
    :digest: ac7831c8a2356092e5b3d04ed4db1c1c

Starts an encrypted connection to the device *hostName* on *port*, using *mode* as the OpenMode. This is equivalent to calling :sip:ref:`~PyQt6.QtNetwork.QSslSocket.connectToHost` to establish the connection, followed by a call to :sip:ref:`~PyQt6.QtNetwork.QSslSocket.startClientEncryption`. The *protocol* parameter can be used to specify which network protocol to use (eg. IPv4 or IPv6).

:sip:ref:`~PyQt6.QtNetwork.QSslSocket` first enters the HostLookupState. Then, after entering either the event loop or one of the waitFor...() functions, it enters the ConnectingState, emits connected(), and then initiates the SSL client handshake. At each state change, :sip:ref:`~PyQt6.QtNetwork.QSslSocket` emits signal stateChanged().

After initiating the SSL client handshake, if the identity of the peer can't be established, signal :sip:ref:`~PyQt6.QtNetwork.QSslSocket.sslErrors` is emitted. If you want to ignore the errors and continue connecting, you must call :sip:ref:`~PyQt6.QtNetwork.QSslSocket.ignoreSslErrors`, either from inside a slot function connected to the :sip:ref:`~PyQt6.QtNetwork.QSslSocket.sslErrors` signal, or prior to entering encrypted mode. If :sip:ref:`~PyQt6.QtNetwork.QSslSocket.ignoreSslErrors` is not called, the connection is dropped, signal disconnected() is emitted, and :sip:ref:`~PyQt6.QtNetwork.QSslSocket` returns to the UnconnectedState.

If the SSL handshake is successful, :sip:ref:`~PyQt6.QtNetwork.QSslSocket` emits :sip:ref:`~PyQt6.QtNetwork.QSslSocket.encrypted`.

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_ssl_qsslsocket.py
    :lines: 91-95

**Note:** The example above shows that text can be written to the socket immediately after requesting the encrypted connection, before the :sip:ref:`~PyQt6.QtNetwork.QSslSocket.encrypted` signal has been emitted. In such cases, the text is queued in the object and written to the socket *after* the connection is established and the :sip:ref:`~PyQt6.QtNetwork.QSslSocket.encrypted` signal has been emitted.

The default for *mode* is :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenMode.ReadWrite`.

If you want to create a :sip:ref:`~PyQt6.QtNetwork.QSslSocket` on the server side of a connection, you should instead call :sip:ref:`~PyQt6.QtNetwork.QSslSocket.startServerEncryption` upon receiving the incoming connection through :sip:ref:`~PyQt6.QtNetwork.QTcpServer`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.connectToHost`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.startClientEncryption`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.waitForConnected`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.waitForEncrypted`.
