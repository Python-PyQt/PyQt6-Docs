.. sip:method-description::
    :status: todo
    :pysig: be14aad66c89fca68fdab2dde771f1ff
    :realsig: (const QString&, QUrl::ParsingMode)
    :digest: dca050ebb5b4f8c0db0ce003ca5a5b53

Sets the host of the URL to *host*. The host is part of the authority.

The *host* data is interpreted according to *mode*: in :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.StrictMode`, any '%' characters must be followed by exactly two hexadecimal characters and some characters (including space) are not allowed in undecoded form. In :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.TolerantMode`, all characters are accepted in undecoded form and the tolerant parser will correct stray '%' not followed by two hex characters. In :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.DecodedMode`, '%' stand for themselves and encoded characters are not possible.

Note that, in all cases, the result of the parsing must be a valid hostname according to STD 3 rules, as modified by the Internationalized Resource Identifiers specification (RFC 3987). Invalid hostnames are not permitted and will cause :sip:ref:`~PyQt6.QtCore.QUrl.isValid` to become false.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.host`, :sip:ref:`~PyQt6.QtCore.QUrl.setAuthority`.
