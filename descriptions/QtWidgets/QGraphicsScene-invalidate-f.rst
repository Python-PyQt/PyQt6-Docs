.. sip:method-description::
    :status: todo
    :pysig: 45ef749e074bbf5953f6edbf12bf2654
    :realsig: (const QRectF&,QGraphicsScene::SceneLayers)
    :digest: 67a9f6a11df4d793d442b7dead1988ea

Invalidates and schedules a redraw of the *layers* in *rect* on the scene. Any cached content in *layers* is unconditionally invalidated and redrawn.

You can use this function overload to notify :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene` of changes to the background or the foreground of the scene. This function is commonly used for scenes with tile-based backgrounds to notify changes when :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` has enabled :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.CacheMode.CacheBackground`.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsscene.py
    :lines: 108-133

Note that :sip:ref:`~PyQt6.QtWidgets.QGraphicsView` currently supports background caching only (see :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.CacheMode.CacheBackground`). This function is equivalent to calling :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.update` if any layer but :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.SceneLayers.BackgroundLayer` is passed.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.resetCachedContent`.
