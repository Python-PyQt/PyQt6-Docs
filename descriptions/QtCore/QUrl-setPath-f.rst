.. sip:method-description::
    :status: todo
    :pysig: 108fb5694a994ef378c805ae2b1f5502
    :realsig: (const QString&,QUrl::ParsingMode)
    :digest: 4173f88b57dc71d2e28f9420b8866927

Sets the path of the URL to *path*. The path is the part of the URL that comes after the authority but before the query string.

.. image:: ../../../images/qurl-ftppath.png

For non-hierarchical schemes, the path will be everything following the scheme declaration, as in the following example:

.. image:: ../../../images/qurl-mailtopath.png

The *path* data is interpreted according to *mode*: in :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.StrictMode`, any '%' characters must be followed by exactly two hexadecimal characters and some characters (including space) are not allowed in undecoded form. In :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.TolerantMode`, all characters are accepted in undecoded form and the tolerant parser will correct stray '%' not followed by two hex characters. In :sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.DecodedMode`, '%' stand for themselves and encoded characters are not possible.

:sip:ref:`~PyQt6.QtCore.QUrl.ParsingMode.DecodedMode` should be used when setting the path from a data source which is not a URL, such as a dialog shown to the user or with a path obtained by calling :sip:ref:`~PyQt6.QtCore.QUrl.path` with the :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOptions.FullyDecoded` formatting option.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.path`.
