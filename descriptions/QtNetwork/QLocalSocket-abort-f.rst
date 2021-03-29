.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 320990c2cb8523b4265ad5cd2a2f4c00

Aborts the current connection and resets the socket. Unlike :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.disconnectFromServer`, this function immediately closes the socket, clearing any pending data in the write buffer.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.disconnectFromServer`, :sip:ref:`~PyQt6.QtNetwork.QLocalSocket.close`.
