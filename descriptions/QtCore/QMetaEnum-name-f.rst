.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 08fdd730ea736736d0e656e080948c84

Returns the name of the type (without the scope).

For example, the :sip:ref:`~PyQt6.QtCore.Qt.Key` enumeration has ``Key`` as the type name and :sip:ref:`~PyQt6.QtCore.Qt` as the scope.

For flags this returns the name of the flag type, not the name of the enum type.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaEnum.isValid`, :sip:ref:`~PyQt6.QtCore.QMetaEnum.scope`, :sip:ref:`~PyQt6.QtCore.QMetaEnum.enumName`.
