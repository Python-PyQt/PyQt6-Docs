.. sip:method-description::
    :status: todo
    :pysig: fa9607d7c74348deaea2550ae89b9113
    :realsig: (QTcpSocket*)
    :digest: 079643acf79e3142a0f27db3a880ac38

This function is called by :sip:ref:`~PyQt6.QtNetwork.QTcpServer.incomingConnection` to add the *socket* to the list of pending incoming connections.

**Note:** Don't forget to call this member from reimplemented :sip:ref:`~PyQt6.QtNetwork.QTcpServer.incomingConnection` if you do not want to break the Pending Connections mechanism. This function emits the :sip:ref:`~PyQt6.QtNetwork.QTcpServer.pendingConnectionAvailable` signal after the socket has been added.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QTcpServer.incomingConnection`, :sip:ref:`~PyQt6.QtNetwork.QTcpServer.pendingConnectionAvailable`.
