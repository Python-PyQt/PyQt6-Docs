.. sip:method-description::
    :status: todo
    :pysig: 10b73e32ef579338968290bf7f39b35c
    :realsig: (const QRectF&) const
    :digest: 9f72d72a1ebae33e7a94d42701260534

Creates and returns a :sip:ref:`~PyQt6.QtCore.QRectF` object that is a copy of the given *rectangle*, mapped into the coordinate system defined by this matrix.

The rectangle's coordinates are transformed using the following formulas:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qtransform.py
    :lines: 79-85

If rotation or shearing has been specified, this function returns the *bounding* rectangle. To retrieve the exact region the given *rectangle* maps to, use the :sip:ref:`~PyQt6.QtGui.QTransform.mapToPolygon` function instead.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTransform.mapToPolygon`, Basic Matrix Operations.
