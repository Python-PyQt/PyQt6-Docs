.. sip:method-description::
    :status: todo
    :pysig: 93a40e16eb9c57e19d53172cc8afd089
    :realsig: () const
    :digest: 0e24535ca7089ed8587b7f4552df83d5

Returns a common :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` which can be used by any QML type instantiated by this engine.

If a :sip:ref:`~PyQt6.QtQml.QQmlNetworkAccessManagerFactory` has been set and a :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` has not yet been created, the :sip:ref:`~PyQt6.QtQml.QQmlNetworkAccessManagerFactory` will be used to create the :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`; otherwise the returned :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` will have no proxy or cache set.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlEngine.setNetworkAccessManagerFactory`.
