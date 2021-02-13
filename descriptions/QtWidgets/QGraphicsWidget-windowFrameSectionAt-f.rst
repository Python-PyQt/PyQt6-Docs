.. sip:method-description::
    :status: todo
    :pysig: 30a1f6e6fb78087f1d3bf1643809352e
    :realsig: (const QPointF&) const
    :digest: 199718c8af50834d828ac53595607c74

Returns the window frame section at position *pos*, or :sip:ref:`~PyQt6.QtCore.Qt.WindowFrameSection.NoSection` if there is no window frame section at this position.

This function is used in `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_'s base implementation for window frame interaction.

You can reimplement this function if you want to customize how a window can be interactively moved or resized. For instance, if you only want to allow a window to be resized by the bottom right corner, you can reimplement this function to return :sip:ref:`~PyQt6.QtCore.Qt.WindowFrameSection.NoSection` for all sections except :sip:ref:`~PyQt6.QtCore.Qt.WindowFrameSection.BottomRightSection`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.windowFrameEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.paintWindowFrame`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.windowFrameGeometry`.
