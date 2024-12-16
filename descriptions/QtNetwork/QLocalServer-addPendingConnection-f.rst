.. sip:method-description::
    :status: todo
    :pysig: db2018af6e33b41f2444c94fd7fdc8c7
    :realsig: (QLocalSocket*)
    :digest: eef2d8f80042781583957bfe9fa94917

This function is called by :sip:ref:`~PyQt6.QtNetwork.QLocalServer.incomingConnection` to add the *socket* to the list of pending incoming connections.

**Note:** Don't forget to call this member from reimplemented :sip:ref:`~PyQt6.QtNetwork.QLocalServer.incomingConnection` if you do not want to break the Pending Connections mechanism. This function emits the :sip:ref:`~PyQt6.QtNetwork.QLocalServer.newConnection` signal after the socket has been added.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalServer.incomingConnection`, :sip:ref:`~PyQt6.QtNetwork.QLocalServer.newConnection`.
