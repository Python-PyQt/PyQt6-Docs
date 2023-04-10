.. sip:method-description::
    :status: todo
    :pysig: 9216a948f4eab999f76922f164bb49ab
    :realsig: (const QList<QQmlContext::PropertyPair>&)
    :digest: 548e01e378c1fec563a1cb8cfe088399

Set a batch of *properties* on this context.

Setting all properties in one batch avoids unnecessary refreshing expressions, and is therefore recommended instead of calling :sip:ref:`~PyQt6.QtQml.QQmlContext.setContextProperty` for each individual property.

**Note:** You should not use context properties to inject values into your QML components. Use singletons or regular object properties instead.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlContext.setContextProperty`.
