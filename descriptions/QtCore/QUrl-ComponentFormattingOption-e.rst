.. sip:enum-description::
    :status: todo
    :digest: 4aa144356a92850f7ba6200493b9fbdf

The component formatting options define how the components of an URL will be formatted when written out as text. They can be combined with the options from QUrl::FormattingOptions when used in :sip:ref:`~PyQt6.QtCore.QUrl.toString` and :sip:ref:`~PyQt6.QtCore.QUrl.toEncoded`.

The values of EncodeReserved and DecodeReserved should not be used together in one call. The behavior is undefined if that happens. They are provided as separate values because the behavior of the "pretty mode" with regards to reserved characters is different on certain components and specially on the full URL.

Full decoding
.............

The FullyDecoded mode is similar to the behavior of the functions returning QString in Qt 4.x, in that every character represents itself and never has any special meaning. This is true even for the percent character ('%'), which should be interpreted to mean a literal percent, not the beginning of a percent-encoded sequence. The same actual character, in all other decoding modes, is represented by the sequence "%25".

Whenever re-applying data obtained with QUrl::FullyDecoded into a :sip:ref:`~PyQt6.QtCore.QUrl`, care must be taken to use the :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.DecodedMode` parameter to the setters (like :sip:ref:`~PyQt6.QtCore.QUrl.setPath` and :sip:ref:`~PyQt6.QtCore.QUrl.setUserName`). Failure to do so may cause re-interpretation of the percent character ('%') as the beginning of a percent-encoded sequence.

This mode is quite useful when portions of a URL are used in a non-URL context. For example, to extract the username, password or file paths in an FTP client application, the FullyDecoded mode should be used.

This mode should be used with care, since there are two conditions that cannot be reliably represented in the returned QString. They are:

* **Non-UTF-8 sequences:** URLs may contain sequences of percent-encoded characters that do not form valid UTF-8 sequences. Since URLs need to be decoded using UTF-8, any decoder failure will result in the QString containing one or more replacement characters where the sequence existed.

* **Encoded delimiters:** URLs are also allowed to make a distinction between a delimiter found in its literal form and its equivalent in percent-encoded form. This is most commonly found in the query, but is permitted in most parts of the URL.

The following example illustrates the problem:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qurl.py
    :lines: 127-132

If the two URLs were used via HTTP GET, the interpretation by the web server would probably be different. In the first case, it would interpret as one parameter, with a key of "q" and value "a+=b&c". In the second case, it would probably interpret as two parameters, one with a key of "q" and value "a =b", and the second with a key "c" and no value.

.. seealso:: QUrl::FormattingOptions.
