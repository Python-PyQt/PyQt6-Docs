.. sip:method-description::
    :status: todo
    :pysig: 3661c5104eb7d7270fb018db9f4a57af
    :realname: QFontMetricsF::boundingRect
    :realsig: (QChar) const
    :digest: f53e946abf9a5d5c1ed1430ffcf437d5

Returns the bounding rectangle of the character *ch* relative to the left-most point on the base line.

Note that the bounding rectangle may extend to the left of (0, 0), e.g. for italicized fonts, and that the text output may cover *all* pixels in the bounding rectangle.

Note that the rectangle usually extends both above and below the base line.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontMetricsF.horizontalAdvance`.
