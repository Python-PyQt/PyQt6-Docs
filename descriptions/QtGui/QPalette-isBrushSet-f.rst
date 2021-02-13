.. sip:method-description::
    :status: todo
    :pysig: d99b156b48ae99ca075a0385440c5f34
    :realsig: (QPalette::ColorGroup,QPalette::ColorRole) const
    :digest: 6d94dc2f5420dd427a1d4bf003501ec7

Returns ``true`` if the :sip:ref:`~PyQt6.QtGui.QPalette.ColorGroup.ColorGroup` *cg* and :sip:ref:`~PyQt6.QtGui.QPalette.ColorRole.ColorRole` *cr* has been set previously on this palette; otherwise returns ``false``.

The :sip:ref:`~PyQt6.QtGui.QPalette.ColorGroup.ColorGroup` *cg* should be less than :sip:ref:`~PyQt6.QtGui.QPalette.ColorGroup.NColorGroups`, but you can use :sip:ref:`~PyQt6.QtGui.QPalette.ColorGroup.Current`. In this case, the previously set current color group will be used.

The :sip:ref:`~PyQt6.QtGui.QPalette.ColorRole.ColorRole` *cr* should be less than :sip:ref:`~PyQt6.QtGui.QPalette.ColorRole.NColorRoles`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPalette.setBrush`, :sip:ref:`~PyQt6.QtGui.QPalette.currentColorGroup`.
