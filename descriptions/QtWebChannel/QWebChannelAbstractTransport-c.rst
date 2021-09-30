.. sip:class-description::
    :status: todo
    :brief: Communication channel between the C++ QWebChannel server and a HTML/JS client
    :digest: 37aa57929b839b722e74b3bca232fb27

Communication channel between the C++ :sip:ref:`~PyQt6.QtWebChannel.QWebChannel` server and a HTML/JS client.

Users of the :sip:ref:`~PyQt6.QtWebChannel.QWebChannel` must implement this interface and connect instances of it to the :sip:ref:`~PyQt6.QtWebChannel.QWebChannel` server for every client that should be connected to the :sip:ref:`~PyQt6.QtWebChannel.QWebChannel`. The `Qt WebChannel Standalone Example <https://doc.qt.io/qt-6/qtwebchannel-standalone-example.html>`_ shows how this can be done using `Qt WebSockets <https://doc.qt.io/qt-6/qtwebsockets-index.html>`_.

**Note:** The JSON message protocol is considered internal and might change over time.

.. seealso:: `Qt WebChannel Standalone Example <https://doc.qt.io/qt-6/qtwebchannel-standalone-example.html>`_.
