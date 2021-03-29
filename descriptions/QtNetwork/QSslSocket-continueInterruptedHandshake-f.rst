.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 59fe37699eb71d14188cfd95d2c7fe7e

If an application wants to conclude a handshake even after receiving :sip:ref:`~PyQt6.QtNetwork.QSslSocket.handshakeInterruptedOnError` signal, it must call this function. This call must be done from a slot function attached to the signal. The signal-slot connection must be direct.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.handshakeInterruptedOnError`, :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setHandshakeMustInterruptOnError`.
