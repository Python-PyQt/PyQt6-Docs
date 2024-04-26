.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 2221706fedbcb6a65e80df3ad1ec96b3

Removes the profile's cache entries.

**Note:** Make sure that you do not start new navigation or any operation on the profile while the clear operation is in progress. The clearHttpCacheCompleted() signal notifies about the completion.

.. seealso:: QWebEngineProfile::clearHttpCacheCompleted().
