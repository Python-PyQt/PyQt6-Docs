.. sip:method-description::
    :status: todo
    :pysig: a22ebaa09d7b4d7f39256027764f9bab
    :realsig: (const QString&,QUrl::ParsingMode)
    :digest: c5c33b5ced5b272e74aafa5b46fff283

Sets the query string of the URL to *query*.

This function is useful if you need to pass a query string that does not fit into the key-value pattern, or that uses a different scheme for encoding special characters than what is suggested by :sip:ref:`~PyQt6.QtCore.QUrl`.

Passing a value of QString() to *query* (a null QString) unsets the query completely. However, passing a value of QString("") will set the query to an empty value, as if the original URL had a lone "?".

The *query* data is interpreted according to *mode*: in :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.StrictMode`, any '%' characters must be followed by exactly two hexadecimal characters and some characters (including space) are not allowed in undecoded form. In :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.TolerantMode`, all characters are accepted in undecoded form and the tolerant parser will correct stray '%' not followed by two hex characters. In :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.DecodedMode`, '%' stand for themselves and encoded characters are not possible.

Query strings often contain percent-encoded sequences, so use of :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.DecodedMode` is discouraged. One special sequence to be aware of is that of the plus character ('+'). :sip:ref:`~PyQt6.QtCore.QUrl` does not convert spaces to plus characters, even though HTML forms posted by web browsers do. In order to represent an actual plus character in a query, the sequence "%2B" is usually used. This function will leave "%2B" sequences untouched in :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.TolerantMode` or :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.StrictMode`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.query`, :sip:ref:`~PyQt6.QtCore.QUrl.hasQuery`.
