.. sip:method-description::
    :status: todo
    :pysig: 469d384ac9f2f4cf93090d7b7441468e
    :realsig: (Qt::TextInteractionFlags)
    :digest: 59e26975732c916f7b81d3025d08d3d4

Sets the flags *flags* to specify how the text item should react to user input.

The default for a :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem` is :sip:ref:`~PyQt6.QtCore.Qt.TextInteractionFlags.NoTextInteraction`. This function also affects the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemIsFocusable` :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` flag by setting it if *flags* is different from :sip:ref:`~PyQt6.QtCore.Qt.TextInteractionFlags.NoTextInteraction` and clearing it otherwise.

By default, the text is read-only. To transform the item into an editor, set the :sip:ref:`~PyQt6.QtCore.Qt.TextInteractionFlags.TextEditable` flag.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem.textInteractionFlags`.
