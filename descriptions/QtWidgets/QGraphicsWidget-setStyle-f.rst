.. sip:method-description::
    :status: todo
    :pysig: 7cce74340329521a145f04963f5c9bd7
    :realsig: (QStyle*)
    :digest: b0d7e9de93d8d77b2189240ef9b0cd75

Sets the widget's style to *style*. `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_ does *not* take ownership of *style*.

If no style is assigned, or *style* is ``nullptr``, the widget will use :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.style` (if this has been set). Otherwise the widget will use :sip:ref:`~PyQt6.QtWidgets.QApplication.style`.

This function sets the :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_SetStyle` attribute if *style* is not ``nullptr``; otherwise it clears the attribute.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.style`.
