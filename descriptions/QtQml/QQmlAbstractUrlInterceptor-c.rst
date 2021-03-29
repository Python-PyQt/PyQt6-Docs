.. sip:class-description::
    :status: todo
    :brief: Allows you to control QML file loading
    :digest: f5cb5782595463124c2cb9bd10707d16

allows you to control QML file loading.

:sip:ref:`~PyQt6.QtQml.QQmlAbstractUrlInterceptor` is an interface which can be used to alter URLs before they are used by the QML engine. This is primarily useful for altering file urls into other file urls, such as selecting different graphical assets for the current platform.

Relative URLs are intercepted after being resolved against the file path of the current QML context. URL interception also occurs after setting the base path for a loaded QML file. This means that the content loaded for that QML file uses the intercepted URL, but inside the file the pre-intercepted URL is used for resolving relative paths. This allows for interception of .qml file loading without needing all paths (or local types) inside intercepted content to insert a different relative path.

Compared to setNetworkAccessManagerFactory, :sip:ref:`~PyQt6.QtQml.QQmlAbstractUrlInterceptor` affects all URLs and paths, including local files and embedded resource files. :sip:ref:`~PyQt6.QtQml.QQmlAbstractUrlInterceptor` is synchronous, and for asynchronous files must return a url with an asynchronous scheme (such as http or a custom scheme handled by your own custom :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`). You can use a :sip:ref:`~PyQt6.QtQml.QQmlAbstractUrlInterceptor` to change file URLs into networked URLs which are handled by your own custom :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`.

To implement support for a custom networked scheme, see setNetworkAccessManagerFactory.
