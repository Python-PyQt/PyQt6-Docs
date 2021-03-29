.. sip:method-description::
    :status: todo
    :pysig: 94b5250f0963301a3ec0b6bb2b4e2713
    :realsig: (const QPointF&,const QStaticText&)
    :digest: 48db7603ba1269b2182b38f8032eaf4b

Draws the given *staticText* at the given *topLeftPosition*.

The text will be drawn using the font and the transformation set on the painter. If the font and/or transformation set on the painter are different from the ones used to initialize the layout of the :sip:ref:`~PyQt6.QtGui.QStaticText`, then the layout will have to be recalculated. Use :sip:ref:`~PyQt6.QtGui.QStaticText.prepare` to initialize *staticText* with the font and transformation with which it will later be drawn.

If *topLeftPosition* is not the same as when *staticText* was initialized, or when it was last drawn, then there will be a slight overhead when translating the text to its new position.

**Note:** If the painter's transformation is not affine, then *staticText* will be drawn using regular calls to :sip:ref:`~PyQt6.QtGui.QPainter.drawText`, losing any potential for performance improvement.

**Note:** The y-position is used as the top of the font.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QStaticText`.
