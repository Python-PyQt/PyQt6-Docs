.. sip:method-description::
    :status: todo
    :pysig: 0e67cb347663de0f2740870caac2926b
    :realsig: (int) const
    :digest: 6eb4e12f2084f35340a47b28c43fe4e7

Returns the metatype of the parameter at the given *index*.

If the *index* is smaller than zero or larger than :sip:ref:`~PyQt6.QtCore.QMetaMethod.parameterCount`, an invalid `QMetaType <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qmetatype>`_ is returned.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaMethod.parameterCount`, :sip:ref:`~PyQt6.QtCore.QMetaMethod.returnMetaType`, `QMetaType <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qmetatype>`_.
