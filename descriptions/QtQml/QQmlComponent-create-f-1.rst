.. sip:method-description::
    :status: todo
    :pysig: 7c05e57425aadef109013fc197288a18
    :realsig: (QQmlIncubator&,QQmlContext*,QQmlContext*)
    :digest: 5da0b91c7b4f98d668a2826af87c1d2b

Create an object instance from this component using the provided *incubator*. *context* specifies the context within which to create the object instance.

If *context* is 0 (the default), it will create the instance in the engine's :sip:ref:`~PyQt6.QtQml.QQmlEngine.rootContext`.

*forContext* specifies a context that this object creation depends upon. If the *forContext* is being created asynchronously, and the :sip:ref:`~PyQt6.QtQml.QQmlIncubator.IncubationMode` is :sip:ref:`~PyQt6.QtQml.QQmlIncubator.IncubationMode.AsynchronousIfNested`, this object will also be created asynchronously. If *forContext* is 0 (the default), the *context* will be used for this decision.

The created object and its creation status are available via the *incubator*.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlIncubator`.
