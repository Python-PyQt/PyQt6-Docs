.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 378800739ad5cfbafb11269f25cfc565

Sets the host name of the remote peer to *name*.

You can call this function in a subclass of :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` to change the return value of the :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.peerName` function after a connection has been established. This feature is commonly used by proxy connections for virtual connection settings.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.peerName`.
