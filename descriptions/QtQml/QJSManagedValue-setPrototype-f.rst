.. sip:method-description::
    :status: todo
    :pysig: d44cb0f49a4e63d6c278c57e8fd27771
    :realsig: (const QJSManagedValue&)
    :digest: 52b4e8cd22e19ba104a5eca3100fef3f

Sets the prototype of this :sip:ref:`~PyQt6.QtQml.QJSManagedValue` to *prototype*. A precondition is that *prototype* belongs to the same :sip:ref:`~PyQt6.QtQml.QJSEngine` as this :sip:ref:`~PyQt6.QtQml.QJSManagedValue` and is an object (including null). Furthermore, this :sip:ref:`~PyQt6.QtQml.QJSManagedValue` has to be an object (excluding null), too, and you cannot create prototype cycles.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSManagedValue.prototype`.
