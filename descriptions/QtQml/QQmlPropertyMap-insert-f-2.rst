.. sip:method-description::
    :status: todo
    :pysig: d724b549ee2faa81b61b29cf2e8443ba
    :realsig: (const QVariantHash&)
    :digest: 44de393c45b50c50df0357285681f9c3

Inserts the *values* into the :sip:ref:`~PyQt6.QtQml.QQmlPropertyMap`.

Keys that don't exist are automatically created.

This method is substantially faster than calling ``insert(key, value)`` many times in a row.
