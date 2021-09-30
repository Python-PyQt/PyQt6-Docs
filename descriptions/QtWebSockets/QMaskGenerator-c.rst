.. sip:class-description::
    :status: todo
    :brief: Abstract base for custom 32-bit mask generators
    :digest: b641ddcd35d0c2f16f0de257e018f740

The :sip:ref:`~PyQt6.QtWebSockets.QMaskGenerator` class provides an abstract base for custom 32-bit mask generators.

The WebSockets specification as outlined in `RFC 6455 <https://doc.qt.io/qt-6/https://datatracker.ietf.org/doc/html/rfc6455>`_ requires that all communication from client to server be masked. This is to prevent malicious scripts from attacking badly behaving proxies. For more information about the importance of good masking, see `"Talking to Yourself for Fun and Profit" by Lin-Shung Huang et al <https://doc.qt.io/qt-6/http://w2spconf.com/2011/papers/websocket.pdf>`_. By default :sip:ref:`~PyQt6.QtWebSockets.QWebSocket` uses the reasonably secure :sip:ref:`~PyQt6.QtCore.QRandomGenerator.global_`->generate() function. The best measure against attacks mentioned in the document above, is to use :sip:ref:`~PyQt6.QtWebSockets.QWebSocket` over a secure connection (\ *wss://*). In general, always be careful to not have 3rd party script access to a :sip:ref:`~PyQt6.QtWebSockets.QWebSocket` in your application.
