.. sip:method-description::
    :status: todo
    :pysig: bab5c0e581d25682638382ee3c1c852b
    :realsig: (QUrl::ComponentFormattingOptions) const
    :digest: f8a204726a8824fee046914dd9de7d8d

Returns the query string of the URL if there's a query string, or an empty result if not. To determine if the parsed URL contained a query string, use :sip:ref:`~PyQt6.QtCore.QUrl.hasQuery`.

The *options* argument controls how to format the query component. All values produce an unambiguous result. With :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOption.FullyDecoded`, all percent-encoded sequences are decoded; otherwise, the returned value may contain some percent-encoded sequences for some control sequences not representable in decoded form in QString.

Note that use of :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOption.FullyDecoded` in queries is discouraged, as queries often contain data that is supposed to remain percent-encoded, including the use of the "%2B" sequence to represent a plus character ('+').

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.setQuery`, :sip:ref:`~PyQt6.QtCore.QUrl.hasQuery`.
