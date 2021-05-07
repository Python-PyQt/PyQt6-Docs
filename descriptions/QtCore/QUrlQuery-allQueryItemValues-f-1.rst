.. sip:method-description::
    :status: todo
    :pysig: db6a17286360e70c0002f51bcf953a48
    :realsig: (const QString&,QUrl::ComponentFormattingOptions) const
    :digest: e27974a22f53a7dd4f7e159d4a2a8941

Returns the a list of query string values whose key is equal to *key* from the URL, using the options specified in *encoding* to encode the return value. If the key *key* is not found, this function returns an empty list.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrlQuery.queryItemValue`, :sip:ref:`~PyQt6.QtCore.QUrlQuery.addQueryItem`.
