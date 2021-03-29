.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 4c9b701b56c37de1599adc40eff0212b

Returns the method offset for this class; i.e. the index position of this class's first member function.

The offset is the sum of all the methods in the class's superclasses (which is always positive since :sip:ref:`~PyQt6.QtCore.QObject` has the deleteLater() slot and a destroyed() signal).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaObject.method`, :sip:ref:`~PyQt6.QtCore.QMetaObject.methodCount`, :sip:ref:`~PyQt6.QtCore.QMetaObject.indexOfMethod`.
