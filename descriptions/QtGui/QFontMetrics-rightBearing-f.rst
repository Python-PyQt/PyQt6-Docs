.. sip:method-description::
    :status: todo
    :pysig: 0f9b0ea7a3407ca50e1df7b110b9ad1f
    :realsig: (QChar) const
    :digest: 9786263cccafe95a84c1998d10b4a5e2

Returns the right bearing of character *ch* in the font.

The right bearing is the left-ward distance of the right-most pixel of the character from the logical origin of a subsequent character. This value is negative if the pixels of the character extend to the right of the :sip:ref:`~PyQt6.QtGui.QFontMetrics.horizontalAdvance` of the character.

See :sip:ref:`~PyQt6.QtGui.QFontMetrics.horizontalAdvance` for a graphical description of this metric.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontMetrics.leftBearing`, :sip:ref:`~PyQt6.QtGui.QFontMetrics.minRightBearing`, :sip:ref:`~PyQt6.QtGui.QFontMetrics.horizontalAdvance`.
