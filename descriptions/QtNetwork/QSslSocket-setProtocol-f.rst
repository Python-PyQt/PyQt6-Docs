.. sip:method-description::
    :status: todo
    :pysig: c5aa82f7af8388c4d53bec9a0b893b59
    :realsig: (QSsl::SslProtocol)
    :digest: 720cda0367c7855acf039677a1945961

Sets the socket's SSL protocol to *protocol*. This will affect the next initiated handshake; calling this function on an already-encrypted socket will not affect the socket's protocol.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.protocol`.
