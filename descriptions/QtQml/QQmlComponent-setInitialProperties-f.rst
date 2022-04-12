.. sip:method-description::
    :status: todo
    :pysig: 26e1e18cdb31dba61285d5a34924d3f0
    :realsig: (QObject*,const QVariantMap&)
    :digest: 97d6bcad9ffa3485f22e6c43ed8297d2

Set top-level *properties* of the *component*.

This method provides advanced control over component instance creation. In general, programmers should use :sip:ref:`~PyQt6.QtQml.QQmlComponent.createWithInitialProperties` to create a component.

Use this method after :sip:ref:`~PyQt6.QtQml.QQmlComponent.beginCreate` and before :sip:ref:`~PyQt6.QtQml.QQmlComponent.completeCreate` has been called. If a provided property does not exist, a warning is issued.
