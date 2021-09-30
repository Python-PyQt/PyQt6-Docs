.. sip:class-description::
    :status: todo
    :brief: Configures a custom URL scheme
    :digest: cb6fa14bef695f3e3704c2e543327027

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlScheme` class configures a custom URL scheme.

A web engine URL scheme describes a URL scheme from the web engine's perspective, specifying how URLs of this scheme should be parsed, and which security restrictions should be placed on resources originating from such URLs.

Custom URL schemes must be configured early at application startup, before creating any Qt WebEngine classes. In general this means the schemes need to be configured before a :sip:ref:`~PyQt6.QtGui.QGuiApplication` or :sip:ref:`~PyQt6.QtWidgets.QApplication` instance is created.

Every registered scheme configuration applies globally to all profiles.

::

    int main(int argc, char **argv)
    {
        QWebEngineUrlScheme scheme("myscheme");
        scheme.setSyntax(QWebEngineUrlScheme::Syntax::HostAndPort);
        scheme.setDefaultPort(2345);
        scheme.setFlags(QWebEngineUrlScheme::SecureScheme);
        QWebEngineUrlScheme::registerScheme(scheme);
        ...
    }

To actually make use of the custom URL scheme, a :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlSchemeHandler` must be created and registered in a profile.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlSchemeHandler`.
