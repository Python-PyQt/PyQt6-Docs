.. sip:class-description::
    :status: todo
    :brief: Implements a TCP socket that talks the WebSocket protocol
    :digest: 20162023d892692d832e3321ab004e4c

Implements a TCP socket that talks the WebSocket protocol.

WebSockets is a web technology providing full-duplex communications channels over a single TCP connection. The WebSocket protocol was standardized by the IETF as `RFC 6455 <https://doc.qt.io/qt-6/https://datatracker.ietf.org/doc/html/rfc6455>`_ in 2011. :sip:ref:`~PyQt6.QtWebSockets.QWebSocket` can both be used in a client application and server application.

This class was modeled after :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket`.

:sip:ref:`~PyQt6.QtWebSockets.QWebSocket` currently does not support `WebSocket Extensions <https://doc.qt.io/qt-6/https://datatracker.ietf.org/doc/html/rfc6455#section-9>`_.

:sip:ref:`~PyQt6.QtWebSockets.QWebSocket` only supports version 13 of the WebSocket protocol, as outlined in `RFC 6455 <https://doc.qt.io/qt-6/https://datatracker.ietf.org/doc/html/rfc6455>`_.

**Note:** Some proxies do not understand certain HTTP headers used during a WebSocket handshake. In that case, non-secure WebSocket connections fail. The best way to mitigate against this problem is to use WebSocket over a secure connection.

**Warning:** To generate masks, this implementation of WebSockets uses the reasonably secure :sip:ref:`~PyQt6.QtCore.QRandomGenerator.global_`->generate() function. For more information about the importance of good masking, see `"Talking to Yourself for Fun and Profit" by Lin-Shung Huang et al <https://doc.qt.io/qt-6/https://www.ieee-security.org/TC/W2SP/2011/papers/websocket.pdf>`_. The best measure against attacks mentioned in the document above, is to use :sip:ref:`~PyQt6.QtWebSockets.QWebSocket` over a secure connection (\ *wss://*). In general, always be careful to not have 3rd party script access to a :sip:ref:`~PyQt6.QtWebSockets.QWebSocket` in your application.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket`, :sip:ref:`~PyQt6.QtNetwork.QTcpSocket`, `QWebSocket client example <https://doc.qt.io/qt-6/echoclient.html>`_.
