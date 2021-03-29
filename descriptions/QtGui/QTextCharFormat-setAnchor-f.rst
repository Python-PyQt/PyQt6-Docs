.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 871085f7aa8ee1a0ef6e5125e169bb72

If *anchor* is true, text with this format represents an anchor, and is formatted in the appropriate way; otherwise the text is formatted normally. (Anchors are hyperlinks which are often shown underlined and in a different color from plain text.)

The way the text is rendered is independent of whether or not the format has a valid anchor defined. Use :sip:ref:`~PyQt6.QtGui.QTextCharFormat.setAnchorHref`, and optionally :sip:ref:`~PyQt6.QtGui.QTextCharFormat.setAnchorNames` to create a hypertext link.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCharFormat.isAnchor`.
