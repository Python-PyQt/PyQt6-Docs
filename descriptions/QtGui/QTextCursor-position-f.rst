.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: f9006bc4733d61ce784794ade259f752

Returns the absolute position of the cursor within the document. The cursor is positioned between characters.

**Note:** The "characters" in this case refer to the string of QChar objects, i.e. 16-bit Unicode characters, and the position is considered an index into this string. This does not necessarily correspond to individual graphemes in the writing system, as a single grapheme may be represented by multiple Unicode characters, such as in the case of surrogate pairs, linguistic ligatures or diacritics.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCursor.setPosition`, :sip:ref:`~PyQt6.QtGui.QTextCursor.movePosition`, :sip:ref:`~PyQt6.QtGui.QTextCursor.anchor`, :sip:ref:`~PyQt6.QtGui.QTextCursor.positionInBlock`.
