.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 63b950ef1bc21192f260c6add96ac795

If *b* is true, the Tab key will cause the widget to change focus; otherwise, the tab key will insert a tab into the document.

In some occasions text edits should not allow the user to input tabulators or change indentation using the Tab key, as this breaks the focus chain. The default is false.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem.tabChangesFocus`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemIsFocusable`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem.textInteractionFlags`.
