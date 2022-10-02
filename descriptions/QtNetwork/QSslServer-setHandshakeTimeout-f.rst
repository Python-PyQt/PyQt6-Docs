.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: bd7351fec4aad32736384e89e5e0bade

Sets the *timeout* to use for all incoming handshakes, in milliseconds.

This is relevant in the scenario where a client, whether malicious or accidental, connects to the server but makes no attempt at communicating or initiating a handshake. :sip:ref:`~PyQt6.QtNetwork.QSslServer` will then automatically end the connection after *timeout* milliseconds have elapsed.

By default the timeout is 5000 milliseconds (5 seconds).

**Note:** The underlying TLS framework may have their own timeout logic now or in the future, this function does not affect that.

**Note:** The *timeout* passed to this function will only apply to *new* connections. If a client is already connected it will use the timeout which was set when it connected.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslServer.handshakeTimeout`.
