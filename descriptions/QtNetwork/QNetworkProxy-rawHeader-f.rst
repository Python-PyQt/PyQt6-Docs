.. sip:method-description::
    :status: todo
    :pysig: edfc6ad7e4c99d0040585a75d6eaae73
    :realsig: (const QByteArray&) const
    :digest: e40264a20ad0ff1d833152654ecf99e9

Returns the raw form of header *headerName*. If no such header is present or the proxy is not of type :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.ProxyType.HttpProxy` or :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.ProxyType.HttpCachingProxy`, an empty :sip:ref:`~PyQt6.QtCore.QByteArray` is returned, which may be indistinguishable from a header that is present but has no content (use :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.hasRawHeader` to find out if the header exists or not).

Raw headers can be set with :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.setRawHeader` or with :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.setHeader`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.header`, :sip:ref:`~PyQt6.QtNetwork.QNetworkProxy.setRawHeader`.
