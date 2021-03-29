.. sip:method-description::
    :status: todo
    :pysig: 2bb72491117d97ac8360eb5775bf5bf6
    :realsig: () const
    :digest: 3133764687bcb4520b765172270a7237

Returns the current mode for the socket; either :sip:ref:`~PyQt6.QtNetwork.QSslSocket.SslMode.UnencryptedMode`, where :sip:ref:`~PyQt6.QtNetwork.QSslSocket` behaves identially to :sip:ref:`~PyQt6.QtNetwork.QTcpSocket`, or one of :sip:ref:`~PyQt6.QtNetwork.QSslSocket.SslMode.SslClientMode` or :sip:ref:`~PyQt6.QtNetwork.QSslSocket.SslMode.SslServerMode`, where the client is either negotiating or in encrypted mode.

When the mode changes, :sip:ref:`~PyQt6.QtNetwork.QSslSocket` emits :sip:ref:`~PyQt6.QtNetwork.QSslSocket.modeChanged`

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.SslMode.SslMode`.
