.. sip:method-description::
    :status: todo
    :pysig: 1ec6141d850ed80f0a5d5d99858382df
    :realsig: (QAbstractSocket::PauseModes)
    :digest: 0099d21b0a8a336667b7ab23283dd7dc

Controls whether to pause upon receiving a notification. The *pauseMode* parameter specifies the conditions in which the socket should be paused. The only notification currently supported is :sip:ref:`~PyQt6.QtNetwork.QSslSocket.sslErrors`. If set to :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.PauseMode.PauseOnSslErrors`, data transfer on the socket will be paused and needs to be enabled explicitly again by calling :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.resume`. By default this option is set to :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.PauseMode.PauseNever`. This option must be called before connecting to the server, otherwise it will result in undefined behavior.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.pauseMode`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.resume`.
