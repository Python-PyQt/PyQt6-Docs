.. sip:method-description::
    :status: todo
    :pysig: 39aaf14661efa90a77ee054098b0fc5c
    :realsig: (QMetaType)
    :digest: 50e1626a459c4f3463b50939ee630f16

Casts the variant to the requested type, *targetType*. If the cast cannot be done, the variant is still changed to the requested type, but is left in a cleared null state similar to that constructed by :sip:ref:`~PyQt6.QtCore.QVariant`\ (Type).

Returns ``true`` if the current type of the variant was successfully cast; otherwise returns ``false``.

A :sip:ref:`~PyQt6.QtCore.QVariant` containing a pointer to a type derived from :sip:ref:`~PyQt6.QtCore.QObject` will also convert and return true for this function if a qobject_cast to the type described by *targetType* would succeed. Note that this only works for :sip:ref:`~PyQt6.QtCore.QObject` subclasses which use the Q_OBJECT macro.

**Note:** converting QVariants that are null due to not being initialized or having failed a previous conversion will always fail, changing the type, remaining null, and returning ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QVariant.canConvert`, :sip:ref:`~PyQt6.QtCore.QVariant.clear`.
