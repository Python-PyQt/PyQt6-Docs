.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 1455e7a43a113ef038f8db07f27c3f5e

If *enabled* is true, client :sip:ref:`~PyQt6.QtNetwork.QSslSocket` will send a certificate status request to its peer when initiating a handshake. During the handshake :sip:ref:`~PyQt6.QtNetwork.QSslSocket` will verify the server's response. This value must be set before the handshake starts.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslConfiguration.ocspStaplingEnabled`.
