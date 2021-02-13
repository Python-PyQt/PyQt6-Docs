.. sip:class-description::
    :status: todo
    :brief: Application-wide cache for pixmaps
    :digest: 2d1ae3bd09857027413a62c42f71a729

The :sip:ref:`~PyQt6.QtGui.QPixmapCache` class provides an application-wide cache for pixmaps.

This class is a tool for optimized drawing with :sip:ref:`~PyQt6.QtGui.QPixmap`. You can use it to store temporary pixmaps that are expensive to generate without using more storage space than :sip:ref:`~PyQt6.QtGui.QPixmapCache.cacheLimit`. Use :sip:ref:`~PyQt6.QtGui.QPixmapCache.insert` to insert pixmaps, :sip:ref:`~PyQt6.QtGui.QPixmapCache.find` to find them, and :sip:ref:`~PyQt6.QtGui.QPixmapCache.clear` to empty the cache.

:sip:ref:`~PyQt6.QtGui.QPixmapCache` contains no member data, only static functions to access the global pixmap cache. It creates an internal QCache object for caching the pixmaps.

The cache associates a pixmap with a user-provided string as a key, or with a :sip:ref:`~PyQt6.QtGui.QPixmapCache.Key` that the cache generates. Using :sip:ref:`~PyQt6.QtGui.QPixmapCache.Key` for keys is faster than using strings. The string API is very convenient for complex keys but the :sip:ref:`~PyQt6.QtGui.QPixmapCache.Key` API will be very efficient and convenient for a one-to-one object-to-pixmap mapping - in this case, you can store the keys as members of an object.

If two pixmaps are inserted into the cache using equal keys then the last pixmap will replace the first pixmap in the cache. This follows the behavior of the QHash and QCache classes.

The cache becomes full when the total size of all pixmaps in the cache exceeds :sip:ref:`~PyQt6.QtGui.QPixmapCache.cacheLimit`. The initial cache limit is 10240 KB (10 MB); you can change this by calling :sip:ref:`~PyQt6.QtGui.QPixmapCache.setCacheLimit` with the required value. A pixmap takes roughly (\ *width* \* *height* \* *depth*)/8 bytes of memory.

The *Qt Quarterly* article `Optimizing with QPixmapCache <http://doc.qt.io/archives/qq/qq12-qpixmapcache.html>`_ explains how to use :sip:ref:`~PyQt6.QtGui.QPixmapCache` to speed up applications by caching the results of painting.

**Note:** :sip:ref:`~PyQt6.QtGui.QPixmapCache` is only usable from the application's main thread. Access from other threads will be ignored and return failure.

.. seealso:: QCache, :sip:ref:`~PyQt6.QtGui.QPixmap`.
