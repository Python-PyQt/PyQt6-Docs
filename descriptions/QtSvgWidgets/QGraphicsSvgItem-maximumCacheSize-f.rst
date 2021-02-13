.. sip:method-description::
    :status: todo
    :pysig: 364191bc772363d61cf96ad3eac70cf9
    :realsig: () const
    :digest: 351f2ede1565a40ef33ad34d0cb67162

Returns the current maximum size of the device coordinate cache for this item. If the item is cached using :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.CacheMode.DeviceCoordinateCache` mode, caching is bypassed if the extension of the item in device coordinates is larger than the maximum size.

The default maximum cache size is 1024x768. :sip:ref:`~PyQt6.QtGui.QPixmapCache.cacheLimit` gives the cumulative bounds of the whole cache, whereas  refers to a maximum cache size for this particular item.

.. seealso:: :sip:ref:`~PyQt6.QtSvgWidgets.QGraphicsSvgItem.setMaximumCacheSize`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.cacheMode`.
