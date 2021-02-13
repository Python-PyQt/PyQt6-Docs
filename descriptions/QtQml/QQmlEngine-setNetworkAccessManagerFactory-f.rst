.. sip:method-description::
    :status: todo
    :pysig: 9f5dd89824d6f0d40fe98df7897c6cad
    :realsig: (QQmlNetworkAccessManagerFactory*)
    :digest: bcd5584b64dc39a8de0beeed34bae76b

Sets the *factory* to use for creating :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`\ (s).

:sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` is used for all network access by QML. By implementing a factory it is possible to create custom :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` with specialized caching, proxy and cookie support.

The factory must be set before executing the engine.

**Note:** :sip:ref:`~PyQt6.QtQml.QQmlEngine` does not take ownership of the factory.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlEngine.networkAccessManagerFactory`.
