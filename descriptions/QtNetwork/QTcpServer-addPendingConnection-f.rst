.. sip:method-description::
    :status: todo
    :pysig: fa9607d7c74348deaea2550ae89b9113
    :realsig: (QTcpSocket*)
    :digest: ee898ac2ff60c79b18079d546fc4f4ae

This function is called by :sip:ref:`~PyQt6.QtNetwork.QTcpServer.incomingConnection` to add the *socket* to the list of pending incoming connections.

**Note:** Don't forget to call this member from reimplemented :sip:ref:`~PyQt6.QtNetwork.QTcpServer.incomingConnection` if you do not want to break the Pending Connections mechanism.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QTcpServer.incomingConnection`.
