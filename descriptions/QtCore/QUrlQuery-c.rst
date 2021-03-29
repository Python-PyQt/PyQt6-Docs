.. sip:class-description::
    :status: todo
    :brief: Way to manipulate a key-value pairs in a URL's query
    :digest: 732eb8f6a4426ff99005e7bbfe61930a

The :sip:ref:`~PyQt6.QtCore.QUrlQuery` class provides a way to manipulate a key-value pairs in a URL's query.

It is used to parse the query strings found in URLs like the following:

.. image:: ../../../images/qurl-querystring.png

Query strings like the above are used to transmit options in the URL and are usually decoded into multiple key-value pairs. The one above would contain two entries in its list, with keys "type" and "color". :sip:ref:`~PyQt6.QtCore.QUrlQuery` can also be used to create a query string suitable for use in :sip:ref:`~PyQt6.QtCore.QUrl.setQuery` from the individual components of the query.

The most common way of parsing a query string is to initialize it in the constructor by passing it the query string. Otherwise, the :sip:ref:`~PyQt6.QtCore.QUrlQuery.setQuery` method can be used to set the query to be parsed. That method can also be used to parse a query with non-standard delimiters, after having set them using the :sip:ref:`~PyQt6.QtCore.QUrlQuery.setQueryDelimiters` function.

The encoded query string can be obtained again using :sip:ref:`~PyQt6.QtCore.QUrlQuery.query`. This will take all the internally-stored items and encode the string using the delimiters.

.. _qurlquery-encoding:

Encoding
--------

All of the getter methods in :sip:ref:`~PyQt6.QtCore.QUrlQuery` support an optional parameter of type QUrl::ComponentFormattingOptions, including :sip:ref:`~PyQt6.QtCore.QUrlQuery.query`, which dictate how to encode the data in question. Except for :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOptions.FullyDecoded`, the returned value must still be considered a percent-encoded string, as there are certain values which cannot be expressed in decoded form (like control characters, byte sequences not decodable to UTF-8). For that reason, the percent character is always represented by the string "%25".

.. _qurlquery-handling-of-spaces-and-plus:

Handling of spaces and plus ("+")
.................................

Web browsers usually encode spaces found in HTML FORM elements to a plus sign ("+") and plus signs to its percent-encoded form (%2B). However, the Internet specifications governing URLs do not consider spaces and the plus character equivalent.

For that reason, :sip:ref:`~PyQt6.QtCore.QUrlQuery` never encodes the space character to "+" and will never decode "+" to a space character. Instead, space characters will be rendered "%20" in encoded form.

To support encoding like that of HTML forms, :sip:ref:`~PyQt6.QtCore.QUrlQuery` also never decodes the "%2B" sequence to a plus sign nor encode a plus sign. In fact, any "%2B" or "+" sequences found in the keys, values, or query string are left exactly like written (except for the uppercasing of "%2b" to "%2B").

.. _qurlquery-full-decoding:

Full decoding
.............

With :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOptions.FullyDecoded` formatting, all percent-encoded sequences will be decoded fully and the '%' character is used to represent itself. :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOptions.FullyDecoded` should be used with care, since it may cause data loss. See the documentation of :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOptions.FullyDecoded` for information on what data may be lost.

This formatting mode should be used only when dealing with text presented to the user in contexts where percent-encoding is not desired. Note that :sip:ref:`~PyQt6.QtCore.QUrlQuery` setters and query methods do not support the counterpart :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.DecodedMode` parsing, so using :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOptions.FullyDecoded` to obtain a listing of keys may result in keys not found in the object.

.. _qurlquery-non-standard-delimiters:

Non-standard delimiters
-----------------------

By default, :sip:ref:`~PyQt6.QtCore.QUrlQuery` uses an equal sign ("=") to separate a key from its value, and an ampersand ("&") to separate key-value pairs from each other. It is possible to change the delimiters that :sip:ref:`~PyQt6.QtCore.QUrlQuery` uses for parsing and for reconstructing the query by calling :sip:ref:`~PyQt6.QtCore.QUrlQuery.setQueryDelimiters`.

Non-standard delimiters should be chosen from among what RFC 3986 calls "sub-delimiters". They are:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qurlquery.py
    :lines: 54-55

Use of other characters is not supported and may result in unexpected behaviour. :sip:ref:`~PyQt6.QtCore.QUrlQuery` does not verify that you passed a valid delimiter.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl`.
