.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: ()
    :digest: b9fbae7c14487297d2148dd600e85d82

Cleans the cache so that its size is under the maximum cache size. Returns the current size of the cache.

When the current size of the cache is greater than the :sip:ref:`~PyQt6.QtNetwork.QNetworkDiskCache.maximumCacheSize` older cache files are removed until the total size is less then 90% of :sip:ref:`~PyQt6.QtNetwork.QNetworkDiskCache.maximumCacheSize` starting with the oldest ones first using the file creation date to determine how old a cache file is.

Subclasses can reimplement this function to change the order that cache files are removed taking into account information in the application knows about that :sip:ref:`~PyQt6.QtNetwork.QNetworkDiskCache` does not, for example the number of times a cache is accessed.

**Note:** :sip:ref:`~PyQt6.QtNetwork.QNetworkDiskCache.cacheSize` calls expire if the current cache size is unknown.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkDiskCache.maximumCacheSize`, :sip:ref:`~PyQt6.QtNetwork.QNetworkDiskCache.fileMetaData`.
