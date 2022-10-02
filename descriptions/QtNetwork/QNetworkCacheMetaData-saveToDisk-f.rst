.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 910334289b168de5f9a30b30a049ece2

Returns is this cache should be allowed to be stored on disk.

Some cache implementations can keep these cache items in memory for performance reasons, but for security reasons they should not be written to disk.

Specifically with http, documents with Cache-control set to no-store or any https document that doesn't have "Cache-control: public" set will set the saveToDisk to false.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkCacheMetaData.setSaveToDisk`.
