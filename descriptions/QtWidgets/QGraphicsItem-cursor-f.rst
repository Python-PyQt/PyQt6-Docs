.. sip:method-description::
    :status: todo
    :pysig: 09e612eb66bcc1ae6053c82846817e48
    :realsig: () const
    :digest: 63e9b047cb5c98b9dff09bc8272e0d11

Returns the current cursor shape for the item. The mouse cursor will assume this shape when it's over this item. See the :sip:ref:`~PyQt6.QtCore.Qt.CursorShape` for a range of useful shapes.

An editor item might want to use an I-beam cursor:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsitem.py
    :lines: 90-90

If no cursor has been set, the cursor of the item beneath is used.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setCursor`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.hasCursor`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.unsetCursor`, :sip:ref:`~PyQt6.QtWidgets.QWidget.cursor`, QApplication::overrideCursor().
