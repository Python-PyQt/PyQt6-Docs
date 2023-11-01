.. sip:method-description::
    :status: todo
    :pysig: 9cd6972fde316dd596f6d3e861be7e78
    :realsig: (const QPixmapCache::Key&,const QPixmap&)
    :digest: 7d4e7698b4811494081f7ebe2746cea1

Use ``remove(key); key = insert(pixmap);`` instead.

Replaces the pixmap associated with the given *key* with the *pixmap* specified. Returns ``true`` if the *pixmap* has been correctly inserted into the cache; otherwise returns ``false``.

The passed *key* is updated to reference *pixmap* now. Other copies of *key*, if any, still refer to the old pixmap, which is, however, removed from the cache by this function.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixmapCache.setCacheLimit`, :sip:ref:`~PyQt6.QtGui.QPixmapCache.insert`.
