.. sip:method-description::
    :status: todo
    :pysig: 3d58b35510c8def711868c852c1c5630
    :realsig: () const
    :digest: d970d8f319e31bba7a63bbc55343a95f

Returns a list of all raw headers that are set in this network proxy. The list is in the order that the headers were set.

If the proxy is not of type :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.ProxyType.HttpProxy` or :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.ProxyType.HttpCachingProxy` an empty QList is returned.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.hasRawHeader`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.rawHeader`.
