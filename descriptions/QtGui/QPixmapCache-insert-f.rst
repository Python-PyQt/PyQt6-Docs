.. sip:method-description::
    :status: todo
    :pysig: cdd41ad1110e1a711b18049f29c53f10
    :realsig: (const QPixmap&)
    :digest: 9102c5b4506645128a993a01ee35f899

Inserts a copy of the given *pixmap* into the cache and returns a key that can be used to retrieve it.

When a pixmap is inserted and the cache is about to exceed its limit, it removes pixmaps until there is enough room for the pixmap to be inserted.

The oldest pixmaps (least recently accessed in the cache) are deleted when more space is needed.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixmapCache.setCacheLimit`, :sip:ref:`~PyQt6.QtGui.QPixmapCache.replace`.
