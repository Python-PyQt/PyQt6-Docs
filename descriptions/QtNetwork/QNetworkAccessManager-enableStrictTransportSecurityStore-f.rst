.. sip:method-description::
    :status: todo
    :pysig: f2772e207b8e2b93e7333f5c0dabf816
    :realsig: (bool,const QString&)
    :digest: 270e121712682abe5461164cbf5f0a7a

If *enabled* is ``true``, the internal HSTS cache will use a persistent store to read and write HSTS policies. *storeDir* defines where this store will be located. The default location is defined by :sip:ref:`~PyQt6.QtCore.QStandardPaths.StandardLocation.CacheLocation`. If there is no writable QStandartPaths::CacheLocation and *storeDir* is an empty string, the store will be located in the program's working directory.

**Note:** If HSTS cache already contains HSTS policies by the time persistent store is enabled, these policies will be preserved in the store. In case both cache and store contain the same known hosts, policies from cache are considered to be more up-to-date (and thus will overwrite the previous values in the store). If this behavior is undesired, enable HSTS store before enabling Strict Tranport Security. By default, the persistent store of HSTS policies is disabled.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.isStrictTransportSecurityStoreEnabled`, :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.setStrictTransportSecurityEnabled`, :sip:ref:`~PyQt6.QtCore.QStandardPaths.standardLocations`.
