.. sip:class-description::
    :status: todo
    :brief: Widget for displaying the contents of a QGraphicsScene
    :digest: a363f7d584057705c2389d6a1ff6264c

The :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` class provides a widget for displaying the contents of a :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene`.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsView` visualizes the contents of a :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` in a scrollable viewport. To create a scene with geometrical items, see :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene`'s documentation. :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` is part of the `Graphics View Framework <https://doc.qt.io/qt-6/graphicsview.html>`_.

To visualize a scene, you start by constructing a :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` object, passing the address of the scene you want to visualize to :sip:ref:`~PyQt6.QtWidgets.QGraphicsView`'s constructor. Alternatively, you can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.setScene` to set the scene at a later point. After you call show(), the view will by default scroll to the center of the scene and display any items that are visible at this point. For example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsview.py
    :lines: 54-58

You can explicitly scroll to any position on the scene by using the scroll bars, or by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.centerOn`. By passing a point to :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.centerOn`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` will scroll its viewport to ensure that the point is centered in the view. An overload is provided for scrolling to a :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`, in which case :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` will see to that the center of the item is centered in the view. If all you want is to ensure that a certain area is visible, (but not necessarily centered,) you can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.ensureVisible` instead.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsView` can be used to visualize a whole scene, or only parts of it. The visualized area is by default detected automatically when the view is displayed for the first time (by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.itemsBoundingRect`). To set the visualized area rectangle yourself, you can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.setSceneRect`. This will adjust the scroll bars' ranges appropriately. Note that although the scene supports a virtually unlimited size, the range of the scroll bars will never exceed the range of an integer (INT_MIN, INT_MAX).

:sip:ref:`~PyQt6.QtWidgets.QGraphicsView` visualizes the scene by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.render`. By default, the items are drawn onto the viewport by using a regular :sip:ref:`~PyQt6.QtGui.QPainter`, and using default render hints. To change the default render hints that :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` passes to :sip:ref:`~PyQt6.QtGui.QPainter` when painting items, you can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.setRenderHints`.

By default, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` provides a regular :sip:ref:`~PyQt6.QtWidgets.QWidget` for the viewport widget. You can access this widget by calling viewport(), or you can replace it by calling setViewport(). To render using OpenGL, simply call setViewport(new :sip:ref:`~PyQt6.QtOpenGLWidgets.QOpenGLWidget`). :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` takes ownership of the viewport widget.

:sip:ref:`~PyQt6.QtWidgets.QGraphicsView` supports affine transformations, using :sip:ref:`~PyQt6.QtGui.QTransform`. You can either pass a matrix to :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.setTransform`, or you can call one of the convenience functions :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.rotate`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.scale`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.translate` or :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.shear`. The most two common transformations are scaling, which is used to implement zooming, and rotation. :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` keeps the center of the view fixed during a transformation. Because of the scene alignment (setAligment()), translating the view will have no visual impact.

You can interact with the items on the scene by using the mouse and keyboard. :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` translates the mouse and key events into *scene* events, (events that inherit :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneEvent`,), and forward them to the visualized scene. In the end, it's the individual item that handles the events and reacts to them. For example, if you click on a selectable item, the item will typically let the scene know that it has been selected, and it will also redraw itself to display a selection rectangle. Similiary, if you click and drag the mouse to move a movable item, it's the item that handles the mouse moves and moves itself. Item interaction is enabled by default, and you can toggle it by calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.setInteractive`.

You can also provide your own custom scene interaction, by creating a subclass of :sip:ref:`~PyQt6.QtWidgets.QGraphicsView`, and reimplementing the mouse and key event handlers. To simplify how you programmatically interact with items in the view, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` provides the mapping functions :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.mapToScene` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.mapFromScene`, and the item accessors :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.items` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.itemAt`. These functions allow you to map points, rectangles, polygons and paths between view coordinates and scene coordinates, and to find items on the scene using view coordinates.

.. image:: ../../../images/graphicsview-view.png

**Note:** Using an OpenGL viewport limits the ability to use :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget`. Not all combinations of widgets and styles can be supported with such a setup. You should carefully test your UI and make the necessary adjustments.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneEvent`.
