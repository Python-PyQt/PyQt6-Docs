.. sip:method-description::
    :status: todo
    :pysig: 364191bc772363d61cf96ad3eac70cf9
    :realsig: (const QSize&)
    :digest: 4b6b9114a2a4b9c347b68deb67fb8ad5

Sets the maximum device coordinate cache size of the item to *size*. If the item is cached using :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.CacheMode.DeviceCoordinateCache` mode, caching is bypassed if the extension of the item in device coordinates is larger than *size*.

The cache corresponds to the :sip:ref:`~PyQt6.QtGui.QPixmap` which is used to cache the results of the rendering. Use :sip:ref:`~PyQt6.QtGui.QPixmapCache.setCacheLimit` to set limitations on the whole cache and use  when setting cache size for individual items.

.. seealso:: :sip:ref:`~PyQt6.QtSvgWidgets.QGraphicsSvgItem.maximumCacheSize`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.cacheMode`.
