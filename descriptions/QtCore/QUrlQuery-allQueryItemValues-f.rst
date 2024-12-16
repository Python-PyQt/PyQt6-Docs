.. sip:method-description::
    :status: todo
    :pysig: 523e1ca4365c05e20fefc345713d4f67
    :realsig: (const QString&, QUrl::ComponentFormattingOptions) const
    :digest: b4beb39a127bb46c08b17256152eb0dc

Returns the a list of query string values whose key is equal to *key* from the URL, using the options specified in *encoding* to encode the return value. If the key *key* is not found, this function returns an empty list.

**Note:** The key is expected to be in percent-encoded form.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrlQuery.queryItemValue`, :sip:ref:`~PyQt6.QtCore.QUrlQuery.addQueryItem`.
