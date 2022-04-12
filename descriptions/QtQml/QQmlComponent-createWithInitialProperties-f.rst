.. sip:method-description::
    :status: todo
    :pysig: 670d17152399e1dc329b0182ead12c95
    :realsig: (const QVariantMap&,QQmlContext*)
    :digest: 6a15ae022849d5afe997b4898d416fd3

Create an object instance of this component, within the specified *context*, and initialize its top-level properties with *initialProperties*.

If any of the ``initialProperties`` cannot be set, :sip:ref:`~PyQt6.QtQml.QQmlComponent.isError` will return ``true``, and the :sip:ref:`~PyQt6.QtQml.QQmlComponent.errors` function can be used to get detailed information about the error(s).

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlComponent.create`.
