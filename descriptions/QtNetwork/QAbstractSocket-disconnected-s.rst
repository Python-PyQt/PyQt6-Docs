.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: aa3a608f857188147ba3a3de58de3c93

This signal is emitted when the socket has been disconnected.

**Warning:** If you need to delete the sender() of this signal in a slot connected to it, use the :sip:ref:`~PyQt6.QtCore.QObject.deleteLater` function.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.connectToHost`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.disconnectFromHost`, :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.abort`.
