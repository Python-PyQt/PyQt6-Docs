.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: 6a913d6c8cb5cd472f4ec88bd022c964

:sip:ref:`~PyQt6.QtWidgets.QGraphicsView` will determine the minimal viewport region that requires a redraw, minimizing the time spent drawing by avoiding a redraw of areas that have not changed. This is :sip:ref:`~PyQt6.QtWidgets.QGraphicsView`'s default mode. Although this approach provides the best performance in general, if there are many small visible changes on the scene, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` might end up spending more time finding the minimal approach than it will spend drawing.
