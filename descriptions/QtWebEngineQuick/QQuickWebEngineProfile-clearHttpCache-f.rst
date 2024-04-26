.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 3cd9b22b43bf5bf197e41f38e1628e4b

Removes the profile's cache entries.

**Note:** Make sure that you do not start new navigation or any operation on the profile while the clear operation is in progress. The clearHttpCacheCompleted() signal notifies about the completion.

.. seealso:: WebEngineProfile::clearHttpCache(), clearHttpCacheCompleted().
