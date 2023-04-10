.. sip:class-description::
    :status: todo
    :brief: Creates QNetworkAccessManager instances for a QML engine
    :digest: 06e242eed73a67d0aa999888744c9df9

The :sip:ref:`~PyQt6.QtQml.QQmlNetworkAccessManagerFactory` class creates :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` instances for a QML engine.

A QML engine uses :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` for all network access. By implementing a factory, it is possible to provide the QML engine with custom :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` instances with specialized caching, proxy and cookies support.

* The :sip:ref:`~PyQt6.QtNetwork.QNetworkDiskCache` can be used as a request cache with :sip:ref:`~PyQt6.QtNetwork.QNetworkDiskCache`.

* Using :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy`, traffic sent by the :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` can be tunnelled through a proxy.

* Cookies can be saved for future requests by adding a :sip:ref:`~PyQt6.QtNetwork.QNetworkCookieJar`.

To implement a factory, subclass :sip:ref:`~PyQt6.QtQml.QQmlNetworkAccessManagerFactory` and implement the virtual :sip:ref:`~PyQt6.QtQml.QQmlNetworkAccessManagerFactory.create` method, then assign it to the relevant QML engine using :sip:ref:`~PyQt6.QtQml.QQmlEngine.setNetworkAccessManagerFactory`. For instance, the :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` objects created by the following snippet will cache requests.

.. literalinclude:: ../../../snippets/qtdeclarative-src-qml-doc-snippets-code-src_network_access_qnetworkaccessmanager.py
    :lines: 7-20

The factory can then be passed to the QML engine so it can instantiate the :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` with the custom behavior.

.. literalinclude:: ../../../snippets/qtdeclarative-src-qml-doc-snippets-code-src_network_access_qnetworkaccessmanager.py
    :lines: 24-25

Note the QML engine may create :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` instances from multiple threads. Because of this, the implementation of the :sip:ref:`~PyQt6.QtQml.QQmlNetworkAccessManagerFactory.create` method must be reentrant. In addition, the developer should be careful if the signals of the object to be returned from :sip:ref:`~PyQt6.QtQml.QQmlNetworkAccessManagerFactory.create` are connected to the slots of an object that may be created in a different thread:

* The QML engine internally handles all requests, and cleans up any :sip:ref:`~PyQt6.QtNetwork.QNetworkReply` objects it creates. Receiving the :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.finished` signal in another thread may not provide the receiver with a valid reply object if it has already been deleted.

* Authentication details provided to :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.authenticationRequired` must be provided immediately, so this signal cannot be connected as a :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.QueuedConnection` (or as the default :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.AutoConnection` from another thread).

For more information about signals and threads, see Threads and QObjects and Signals and Slots Across Threads.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkDiskCache`, Network Access Manager Factory Example.
