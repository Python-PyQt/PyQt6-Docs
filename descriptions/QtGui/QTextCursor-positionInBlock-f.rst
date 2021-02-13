.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: fed418e17a00a4909e86b35b0459ff68

Returns the relative position of the cursor within the block. The cursor is positioned between characters.

This is equivalent to ``position() - block().position()``.

**Note:** The "characters" in this case refer to the string of QChar objects, i.e. 16-bit Unicode characters, and the position is considered an index into this string. This does not necessarily correspond to individual graphemes in the writing system, as a single grapheme may be represented by multiple Unicode characters, such as in the case of surrogate pairs, linguistic ligatures or diacritics.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCursor.position`.
