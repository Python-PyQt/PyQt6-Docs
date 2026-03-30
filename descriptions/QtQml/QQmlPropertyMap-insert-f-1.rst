.. sip:method-description::
    :status: todo
    :pysig: 9e21ab2f0507a2b6f49f9b255e190ffb
    :realsig: (const QVariantHash&)
    :digest: 44de393c45b50c50df0357285681f9c3

Inserts the *values* into the :sip:ref:`~PyQt6.QtQml.QQmlPropertyMap`.

Keys that don't exist are automatically created.

This method is substantially faster than calling ``insert(key, value)`` many times in a row.
