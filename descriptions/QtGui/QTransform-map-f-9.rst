.. sip:method-description::
    :status: todo
    :pysig: 5fd70130e629f44666196fc320d4f2e1
    :realsig: (qreal,qreal,qreal*,qreal*) const
    :digest: 9b5c97adda8ed7420e0eb63ba8677a45

Maps the given coordinates *x* and *y* into the coordinate system defined by this matrix. The resulting values are put in \*\ *tx* and \*\ *ty*, respectively.

The coordinates are transformed using the following formulas:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qtransform.py
    :lines: 90-96

The point (x, y) is the original point, and (x', y') is the transformed point.

.. seealso:: Basic Matrix Operations.
