.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: a853b20fb8cc7230540ecfddc02ea424

Returns true if a verification callback will emit :sip:ref:`~PyQt6.QtNetwork.QSslSocket.handshakeInterruptedOnError` early, before concluding the handshake.

**Note:** This function always returns false for all backends but OpenSSL.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.setHandshakeMustInterruptOnError`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.handshakeInterruptedOnError`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.continueInterruptedHandshake`.
