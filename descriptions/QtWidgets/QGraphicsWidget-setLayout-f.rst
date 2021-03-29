.. sip:method-description::
    :status: todo
    :pysig: 530a9ddf086a80febb14626454beb57d
    :realsig: (QGraphicsLayout*)
    :digest: d2943bf1be4322f59da334e687c487ab

Sets the layout for this widget to *layout*. Any existing layout manager is deleted before the new layout is assigned. If *layout* is ``nullptr``, the widget is left without a layout. Existing subwidgets' geometries will remain unaffected.

All widgets that are currently managed by *layout* or all of its sublayouts, are automatically reparented to this item. The layout is then invalidated, and the child widget geometries are adjusted according to this item's geometry() and contentsMargins(). Children who are not explicitly managed by *layout* remain unaffected by the layout after it has been assigned to this widget.

`QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_ takes ownership of *layout*.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.layout`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsLinearLayout.addItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayout.invalidate`.
