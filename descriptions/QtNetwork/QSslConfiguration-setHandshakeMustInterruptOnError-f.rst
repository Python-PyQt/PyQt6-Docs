.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 27bb031c204e34beac4e591aa7387110

If *interrupt* is true and the underlying backend supports this option, errors found during certificate verification are reported immediately by emitting :sip:ref:`~PyQt6.QtNetwork.QSslSocket.handshakeInterruptedOnError`. This allows to stop the unfinished handshake and send a proper alert message to a peer. No special action is required from the application in this case. :sip:ref:`~PyQt6.QtNetwork.QSslSocket` will close the connection after sending the alert message. If the application after inspecting the error wants to continue the handshake, it must call :sip:ref:`~PyQt6.QtNetwork.QSslSocket.continueInterruptedHandshake` from its slot function. The signal-slot connection must be direct.

**Note:** When interrupting handshake is enabled, errors that would otherwise be reported by :sip:ref:`~PyQt6.QtNetwork.QSslSocket.peerVerifyError` are instead only reported by :sip:ref:`~PyQt6.QtNetwork.QSslSocket.handshakeInterruptedOnError`.

**Note:** Even if the handshake was continued, these errors will be reported when emitting :sip:ref:`~PyQt6.QtNetwork.QSslSocket.sslErrors` signal (and thus must be ignored in the corresponding function slot).

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.handshakeMustInterruptOnError`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.handshakeInterruptedOnError`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.continueInterruptedHandshake`.
