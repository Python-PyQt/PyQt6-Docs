.. sip:method-description::
    :status: todo
    :pysig: 923e0110d456497492881cbc710b5575
    :realsig: (const QString&, QUrl::ComponentFormattingOptions) const
    :digest: b153c5286b0b4bf4bc448a1b9d635515

Returns the query value associated with key *key* from the URL, using the options specified in *encoding* to encode the return value. If the key *key* is not found, this function returns an empty string. If you need to distinguish between an empty value and a non-existent key, you should check for the key's presence first using :sip:ref:`~PyQt6.QtCore.QUrlQuery.hasQueryItem`.

If the key *key* is multiply defined, this function will return the first one found, in the order they were present in the query string or added using :sip:ref:`~PyQt6.QtCore.QUrlQuery.addQueryItem`.

**Note:** The key is expected to be in percent-encoded form.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrlQuery.addQueryItem`, :sip:ref:`~PyQt6.QtCore.QUrlQuery.allQueryItemValues`, Encoding.
