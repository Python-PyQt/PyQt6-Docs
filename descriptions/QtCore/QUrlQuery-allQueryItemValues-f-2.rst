.. sip:method-description::
    :status: todo
    :pysig: 07d07d1c0d75006e34f792f3cad2b3eb
    :realsig: (const QString&, QUrl::ComponentFormattingOptions) const
    :digest: b4beb39a127bb46c08b17256152eb0dc

Returns the a list of query string values whose key is equal to *key* from the URL, using the options specified in *encoding* to encode the return value. If the key *key* is not found, this function returns an empty list.

**Note:** The key is expected to be in percent-encoded form.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrlQuery.queryItemValue`, :sip:ref:`~PyQt6.QtCore.QUrlQuery.addQueryItem`.
