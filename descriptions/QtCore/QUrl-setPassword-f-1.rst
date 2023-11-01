.. sip:method-description::
    :status: todo
    :pysig: be14aad66c89fca68fdab2dde771f1ff
    :realsig: (const QString&, QUrl::ParsingMode)
    :digest: e427d4ecede291ef101c1825e265830d

Sets the URL's password to *password*. The *password* is part of the user info element in the authority of the URL, as described in :sip:ref:`~PyQt6.QtCore.QUrl.setUserInfo`.

The *password* data is interpreted according to *mode*: in :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.StrictMode`, any '%' characters must be followed by exactly two hexadecimal characters and some characters (including space) are not allowed in undecoded form. In :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.TolerantMode`, all characters are accepted in undecoded form and the tolerant parser will correct stray '%' not followed by two hex characters. In :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.DecodedMode`, '%' stand for themselves and encoded characters are not possible.

:sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.DecodedMode` should be used when setting the password from a data source which is not a URL, such as a password dialog shown to the user or with a password obtained by calling :sip:ref:`~PyQt6.QtCore.QUrl.password` with the :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOption.FullyDecoded` formatting option.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.password`, :sip:ref:`~PyQt6.QtCore.QUrl.setUserInfo`.
