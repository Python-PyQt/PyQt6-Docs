.. sip:method-description::
    :status: todo
    :pysig: bc959c75ea51266df2de3e2c83cd104e
    :realsig: (const QObject*) const
    :digest: fc1dfce83f38a4205ed892755440dbf4

Returns the name of *object* in this context, or an empty string if *object* is not named in the context. Objects are named by :sip:ref:`~PyQt6.QtQml.QQmlContext.setContextProperty`, or as properties of a context object, or by ids in the case of QML created contexts.

If the object has multiple names, the first is returned.

In contrast to :sip:ref:`~PyQt6.QtQml.QQmlContext.contextProperty`, this method does not traverse the context hierarchy. If the name is not found in the current context, an empty String is returned.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlContext.contextProperty`, :sip:ref:`~PyQt6.QtQml.QQmlContext.objectForName`.
