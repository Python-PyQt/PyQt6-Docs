.. sip:method-description::
    :status: todo
    :pysig: c0f4499fe0b73d6c2f4290628af553cf
    :realsig: (const QPoint&) const
    :digest: e14fe9bab407a814fb35fae1ef32ea74

Returns a list of all the items at the position *pos* in the view. The items are listed in descending stacking order (i.e., the first item in the list is the uppermost item, and the last item is the lowermost item). *pos* is in viewport coordinates.

This function is most commonly called from within mouse event handlers in a subclass in :sip:ref:`~PyQt6.QtWidgets.QGraphicsView`. *pos* is in untransformed viewport coordinates, just like :sip:ref:`~PyQt6.QtGui.QMouseEvent.pos`.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsview.py
    :lines: 117-121

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.items`, Sorting.
