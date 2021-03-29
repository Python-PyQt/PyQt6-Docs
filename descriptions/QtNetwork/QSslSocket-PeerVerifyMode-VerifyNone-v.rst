.. sip:enum-member-description::
    :status: todo
    :value: 0
    :digest: b7d1df8f14c94e19da65f856767178fb

:sip:ref:`~PyQt6.QtNetwork.QSslSocket` will not request a certificate from the peer. You can set this mode if you are not interested in the identity of the other side of the connection. The connection will still be encrypted, and your socket will still send its local certificate to the peer if it's requested.
