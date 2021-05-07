.. sip:method-description::
    :status: todo
    :pysig: 469d384ac9f2f4cf93090d7b7441468e
    :realsig: (Qt::TextInteractionFlags)
    :digest: 78af760269259e3db8d032610666b0fd

Sets the flags *flags* to specify how the text item should react to user input.

The default for a :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem` is :sip:ref:`~PyQt6.QtCore.Qt.TextInteractionFlag.NoTextInteraction`. This function also affects the ItemIsFocusable :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` flag by setting it if *flags* is different from :sip:ref:`~PyQt6.QtCore.Qt.TextInteractionFlag.NoTextInteraction` and clearing it otherwise.

By default, the text is read-only. To transform the item into an editor, set the :sip:ref:`~PyQt6.QtCore.Qt.TextInteractionFlag.TextEditable` flag.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem.textInteractionFlags`.
