.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: eb56a0765582690616eabaf1d7e2fdc8

Returns ``false`` if the ``Q_PROPERTY()``'s ``USER`` attribute is false. Otherwise it returns true, indicating the property is designated as the ``USER`` property, i.e., the one that the user can edit or that is significant in some other way.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaObject.userProperty`, :sip:ref:`~PyQt6.QtCore.QMetaProperty.isDesignable`, :sip:ref:`~PyQt6.QtCore.QMetaProperty.isScriptable`.
