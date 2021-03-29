.. sip:method-description::
    :status: todo
    :pysig: 5585619ac7706749d93aa933194581de
    :realsig: (QUrl::ComponentFormattingOptions) const
    :digest: 7041e5ab9cba38a0f6f681ff15383761

Returns the reconstructed query string, formed from the key-value pairs currently stored in this :sip:ref:`~PyQt6.QtCore.QUrlQuery` object and separated by the query delimiters chosen for this object. The keys and values are encoded using the options given by the *encoding* parameter.

For this function, the only ambiguous delimiter is the hash ("#"), as in URLs it is used to separate the query string from the fragment that may follow.

The order of the key-value pairs in the returned string is exactly the same as in the original query.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrlQuery.setQuery`, :sip:ref:`~PyQt6.QtCore.QUrl.setQuery`, :sip:ref:`~PyQt6.QtCore.QUrl.fragment`, Encoding.
