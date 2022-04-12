.. sip:method-description::
    :status: todo
    :pysig: 7c05e57425aadef109013fc197288a18
    :realsig: (QQmlIncubator&,QQmlContext*,QQmlContext*)
    :digest: 001e56422d4f2af24266e9373c50ec8c

Create an object instance from this component using the provided *incubator*. *context* specifies the context within which to create the object instance.

If *context* is ``nullptr`` (by default), it will create the instance in the engine's :sip:ref:`~PyQt6.QtQml.QQmlEngine.rootContext`.

*forContext* specifies a context that this object creation depends upon. If the *forContext* is being created asynchronously, and the :sip:ref:`~PyQt6.QtQml.QQmlIncubator.IncubationMode` is :sip:ref:`~PyQt6.QtQml.QQmlIncubator.IncubationMode.AsynchronousIfNested`, this object will also be created asynchronously. If *forContext* is ``nullptr`` (by default), the *context* will be used for this decision.

The created object and its creation status are available via the *incubator*.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlIncubator`.
