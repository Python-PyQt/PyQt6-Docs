.. sip:method-description::
    :status: todo
    :pysig: 87b99329d57d55b999bd2bfec9b01ec6
    :realname: QFontMetrics::boundingRect
    :realsig: (QChar) const
    :digest: cfad24ce7cb3fe21527a22e5031c4553

Returns the rectangle that is covered by ink if character *ch* were to be drawn at the origin of the coordinate system.

Note that the bounding rectangle may extend to the left of (0, 0) (e.g., for italicized fonts), and that the text output may cover *all* pixels in the bounding rectangle. For a space character the rectangle will usually be empty.

Note that the rectangle usually extends both above and below the base line.

**Warning:** The width of the returned rectangle is not the advance width of the character. Use (const QString &) or :sip:ref:`~PyQt6.QtGui.QFontMetrics.horizontalAdvance` instead.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontMetrics.horizontalAdvance`.
