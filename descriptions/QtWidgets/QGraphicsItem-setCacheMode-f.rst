.. sip:method-description::
    :status: todo
    :pysig: 52265df8e4dfb07e8610cf58286c08bd
    :realsig: (QGraphicsItem::CacheMode,const QSize&)
    :digest: fd6d6236267852b7e412045757c69df9

Sets the item's cache mode to *mode*.

The optional *logicalCacheSize* argument is used only by :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.CacheMode.ItemCoordinateCache` mode, and describes the resolution of the cache buffer; if *logicalCacheSize* is (100, 100), :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` will fit the item into 100x100 pixels in graphics memory, regardless of the logical size of the item itself. By default :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` uses the size of :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.boundingRect`. For all other cache modes than :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.CacheMode.ItemCoordinateCache`, *logicalCacheSize* is ignored.

Caching can speed up rendering if your item spends a significant time redrawing itself. In some cases the cache can also slow down rendering, in particular when the item spends less time redrawing than :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` spends redrawing from the cache.

When caching is enabled, an item's :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.paint` function will generally draw into an offscreen pixmap cache; for any subsequent repaint requests, the Graphics View framework will redraw from the cache. This approach works particularly well with QGLWidget, which stores all the cache as OpenGL textures.

Be aware that :sip:ref:`~PyQt6.QtGui.QPixmapCache`'s cache limit may need to be changed to obtain optimal performance.

You can read more about the different cache modes in the :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.CacheMode.CacheMode` documentation.

**Note:** Enabling caching does not imply that the item's :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.paint` function will be called only in response to an explicit :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.update` call. For instance, under memory pressure, Qt may decide to drop some of the cache information; in such cases an item's :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.paint` function will be called even if there was no :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.update` call (that is, exactly as if there were no caching enabled).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.cacheMode`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.CacheMode.CacheMode`, :sip:ref:`~PyQt6.QtGui.QPixmapCache.setCacheLimit`.
