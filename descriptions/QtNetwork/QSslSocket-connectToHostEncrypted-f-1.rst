.. sip:method-description::
    :status: todo
    :pysig: a3e74c431d9485ffac1943901be3d4c9
    :realsig: (const QString&, quint16, const QString&, QIODeviceBase::OpenMode, QAbstractSocket::NetworkLayerProtocol)
    :digest: 02ffd533396abb38770b904e0cac9d49

In addition to the original behaviour of :sip:ref:`~PyQt6.QtNetwork.QSslSocket.connectToHostEncrypted`, this overloaded method enables the usage of a different hostname (\ *sslPeerName*) for the certificate validation instead of the one used for the TCP connection (\ *hostName*).

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.connectToHostEncrypted`.
