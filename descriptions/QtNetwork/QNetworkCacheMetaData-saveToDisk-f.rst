.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: aac86c5b76bab0e0c682c8358287b578

Returns is this cache should be allowed to be stored on disk.

Some cache implementations can keep these cache items in memory for performance reasons, but for security reasons they should not be written to disk.

Specifically with http, documents with Cache-control set to no-store or any https document that doesn't have "Cache-control: public" set will set the  to false.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkCacheMetaData.setSaveToDisk`.
