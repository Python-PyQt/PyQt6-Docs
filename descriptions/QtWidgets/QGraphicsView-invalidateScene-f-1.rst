.. sip:method-description::
    :status: todo
    :pysig: 8bc92587ab84c17c78203460ff2a623e
    :realsig: (const QRectF&,QGraphicsScene::SceneLayers)
    :digest: 1f7c79533ef3c109bc68713787bada90

Invalidates and schedules a redraw of *layers* inside *rect*. *rect* is in scene coordinates. Any cached content for *layers* inside *rect* is unconditionally invalidated and redrawn.

You can call this function to notify :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` of changes to the background or the foreground of the scene. It is commonly used for scenes with tile-based backgrounds to notify changes when :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` has enabled background caching.

Note that :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` currently supports background caching only (see :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.CacheMode.CacheBackground`). This function is equivalent to calling update() if any layer but :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.SceneLayer.BackgroundLayer` is passed.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.invalidate`, update().
