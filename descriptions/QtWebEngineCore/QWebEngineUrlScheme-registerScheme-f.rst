.. sip:method-description::
    :status: todo
    :pysig: b0739667581db374fa5d330de7424ac4
    :realsig: (const QWebEngineUrlScheme&)
    :digest: 816fd9b9b920392a6cc1f3e89e48a774

Registers *scheme* with the web engine's URL parser and security model.

It is recommended that all custom URL schemes are first registered with this function at application startup, even if the default options are to be used.

**Warning:** This function must be called early at application startup, before creating any `WebEngine <https://doc.qt.io/qt-6/qml-qtwebengine-webengine.html>`_ classes. Late calls will be ignored.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlScheme.schemeByName`.
