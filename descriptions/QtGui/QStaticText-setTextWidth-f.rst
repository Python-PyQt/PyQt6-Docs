.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: (qreal)
    :digest: 06b57a71293982b5827c694e268b72dd

Sets the preferred width for this :sip:ref:`~PyQt6.QtGui.QStaticText`. If the text is wider than the specified width, it will be broken into multiple lines and grow vertically. If the text cannot be split into multiple lines, it will be larger than the specified *textWidth*.

Setting the preferred text width to a negative number will cause the text to be unbounded.

Use :sip:ref:`~PyQt6.QtGui.QStaticText.size` to get the actual size of the text.

**Note:** This function will cause the layout of the text to require recalculation.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QStaticText.textWidth`, :sip:ref:`~PyQt6.QtGui.QStaticText.size`.
