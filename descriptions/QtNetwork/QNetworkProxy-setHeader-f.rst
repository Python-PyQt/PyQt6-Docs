.. sip:method-description::
    :status: todo
    :pysig: 3ffc598e8f8ea2d4abdfd08def3e377f
    :realsig: (QNetworkRequest::KnownHeaders,const QVariant&)
    :digest: c4f7334e8eca895e8c57c387315c06f1

Sets the value of the known header *header* to be *value*, overriding any previously set headers. This operation also sets the equivalent raw HTTP header.

If the proxy is not of type :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.ProxyType.HttpProxy` or :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.ProxyType.HttpCachingProxy` this has no effect.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.KnownHeaders`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.setRawHeader`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.header`.
