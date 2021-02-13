.. sip:method-description::
    :status: todo
    :pysig: dc5e90087edbf3fcac7fae31bbd4083b
    :realsig: (const QRect&) const
    :digest: 707579fa357ce51a857a747e755a146d

Creates and returns a :sip:ref:`~PyQt6.QtGui.QPolygon` representation of the given *rectangle*, mapped into the coordinate system defined by this matrix.

The rectangle's coordinates are transformed using the following formulas:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qtransform.py
    :lines: 68-74

Polygons and rectangles behave slightly differently when transformed (due to integer rounding), so ``matrix.map(QPolygon(rectangle))`` is not always the same as ``matrix.mapToPolygon(rectangle)``.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTransform.mapRect`, Basic Matrix Operations.
