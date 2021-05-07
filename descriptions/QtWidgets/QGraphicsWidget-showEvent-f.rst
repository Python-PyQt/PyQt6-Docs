.. sip:method-description::
    :status: todo
    :pysig: 7905de75ba1096b008e853dc1ed418eb
    :realsig: (QShowEvent*)
    :digest: f17ab2a568c3dceed80db8a447312998

This event handler, for :sip:ref:`~PyQt6.QtCore.QEvent.Type.Show` events, is delivered before the widget has been shown, for example, setVisible(true) has been called for the widget or one of its ancestors when the widget was previously hidden.

You can reimplement this event handler to detect when your widget is shown. Calling :sip:ref:`~PyQt6.QtCore.QEvent.accept` or :sip:ref:`~PyQt6.QtCore.QEvent.ignore` on *event* has no effect.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.hideEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.showEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemChange.ItemVisibleChange`.
