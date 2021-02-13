.. sip:class-description::
    :status: todo
    :brief: Pixmap item that you can add to a QGraphicsScene
    :digest: 7a4a9b99f0cedc76213c3092fd09f652

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem` class provides a pixmap item that you can add to a :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene`.

To set the item's pixmap, pass a :sip:ref:`~PyQt6.QtGui.QPixmap` to :sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem`'s constructor, or call the :sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem.setPixmap` function. The :sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem.pixmap` function returns the current pixmap.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem` uses pixmap's optional alpha mask to provide a reasonable implementation of :sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem.boundingRect`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem.shape`, and :sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem.contains`.

.. image:: ../../../images/graphicsview-pixmapitem.png

The pixmap is drawn at the item's (0, 0) coordinate, as returned by :sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem.offset`. You can change the drawing offset by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem.setOffset`.

You can set the pixmap's transformation mode by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem.setTransformationMode`. By default, :sip:ref:`~PyQt6.QtCore.Qt.TransformationMode.FastTransformation` is used, which provides fast, non-smooth scaling. :sip:ref:`~PyQt6.QtCore.Qt.TransformationMode.SmoothTransformation` enables :sip:ref:`~PyQt6.QtGui.QPainter.RenderHints.SmoothPixmapTransform` on the painter, and the quality depends on the platform and viewport. The result is usually not as good as calling QPixmap::scale() directly. Call :sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem.transformationMode` to get the current transformation mode for the item.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsPathItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsRectItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsEllipseItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsPolygonItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsLineItem`, `Graphics View Framework <https://doc.qt.io/qt-6/graphicsview.html>`_.
