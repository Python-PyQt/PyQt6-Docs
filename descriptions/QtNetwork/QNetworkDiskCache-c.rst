.. sip:class-description::
    :status: todo
    :brief: Very basic disk cache
    :digest: 3c6494d74f481c9853c27ed3c133e163

The :sip:ref:`~PyQt6.QtNetwork.QNetworkDiskCache` class provides a very basic disk cache.

:sip:ref:`~PyQt6.QtNetwork.QNetworkDiskCache` stores each url in its own file inside of the :sip:ref:`~PyQt6.QtNetwork.QNetworkDiskCache.cacheDirectory` using :sip:ref:`~PyQt6.QtCore.QDataStream`. Files with a text MimeType are compressed using :sip:ref:`~PyQt6.QtCore.qCompress`. Data is written to disk only in :sip:ref:`~PyQt6.QtNetwork.QNetworkDiskCache.insert` and :sip:ref:`~PyQt6.QtNetwork.QNetworkDiskCache.updateMetaData`.

Currently you cannot share the same cache files with more than one disk cache.

:sip:ref:`~PyQt6.QtNetwork.QNetworkDiskCache` by default limits the amount of space that the cache will use on the system to 50MB.

Note you have to set the cache directory before it will work.

A network disk cache can be enabled by:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_access_qnetworkdiskcache.py
    :lines: 54-57

When sending requests, to control the preference of when to use the cache and when to use the network, consider the following:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_access_qnetworkdiskcache.py
    :lines: 61-68

To check whether the response came from the cache or from the network, the following can be applied:

.. literalinclude:: ../../../snippets/qtbase-src-network-doc-snippets-code-src_network_access_qnetworkdiskcache.py
    :lines: 72-75
