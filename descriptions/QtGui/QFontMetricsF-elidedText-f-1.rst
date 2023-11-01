.. sip:method-description::
    :status: todo
    :pysig: eabb40833a1dfe1ca67c65ee06b0bad0
    :realsig: (const QString&, Qt::TextElideMode, qreal, int) const
    :digest: a1aa617d0a09056a7eed347381e72154

If the string *text* is wider than *width*, returns an elided version of the string (i.e., a string with "..." in it). Otherwise, returns the original string.

The *mode* parameter specifies whether the text is elided on the left (for example, "...tech"), in the middle (for example, "Tr...ch"), or on the right (for example, "Trol...").

The *width* is specified in pixels, not characters.

The *flags* argument is optional and currently only supports :sip:ref:`~PyQt6.QtCore.Qt.TextFlag.TextShowMnemonic` as value.

The elide mark follows the :sip:ref:`~PyQt6.QtCore.Qt.LayoutDirection`. For example, it will be on the right side of the text for right-to-left layouts if the *mode* is ``Qt::ElideLeft``, and on the left side of the text if the *mode* is ``Qt::ElideRight``.
