.. sip:method-description::
    :status: todo
    :pysig: f5079c184afb8cd3e47bc562098d0c92
    :realsig: (QUrl::FormattingOptions) const
    :digest: 924cf31b9038119ec708aa4a7fd1cbc6

Returns the encoded representation of the URL if it's valid; otherwise an empty :sip:ref:`~PyQt6.QtCore.QByteArray` is returned. The output can be customized by passing flags with *options*.

The user info, path and fragment are all converted to UTF-8, and all non-ASCII characters are then percent encoded. The host name is encoded using Punycode.
