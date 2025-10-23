.. sip:method-description::
    :status: todo
    :pysig: cdd41ad1110e1a711b18049f29c53f10
    :realsig: (const QPixmap&)
    :digest: e97ada341442683431a44152aec6bc2c

Inserts a copy of the given *pixmap* into the cache and returns a key that can be used to retrieve it.

When a pixmap is inserted and the cache is about to exceed its limit, it removes pixmaps until there is enough room for the pixmap to be inserted.

The oldest pixmaps (least recently accessed in the cache) are deleted when more space is needed.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixmapCache.setCacheLimit`.
