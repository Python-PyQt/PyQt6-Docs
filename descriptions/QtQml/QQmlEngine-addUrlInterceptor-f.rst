.. sip:method-description::
    :status: todo
    :pysig: 9f595575779d47dd5717ecd5cc95c863
    :realsig: (QQmlAbstractUrlInterceptor*)
    :digest: 222f50f0b114e13bae0ac5c3d05c9369

Adds a *urlInterceptor* to be used when resolving URLs in QML. This also applies to URLs used for loading script files and QML types. The URL interceptors should not be modifed while the engine is loading files, or URL selection may be inconsistent. Multiple URL interceptors, when given, will be called in the order they were added for each URL.

:sip:ref:`~PyQt6.QtQml.QQmlEngine` does not take ownership of the interceptor and won't delete it.
