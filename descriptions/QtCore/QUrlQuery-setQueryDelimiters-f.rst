.. sip:method-description::
    :status: todo
    :pysig: 4b99ff73a8a869319570237b5c57ab03
    :realsig: (QChar,QChar)
    :digest: 4969828449710b612848b9e58ae38132

Sets the characters used for delimiting between keys and values, and between key-value pairs in the URL's query string. The default value delimiter is '=' and the default pair delimiter is '&'.

.. image:: ../../../images/qurl-querystring.png

*valueDelimiter* will be used for separating keys from values, and *pairDelimiter* will be used to separate key-value pairs. Any occurrences of these delimiting characters in the encoded representation of the keys and values of the query string are percent encoded when returned in :sip:ref:`~PyQt6.QtCore.QUrlQuery.query`.

If *valueDelimiter* is set to '(' and *pairDelimiter* is ')', the above query string would instead be represented like this:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qurl.py
    :lines: 83-83

**Note:** Non-standard delimiters should be chosen from among what RFC 3986 calls "sub-delimiters". They are:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qurlquery.py
    :lines: 54-55

Use of other characters is not supported and may result in unexpected behaviour. This method does not verify that you passed a valid delimiter.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrlQuery.queryValueDelimiter`, :sip:ref:`~PyQt6.QtCore.QUrlQuery.queryPairDelimiter`.
