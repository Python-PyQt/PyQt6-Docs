.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 4850735a8b7884162ecdd9aa9e3219fa

Returns the meta-method index of the signal that called the currently executing slot, which is a member of the class returned by :sip:ref:`~PyQt6.QtCore.QObject.sender`. If called outside of a slot activated by a signal, -1 is returned.

For signals with default parameters, this function will always return the index with all parameters, regardless of which was used with connect(). For example, the signal ``destroyed(QObject \*obj = \nullptr)`` will have two different indexes (with and without the parameter), but this function will always return the index with a parameter. This does not apply when overloading signals with different parameters.

**Warning:** This function violates the object-oriented principle of modularity. However, getting access to the signal index might be useful when many signals are connected to a single slot.

**Warning:** The return value of this function is not valid when the slot is called via a :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.DirectConnection` from a thread different from this object's thread. Do not use this function in this type of scenario.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.sender`, :sip:ref:`~PyQt6.QtCore.QMetaObject.indexOfSignal`, :sip:ref:`~PyQt6.QtCore.QMetaObject.method`.
