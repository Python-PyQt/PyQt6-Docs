.. sip:enum-member-description::
    :status: todo
    :value: 0
    :digest: b290ac28f036e4a1b77401f5db77ece1

A :sip:ref:`~PyQt6.QtGui.QTextCharFormat` for the part of the preedit string specified by start and length. value contains a `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ of type :sip:ref:`~PyQt6.QtGui.QTextFormat` specifying rendering of this part of the preedit string. There should be at most one format for every part of the preedit string. If several are specified for any character in the string the behaviour is undefined. A conforming implementation has to at least honor the backgroundColor, textColor and fontUnderline properties of the format.
