.. sip:method-description::
    :status: todo
    :pysig: 86d6cf7b7c1cc1ebbda00d8e36e0a128
    :realsig: (const QString&, Qt::TextElideMode, int, int) const
    :digest: a1aa617d0a09056a7eed347381e72154

If the string *text* is wider than *width*, returns an elided version of the string (i.e., a string with "..." in it). Otherwise, returns the original string.

The *mode* parameter specifies whether the text is elided on the left (e.g., "...tech"), in the middle (e.g., "Tr...ch"), or on the right (e.g., "Trol...").

The *width* is specified in pixels, not characters.

The *flags* argument is optional and currently only supports :sip:ref:`~PyQt6.QtCore.Qt.TextFlag.TextShowMnemonic` as value.

The elide mark follows the :sip:ref:`~PyQt6.QtCore.Qt.LayoutDirection`. For example, it will be on the right side of the text for right-to-left layouts if the *mode* is ``Qt::ElideLeft``, and on the left side of the text if the *mode* is ``Qt::ElideRight``.
