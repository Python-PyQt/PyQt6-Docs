.. sip:method-description::
    :status: todo
    :pysig: 78e5da0a8fab21e479b3dccf51e98fb8
    :realsig: (const QString&,QUrl::ComponentFormattingOptions) const
    :digest: 5b37da4a91ef790dad6217a67c18aa29

Returns the query value associated with key *key* from the URL, using the options specified in *encoding* to encode the return value. If the key *key* is not found, this function returns an empty string. If you need to distinguish between an empty value and a non-existent key, you should check for the key's presence first using :sip:ref:`~PyQt6.QtCore.QUrlQuery.hasQueryItem`.

If the key *key* is multiply defined, this function will return the first one found, in the order they were present in the query string or added using :sip:ref:`~PyQt6.QtCore.QUrlQuery.addQueryItem`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrlQuery.addQueryItem`, :sip:ref:`~PyQt6.QtCore.QUrlQuery.allQueryItemValues`, Encoding.
