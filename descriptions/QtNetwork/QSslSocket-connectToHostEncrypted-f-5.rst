.. sip:method-description::
    :status: todo
    :pysig: 877899636caf8b59a82b2b923dda68dd
    :realsig: (const QString&, quint16, const QString&, QIODeviceBase::OpenMode, QAbstractSocket::NetworkLayerProtocol)
    :digest: 02ffd533396abb38770b904e0cac9d49

In addition to the original behaviour of :sip:ref:`~PyQt6.QtNetwork.QSslSocket.connectToHostEncrypted`, this overloaded method enables the usage of a different hostname (\ *sslPeerName*) for the certificate validation instead of the one used for the TCP connection (\ *hostName*).

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.connectToHostEncrypted`.
