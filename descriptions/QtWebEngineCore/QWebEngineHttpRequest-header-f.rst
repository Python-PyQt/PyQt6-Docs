.. sip:method-description::
    :status: todo
    :pysig: edfc6ad7e4c99d0040585a75d6eaae73
    :realsig: (const QByteArray&) const
    :digest: 6842d43910fcde0e446c52e46e4b7ae6

Returns the header specified by *headerName*. If no such header is present, an empty :sip:ref:`~PyQt6.QtCore.QByteArray` is returned, which may be indistinguishable from a header that is present but has no content (use :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHttpRequest.hasHeader` to find out if the header exists or not).

Headers can be set with :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHttpRequest.setHeader`.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHttpRequest.setHeader`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHttpRequest.hasHeader`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHttpRequest.unsetHeader`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHttpRequest.headers`.
