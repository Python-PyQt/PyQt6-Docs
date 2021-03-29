.. sip:class-description::
    :status: todo
    :brief: Creates QNetworkAccessManager instances for a QML engine
    :digest: 86c956ce2a2351422812b70378dcd9d1

The :sip:ref:`~PyQt6.QtQml.QQmlNetworkAccessManagerFactory` class creates :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` instances for a QML engine.

A QML engine uses :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` for all network access. By implementing a factory, it is possible to provide the QML engine with custom :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` instances with specialized caching, proxy and cookies support.

To implement a factory, subclass :sip:ref:`~PyQt6.QtQml.QQmlNetworkAccessManagerFactory` and implement the virtual :sip:ref:`~PyQt6.QtQml.QQmlNetworkAccessManagerFactory.create` method, then assign it to the relevant QML engine using :sip:ref:`~PyQt6.QtQml.QQmlEngine.setNetworkAccessManagerFactory`.

Note the QML engine may create :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` instances from multiple threads. Because of this, the implementation of the :sip:ref:`~PyQt6.QtQml.QQmlNetworkAccessManagerFactory.create` method must be reentrant. In addition, the developer should be careful if the signals of the object to be returned from :sip:ref:`~PyQt6.QtQml.QQmlNetworkAccessManagerFactory.create` are connected to the slots of an object that may be created in a different thread:

* The QML engine internally handles all requests, and cleans up any :sip:ref:`~PyQt6.QtNetwork.QNetworkReply` objects it creates. Receiving the :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.finished` signal in another thread may not provide the receiver with a valid reply object if it has already been deleted.

* Authentication details provided to :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.authenticationRequired` must be provided immediately, so this signal cannot be connected as a :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.QueuedConnection` (or as the default :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.AutoConnection` from another thread).

For more information about signals and threads, see Threads and QObjects and Signals and Slots Across Threads.

.. seealso:: `Network Access Manager Factory Example <https://doc.qt.io/qt-6/qtqml-networkaccessmanagerfactory-example.html>`_.
