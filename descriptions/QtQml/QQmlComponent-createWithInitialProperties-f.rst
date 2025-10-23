.. sip:method-description::
    :status: todo
    :pysig: 7d450ada1d80c34d105610605211bd4a
    :realsig: (const QVariantMap&, QQmlContext*)
    :digest: 1b644513b224274e2a2fd151c08ce01f

Create an object instance of this component, within the specified *context*, and initialize its top-level properties with *initialProperties*.

If any of the *initialProperties* cannot be set, a warning is issued. If there are unset required properties, the object creation fails and returns ``nullptr``, in which case :sip:ref:`~PyQt6.QtQml.QQmlComponent.isError` will return ``true``.

If *context* is ``nullptr`` (the default), it will create the instance in the :sip:ref:`~PyQt6.QtQml.QQmlEngine.rootContext` of the engine.

The ownership of the returned object instance is transferred to the caller.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlComponent.create`.
