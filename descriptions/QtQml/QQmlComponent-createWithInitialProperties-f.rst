.. sip:method-description::
    :status: todo
    :pysig: 670d17152399e1dc329b0182ead12c95
    :realsig: (const QVariantMap&,QQmlContext*)
    :digest: e85ef4eb8d4afd725e506e66b521d124

Create an object instance of this component, within the specified *context*, and initialize its top-level properties with *initialProperties*.

If any of the *initialProperties* cannot be set, a warning is issued. If there are unset required properties, the object creation fails and returns ``nullptr``, in which case :sip:ref:`~PyQt6.QtQml.QQmlComponent.isError` will return ``true``.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlComponent.create`.
