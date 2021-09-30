.. sip:enum-description::
    :status: todo
    :digest: ce8b2d7f6d5331aa28c0bed3065352cc

This enum describes the possible options that can be used to create the socket. This changes the access permissions on platforms (Linux, Windows) that support access permissions on the socket. Both GroupAccess and OtherAccess may vary slightly in meanings depending on the platform. On Linux and Android it is possible to use sockets with abstract addresses; socket permissions have no meaning for such sockets.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalServer.socketOptions`.
