.. sip:method-description::
    :status: todo
    :pysig: bebdbd41cdb242f6f1fac6eeca28f1f3
    :realsig: (QObject*, const QVariantMap&)
    :digest: 9edf50f5fa72d41b01be977abf14d234

Set top-level *properties* of the *object* that was created from a :sip:ref:`~PyQt6.QtQml.QQmlComponent`.

This method provides advanced control over component instance creation. In general, programmers should use :sip:ref:`~PyQt6.QtQml.QQmlComponent.createWithInitialProperties` to create an object instance from a component.

Use this method after :sip:ref:`~PyQt6.QtQml.QQmlComponent.beginCreate` and before :sip:ref:`~PyQt6.QtQml.QQmlComponent.completeCreate` has been called. If a provided property does not exist, a warning is issued.

This method does not allow setting initial nested properties directly. Instead, setting an initial value for value type properties with nested properties can be achieved by creating that value type, assigning its nested property and then passing the value type as an initial property of the object to be constructed.

For example, in order to set fond.bold, you can create a :sip:ref:`~PyQt6.QtGui.QFont`, set its weight to bold and then pass the font as an initial property.
