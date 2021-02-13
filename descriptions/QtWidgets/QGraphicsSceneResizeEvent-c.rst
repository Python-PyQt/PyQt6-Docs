.. sip:class-description::
    :status: todo
    :brief: Events for widget resizing in the graphics view framework
    :digest: d7878bcae05b499caec61071f1032152

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneResizeEvent` class provides events for widget resizing in the graphics view framework.

A `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_ sends itself a :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneResizeEvent` immediately when its geometry changes.

It's similar to :sip:ref:`~PyQt6.QtGui.QResizeEvent`, but its sizes, :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneResizeEvent.oldSize` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneResizeEvent.newSize`, use :sip:ref:`~PyQt6.QtCore.QSizeF` instead of :sip:ref:`~PyQt6.QtCore.QSize`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.setGeometry`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.resize`.
