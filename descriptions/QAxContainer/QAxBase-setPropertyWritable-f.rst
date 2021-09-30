.. sip:method-description::
    :status: todo
    :pysig: 9d2496c01394f04863ec354dfad3b4be
    :realsig: (const char*,bool)
    :digest: 4e140400401d4d3ccbb85e71271401c7

Sets the property *prop* to writable if *ok* is true, otherwise sets *prop* to be read-only. By default, all properties are writable.

**Warning:** Depending on the control implementation this setting might be ignored for some properties.

.. seealso:: :sip:ref:`~PyQt6.QAxContainer.QAxBase.propertyWritable`, :sip:ref:`~PyQt6.QAxContainer.QAxBaseWidget.propertyChanged`, :sip:ref:`~PyQt6.QAxContainer.QAxBaseObject.propertyChanged`.
