.. sip:method-description::
    :status: todo
    :pysig: edfc6ad7e4c99d0040585a75d6eaae73
    :realsig: (const QByteArray&,const QByteArray&)
    :digest: c006bd3837e34485b9e4e730eba4136a

Sets the header *headerName* to be of value *headerValue*.

**Note:** Setting the same header twice overrides the previous setting. To accomplish the behavior of multiple HTTP headers of the same name, you should concatenate the two values, separating them with a comma (",") and set one single header.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHttpRequest.header`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHttpRequest.hasHeader`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHttpRequest.unsetHeader`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHttpRequest.headers`.
