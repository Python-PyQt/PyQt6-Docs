.. sip:method-description::
    :status: todo
    :pysig: bc959c75ea51266df2de3e2c83cd104e
    :realsig: (const QObject*) const
    :digest: 34a132c48c4309b98c2ea5eed4546e68

Returns the name of *object* in this context, or an empty string if *object* is not named in the context. Objects are named by :sip:ref:`~PyQt6.QtQml.QQmlContext.setContextProperty`, or by ids in the case of QML created contexts.

If the object has multiple names, the first is returned.
