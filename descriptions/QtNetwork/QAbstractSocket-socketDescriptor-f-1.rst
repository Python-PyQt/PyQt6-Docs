.. sip:method-description::
    :status: todo
    :pysig: 9daeab2db5574297592cfe242f3e4da3
    :realsig: () const
    :digest: a4fb086e13dfe43d854fcaf154788c44

Returns the native socket descriptor of the :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` object if this is available; otherwise returns -1.

If the socket is using :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`, the returned descriptor may not be usable with native socket functions.

The socket descriptor is not available when :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` is in :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.SocketState.UnconnectedState`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.setSocketDescriptor`.
