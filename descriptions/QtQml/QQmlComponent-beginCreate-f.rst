.. sip:method-description::
    :status: todo
    :pysig: e991172c6cc0c0ddc36c3e82e4c9e036
    :realsig: (QQmlContext*)
    :digest: c8130f0e94f0717ef1e59915b8052ed9

This method provides advanced control over component instance creation. In general, programmers should use :sip:ref:`~PyQt6.QtQml.QQmlComponent.create` to create object instances.

Create an object instance from this component. Returns ``nullptr`` if creation failed. *publicContext* specifies the context within which to create the object instance.

When :sip:ref:`~PyQt6.QtQml.QQmlComponent` constructs an instance, it occurs in three steps:

#. The object hierarchy is created, and constant values are assigned.

#. Property bindings are evaluated for the first time.

#. If applicable, :sip:ref:`~PyQt6.QtQml.QQmlParserStatus.componentComplete` is called on objects.

differs from :sip:ref:`~PyQt6.QtQml.QQmlComponent.create` in that it only performs step 1. :sip:ref:`~PyQt6.QtQml.QQmlComponent.completeCreate` must be called to complete steps 2 and 3.

This breaking point is sometimes useful when using attached properties to communicate information to an instantiated component, as it allows their initial values to be configured before property bindings take effect.

The ownership of the returned object instance is transferred to the caller.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlComponent.completeCreate`, :sip:ref:`~PyQt6.QtQml.QJSEngine.ObjectOwnership.ObjectOwnership`.
