.. sip:method-description::
    :status: todo
    :pysig: b7a012bc01edc71f741933d6e6e44979
    :realsig: (QAnyStringView, QAnyStringView, QQmlComponent::CompilationMode)
    :digest: b95a2e2ba901ccd9bc75704694764dee

Load the :sip:ref:`~PyQt6.QtQml.QQmlComponent` for *typeName* in the module *uri*. If the type is implemented via a QML file, *mode* is used to load it. Types backed by C++ are always loaded synchronously.

::

    QQmlEngine engine;
    QQmlComponent component(&engine);
    component.loadFromModule("QtQuick", "Item");
    // once the component is ready
    std::unique_ptr<QObject> item(component.create());
    Q_ASSERT(item->metaObject() == &QQuickItem::staticMetaObject);

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlComponent.loadUrl`.
