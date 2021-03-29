.. sip:method-description::
    :status: todo
    :pysig: 9f595575779d47dd5717ecd5cc95c863
    :realsig: (QQmlAbstractUrlInterceptor*)
    :digest: 085dbee1f0d5d76333a1d3950a1e47a8

Remove a *urlInterceptor* that was previously added using :sip:ref:`~PyQt6.QtQml.QQmlEngine.addUrlInterceptor`. The URL interceptors should not be modifed while the engine is loading files, or URL selection may be inconsistent.

This does not delete the interceptor, but merely removes it from the engine. You can re-use it on the same or a different engine afterwards.
