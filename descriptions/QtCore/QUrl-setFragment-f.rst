.. sip:method-description::
    :status: todo
    :pysig: a22ebaa09d7b4d7f39256027764f9bab
    :realsig: (const QString&,QUrl::ParsingMode)
    :digest: 48c3abf38217ee009949f18ca7251549

Sets the fragment of the URL to *fragment*. The fragment is the last part of the URL, represented by a '#' followed by a string of characters. It is typically used in HTTP for referring to a certain link or point on a page:

.. image:: ../../../images/qurl-fragment.png

The fragment is sometimes also referred to as the URL "reference".

Passing an argument of QString() (a null QString) will unset the fragment. Passing an argument of QString("") (an empty but not null QString) will set the fragment to an empty string (as if the original URL had a lone "#").

The *fragment* data is interpreted according to *mode*: in :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.StrictMode`, any '%' characters must be followed by exactly two hexadecimal characters and some characters (including space) are not allowed in undecoded form. In :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.TolerantMode`, all characters are accepted in undecoded form and the tolerant parser will correct stray '%' not followed by two hex characters. In :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.DecodedMode`, '%' stand for themselves and encoded characters are not possible.

:sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.DecodedMode` should be used when setting the fragment from a data source which is not a URL or with a fragment obtained by calling :sip:ref:`~PyQt6.QtCore.QUrl.fragment` with the :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOptions.FullyDecoded` formatting option.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.fragment`, :sip:ref:`~PyQt6.QtCore.QUrl.hasFragment`.
