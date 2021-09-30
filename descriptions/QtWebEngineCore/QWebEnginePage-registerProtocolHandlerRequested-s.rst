.. sip:signal-description::
    :status: todo
    :pysig: 0850b85d87f62d0710ad373d1dfb8b4f
    :realsig: (QWebEngineRegisterProtocolHandlerRequest)
    :digest: 76a3983eb64321a575545878c528aa69

This signal is emitted when the web page tries to register a custom protocol using the `registerProtocolHandler <https://doc.qt.io/qt-6/https://developer.mozilla.org/en-US/docs/Web/API/Navigator/registerProtocolHandler>`_ API.

The request object *request* can be used to accept or reject the request:

.. literalinclude:: ../../../snippets/qtwebengine-examples-webenginewidgets-simplebrowser-webview.py
    :lines: 339-350
