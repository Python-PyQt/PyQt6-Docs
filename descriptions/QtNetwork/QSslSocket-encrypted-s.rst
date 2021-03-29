.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 8cc4f13685f42e2949b05ecb310f23c3

This signal is emitted when :sip:ref:`~PyQt6.QtNetwork.QSslSocket` enters encrypted mode. After this signal has been emitted, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.isEncrypted` will return true, and all further transmissions on the socket will be encrypted.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QSslSocket.connectToHostEncrypted`, :sip:ref:`~PyQt6.QtNetwork.QSslSocket.isEncrypted`.
