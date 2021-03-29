.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 6e701531aed403c9320e2867bfe5edfb

Sets the directory where cached files will be stored to *cacheDir*

:sip:ref:`~PyQt6.QtNetwork.QNetworkDiskCache` will create this directory if it does not exists.

Prepared cache items will be stored in the new cache directory when they are inserted.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkDiskCache.cacheDirectory`, :sip:ref:`~PyQt6.QtCore.QStandardPaths.StandardLocation.CacheLocation`.
