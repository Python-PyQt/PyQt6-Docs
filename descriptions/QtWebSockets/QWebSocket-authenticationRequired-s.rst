.. sip:signal-description::
    :status: todo
    :pysig: 8cd4daad3ddb558978fd4296b3ce2dfa
    :realsig: (QAuthenticator*)
    :digest: 20bfc97f2943b6661e592ce4338e39ad

This signal is emitted when the server requires authentication. The *authenticator* object must then be filled in with the required details to allow authentication and continue the connection.

If you know that the server may require authentication, you can set the username and password on the initial :sip:ref:`~PyQt6.QtCore.QUrl`, using :sip:ref:`~PyQt6.QtCore.QUrl.setUserName` and :sip:ref:`~PyQt6.QtCore.QUrl.setPassword`. :sip:ref:`~PyQt6.QtWebSockets.QWebSocket` will still try to connect *once* without using the provided credentials.

**Note:** It is not possible to use a QueuedConnection to connect to this signal, as the connection will fail if the authenticator has not been filled in with new information when the signal returns.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAuthenticator`.
