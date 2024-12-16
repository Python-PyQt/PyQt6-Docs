.. sip:class-description::
    :status: todo
    :brief: Base class for handling custom URL schemes
    :digest: 88680dfe1b3c5d09273796e6caedd7fe

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlSchemeHandler` class is a base class for handling custom URL schemes.

A custom scheme handler is, broadly speaking, similar to a web application served over HTTP. However, because custom schemes are integrated directly into the web engine, they have the advantage in terms of efficiency and security: There is no need for generating and parsing HTTP messages or for transferring data over sockets, nor any way to intercept or monitor the traffic.

To implement a custom URL scheme for `QtWebEngine <https://doc.qt.io/qt-6/qtwebengine-qmlmodule.html>`_, you first have to create an instance of :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlScheme` and register it using :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlScheme.registerScheme`.

As custom schemes are integrated directly into the web engine, they do not necessarily need to follow the standard security rules which apply to ordinary web content. Depending on the chosen configuration, content served over a custom scheme may be given access to local resources, be set to ignore Content-Security-Policy rules, or conversely, be denied access to any other content entirely. If it is to be accessed by normal content, ensure cross-origin access is enabled, and if accessed from HTTPS that it is marked as secure.

**Note:** Make sure that you create and register the scheme object *before* the :sip:ref:`~PyQt6.QtGui.QGuiApplication` or :sip:ref:`~PyQt6.QtWidgets.QApplication` object is instantiated.

Then you must create a class derived from :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlSchemeHandler`, and reimplement the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlSchemeHandler.requestStarted` method.

Finally, install the scheme handler object via :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.installUrlSchemeHandler` or :sip:ref:`~PyQt6.QtWebEngineQuick.QQuickWebEngineProfile.installUrlSchemeHandler`.

::

    class MySchemeHandler : public QWebEngineUrlSchemeHandler
    {
    public:
        MySchemeHandler(QObject *parent = nullptr);
        void requestStarted(QWebEngineUrlRequestJob *job)
        {
            const QByteArray method = job->requestMethod();
            const QUrl url = job->requestUrl();

            if (isValidUrl(url)) {
                if (method == QByteArrayLiteral("GET"))
                    job->reply(QByteArrayLiteral("text/html"), makeReply(url));
                else // Unsupported method
                    job->fail(QWebEngineUrlRequestJob::RequestDenied);
            } else {
                // Invalid URL
                job->fail(QWebEngineUrlRequestJob::UrlNotFound);
            }
        }
        bool isValidUrl(const QUrl &url) const // ....
        QIODevice *makeReply(const QUrl &url) // ....
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

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlScheme`.
