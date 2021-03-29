.. sip:enum-member-description::
    :status: todo
    :value: 0x2
    :realname: QGraphicsView::OptimizationFlag::DontAdjustForAntialiasing
    :digest: b4947a7d0ed45ee8753e6a197b907a6d

Disables :sip:ref:`~PyQt6.QtWidgets.QGraphicsView`'s antialiasing auto-adjustment of exposed areas. Items that render antialiased lines on the boundaries of their :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRect` can end up rendering parts of the line outside. To prevent rendering artifacts, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` expands all exposed regions by 2 pixels in all directions. If you enable this flag, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` will no longer perform these adjustments, minimizing the areas that require redrawing, which improves performance. A common side effect is that items that do draw with antialiasing can leave painting traces behind on the scene as they are moved.
