.. sip:enum-member-description::
    :status: todo
    :value: 0x0001
    :digest: b59fd35dd4a711dadc234b75a03da092

The match is constrained to start exactly at the offset passed to :sip:ref:`~PyQt6.QtCore.QRegularExpression.match` in order to be successful, even if the pattern string does not contain any metacharacter that anchors the match at that point. Note that passing this option does not anchor the end of the match to the end of the subject; if you want to fully anchor a regular expression, use :sip:ref:`~PyQt6.QtCore.QRegularExpression.anchoredPattern`. This enum value has been introduced in Qt 6.0.
