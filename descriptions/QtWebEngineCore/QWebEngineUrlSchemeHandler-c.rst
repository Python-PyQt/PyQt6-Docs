.. sip:class-description::
    :status: todo
    :brief: Base class for handling custom URL schemes
    :digest: 9f0140ae5c0dc92d5079b59247029880

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlSchemeHandler` class is a base class for handling custom URL schemes.

To implement a custom URL scheme for `QtWebEngine <https://doc.qt.io/qt-6/qtwebengine-qmlmodule.html>`_, you first have to create an instance of :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlScheme` and register it using :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlScheme.registerScheme`.

**Note:** Make sure that you create and register the scheme object *before* the :sip:ref:`~PyQt6.QtGui.QGuiApplication` or :sip:ref:`~PyQt6.QtWidgets.QApplication` object is instantiated.

Then you must create a class derived from :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlSchemeHandler`, and reimplement the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlSchemeHandler.requestStarted` method.

Finally, install the scheme handler object via :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.installUrlSchemeHandler` or :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.installUrlSchemeHandler`.

::

    class MySchemeHandler : public QWebEngineUrlSchemeHandler
    {
    public:
        MySchemeHandler(QObject *parent = nullptr);
        void requestStarted(QWebEngineUrlRequestJob *request)
        {
            // ....
        }
    };

    int main(int argc, char **argv)
    {
        QWebEngineUrlScheme scheme("myscheme");
        scheme.setSyntax(QWebEngineUrlScheme::Syntax::HostAndPort);
        scheme.setDefaultPort(2345);
        scheme.setFlags(QWebEngineUrlScheme::SecureScheme);
        QWebEngineUrlScheme::registerScheme(scheme);

        // ...
        QApplication app(argc, argv);
        // ...

        // installUrlSchemeHandler does not take ownership of the handler.
        MySchemeHandler *handler = new MySchemeHandler(parent);
        QWebEngineProfile::defaultProfile()->installUrlSchemeHandler("myscheme", handler);
    }

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlScheme`, `WebEngine Widgets WebUI Example <https://doc.qt.io/qt-6/qtwebengine-webenginewidgets-webui-example.html>`_.
