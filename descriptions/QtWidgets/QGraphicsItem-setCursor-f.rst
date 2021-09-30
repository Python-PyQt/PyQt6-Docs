.. sip:method-description::
    :status: todo
    :pysig: 8e918d8b61b1642c2f8119e8dadd3b5a
    :realsig: (const QCursor&)
    :digest: ace0c6eef8a63ad07ed435f297237e37

Sets the current cursor shape for the item to *cursor*. The mouse cursor will assume this shape when it's over this item. See the :sip:ref:`~PyQt6.QtCore.Qt.CursorShape` for a range of useful shapes.

An editor item might want to use an I-beam cursor:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsitem.py
    :lines: 95-95

If no cursor has been set, the cursor of the item beneath is used.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.cursor`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.hasCursor`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.unsetCursor`, :sip:ref:`~PyQt6.QtWidgets.QWidget.cursor`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.overrideCursor`.
