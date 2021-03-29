.. sip:method-description::
    :status: todo
    :pysig: 35f2abd91a1c7c0f976e61da95cebf96
    :realsig: (QHideEvent*)
    :digest: 19eec5f174cffd986f749fa4f0ca9d34

This event handler, for :sip:ref:`~PyQt6.QtCore.QEvent.Type.Hide` events, is delivered after the widget has been hidden, for example, setVisible(false) has been called for the widget or one of its ancestors when the widget was previously shown.

You can reimplement this event handler to detect when your widget is hidden. Calling :sip:ref:`~PyQt6.QtCore.QEvent.accept` or :sip:ref:`~PyQt6.QtCore.QEvent.ignore` on *event* has no effect.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.showEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.hideEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemVisibleChange`.
