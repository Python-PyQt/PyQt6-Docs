.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 66e454038fc94fa2fccce16e88642304

Continues data transfer on the socket. This method should only be used after the socket has been set to pause upon notifications and a notification has been received. The only notification currently supported is :sip:ref:`~PyQt6.QtNetwork.QSslSocket.sslErrors`. Calling this method if the socket is not paused results in undefined behavior.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.pauseMode`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.setPauseMode`.
