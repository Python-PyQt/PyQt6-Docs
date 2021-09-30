.. sip:class-description::
    :status: todo
    :brief: Authenticator object for Cross Origin Requests (CORS)
    :digest: 15dde17a6db417703524c8935f57a845

The :sip:ref:`~PyQt6.QtWebSockets.QWebSocketCorsAuthenticator` class provides an authenticator object for Cross Origin Requests (CORS).

The :sip:ref:`~PyQt6.QtWebSockets.QWebSocketCorsAuthenticator` class is used in the :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.originAuthenticationRequired` signal. The class provides a way to pass back the required information to the :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer`. It provides applications with fine-grained control over which origin URLs are allowed and which aren't. By default, every origin is accepted. To get fine-grained control, an application connects the :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer.originAuthenticationRequired` signal to a slot. When the origin (\ :sip:ref:`~PyQt6.QtWebSockets.QWebSocketCorsAuthenticator.origin`) is accepted, it calls :sip:ref:`~PyQt6.QtWebSockets.QWebSocketCorsAuthenticator.setAllowed`\ (true)

**Note:** Checking on the origin does not make much sense when the server is accessed via a non-browser client, as that client can set whatever origin header it likes. In case of a browser client, the server SHOULD check the validity of the origin.

.. seealso:: `WebSocket Security Considerations <https://doc.qt.io/qt-6/https://datatracker.ietf.org/doc/html/rfc6455#section-10>`_, :sip:ref:`~PyQt6.QtWebSockets.QWebSocketServer`.
