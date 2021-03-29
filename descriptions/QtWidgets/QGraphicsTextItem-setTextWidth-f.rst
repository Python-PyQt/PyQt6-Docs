.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: (qreal)
    :digest: b3c4922f43c873f4e1a65f91aec94c21

Sets the preferred width for the item's text. If the actual text is wider than the specified width then it will be broken into multiple lines.

If *width* is set to -1 then the text will not be broken into multiple lines unless it is enforced through an explicit line break or a new paragraph.

The default value is -1.

Note that :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem` keeps a :sip:ref:`~PyQt6.QtGui.QTextDocument` internally, which is used to calculate the text width.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem.textWidth`, :sip:ref:`~PyQt6.QtGui.QTextDocument.setTextWidth`.
