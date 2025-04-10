.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: ad71fb6bb981f1642cb4d433a3b642bd

Returns the method offset for this class; i.e. the index position of this class's first member function.

The offset is the sum of all the methods in the class's superclasses (which is always positive since :sip:ref:`~PyQt6.QtCore.QObject` has the :sip:ref:`~PyQt6.QtCore.QObject.deleteLater` slot and a :sip:ref:`~PyQt6.QtCore.QObject.destroyed` signal).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaObject.method`, :sip:ref:`~PyQt6.QtCore.QMetaObject.methodCount`, :sip:ref:`~PyQt6.QtCore.QMetaObject.indexOfMethod`.
