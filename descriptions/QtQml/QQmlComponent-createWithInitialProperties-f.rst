.. sip:method-description::
    :status: todo
    :pysig: 670d17152399e1dc329b0182ead12c95
    :realsig: (const QVariantMap&,QQmlContext*)
    :digest: 6c850e93493b8c89f9b481d5df78590c

Create an object instance of this component, and initialize its toplevel properties with *initialProperties*. *context* specifies the context where the object instance is to be created.

If any of the ``initialProperties`` cannot be set, :sip:ref:`~PyQt6.QtQml.QQmlComponent.isError` will return ``true``, and the :sip:ref:`~PyQt6.QtQml.QQmlComponent.errors` function can be used to get detailed information about the error(s).

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlComponent.create`.
