.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (qint64)
    :digest: 6d1facefbbec8069f656a1581af40e2d

Sets the maximum size of the disk cache to be *size*.

If the new size is smaller then the current cache size then the cache will call :sip:ref:`~PyQt6.QtNetwork.QNetworkDiskCache.expire`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkDiskCache.maximumCacheSize`.
