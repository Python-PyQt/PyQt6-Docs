.. sip:method-description::
    :status: todo
    :pysig: 3ff31f44bbc3d11e01ac0abe33819cb8
    :realsig: (int,QTextCursor::MoveMode)
    :digest: 632aefb999b790c87e596ae8e7bebb78

Moves the cursor to the absolute position in the document specified by *pos* using a ``MoveMode`` specified by *m*. The cursor is positioned between characters.

**Note:** The "characters" in this case refer to the string of QChar objects, i.e. 16-bit Unicode characters, and *pos* is considered an index into this string. This does not necessarily correspond to individual graphemes in the writing system, as a single grapheme may be represented by multiple Unicode characters, such as in the case of surrogate pairs, linguistic ligatures or diacritics. For a more generic approach to navigating the document, use :sip:ref:`~PyQt6.QtGui.QTextCursor.movePosition`, which will respect the actual grapheme boundaries in the text.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCursor.position`, :sip:ref:`~PyQt6.QtGui.QTextCursor.movePosition`, :sip:ref:`~PyQt6.QtGui.QTextCursor.anchor`.
