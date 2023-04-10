.. sip:enum-description::
    :status: todo
    :digest: 62a5fde87cbe4454379e916a58d43f72

The parsing mode controls the way :sip:ref:`~PyQt6.QtCore.QUrl` parses strings.

In TolerantMode, the parser has the following behaviour:

* Spaces and "%20": unencoded space characters will be accepted and will be treated as equivalent to "%20".

* Single "%" characters: Any occurrences of a percent character "%" not followed by exactly two hexadecimal characters (e.g., "13% coverage.html") will be replaced by "%25". Note that one lone "%" character will trigger the correction mode for all percent characters.

* Reserved and unreserved characters: An encoded URL should only contain a few characters as literals; all other characters should be percent-encoded. In TolerantMode, these characters will be accepted if they are found in the URL: space / double-quote / "<" / ">" / "" / "^" / "`" / "{" / "|" / "}" Those same characters can be decoded again by passing :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOption.DecodeReserved` to :sip:ref:`~PyQt6.QtCore.QUrl.toString` or :sip:ref:`~PyQt6.QtCore.QUrl.toEncoded`. In the getters of individual components, those characters are often returned in decoded form.

When in StrictMode, if a parsing error is found, :sip:ref:`~PyQt6.QtCore.QUrl.isValid` will return ``false`` and :sip:ref:`~PyQt6.QtCore.QUrl.errorString` will return a message describing the error. If more than one error is detected, it is undefined which error gets reported.

Note that TolerantMode is not usually enough for parsing user input, which often contains more errors and expectations than the parser can deal with. When dealing with data coming directly from the user – as opposed to data coming from data-transfer sources, such as other programs – it is recommended to use :sip:ref:`~PyQt6.QtCore.QUrl.fromUserInput`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.fromUserInput`, :sip:ref:`~PyQt6.QtCore.QUrl.setUrl`, :sip:ref:`~PyQt6.QtCore.QUrl.toString`, :sip:ref:`~PyQt6.QtCore.QUrl.toEncoded`, QUrl::FormattingOptions.
