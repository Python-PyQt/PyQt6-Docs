.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: b19aed5c5257fb256c3df19d1e78ee3e

Returns a number that identifies the contents of this :sip:ref:`~PyQt6.QtGui.QIcon` object. Distinct :sip:ref:`~PyQt6.QtGui.QIcon` objects can have the same key if they refer to the same contents.

The  will change when the icon is altered via :sip:ref:`~PyQt6.QtGui.QIcon.addPixmap` or :sip:ref:`~PyQt6.QtGui.QIcon.addFile`.

Cache keys are mostly useful in conjunction with caching.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixmap.cacheKey`.
