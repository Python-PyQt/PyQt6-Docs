.. sip:method-description::
    :status: todo
    :pysig: 2b9057d9b4a06375acf76e6922f506e2
    :realsig: (QObject*)
    :digest: ad18e0f1fe9601ca8d82fc56f4879aac

Called after the *object* is first created, but before complex property bindings are evaluated and, if applicable, :sip:ref:`~PyQt6.QtQml.QQmlParserStatus.componentComplete` is called. This is equivalent to the point between :sip:ref:`~PyQt6.QtQml.QQmlComponent.beginCreate` and :sip:ref:`~PyQt6.QtQml.QQmlComponent.completeCreate`, and can be used to assign initial values to the object's properties.

The default implementation does nothing.

**Note:** Simple bindings such as numeric literals are evaluated before setInitialState() is called. The categorization of bindings into simple and complex ones is intentionally unspecified and may change between versions of Qt and depending on whether and how you are using `qmlcachegen <https://doc.qt.io/qt-6/qtqml-tool-qmlcachegen.html>`_. You should not rely on any particular binding to be evaluated either before or after setInitialState() is called. For example, a constant expression like *MyType.EnumValue* may be recognized as such at compile time or deferred to be executed as binding. The same holds for constant expressions like *-(5)* or *"a" + " constant string"*.
