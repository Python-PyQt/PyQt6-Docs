.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 1759425eb0c1a552953acfab516850db

Returns the property offset for this class; i.e. the index position of this class's first property.

The offset is the sum of all the properties in the class's superclasses (which is always positive since :sip:ref:`~PyQt6.QtCore.QObject` has the name() property).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaObject.property`, :sip:ref:`~PyQt6.QtCore.QMetaObject.propertyCount`, :sip:ref:`~PyQt6.QtCore.QMetaObject.indexOfProperty`.
