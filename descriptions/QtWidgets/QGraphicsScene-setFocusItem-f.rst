.. sip:method-description::
    :status: todo
    :pysig: 579b1ff290dba20a686b0721051cfd5f
    :realsig: (QGraphicsItem*,Qt::FocusReason)
    :digest: 775f8d4357850c242a2f5d11159977f9

Sets the scene's focus item to *item*, with the focus reason *focusReason*, after removing focus from any previous item that may have had focus.

If *item* is ``nullptr``, or if it either does not accept focus (i.e., it does not have the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.GraphicsItemFlags.ItemIsFocusable` flag enabled), or is not visible or not enabled, this function only removes focus from any previous focusitem.

If item is not ``nullptr``, and the scene does not currently have focus (i.e., :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.hasFocus` returns ``false``), this function will call :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.setFocus` automatically.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.focusItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.hasFocus`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.setFocus`.
