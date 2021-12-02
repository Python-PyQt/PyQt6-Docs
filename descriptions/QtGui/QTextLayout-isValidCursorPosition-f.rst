.. sip:method-description::
    :status: todo
    :pysig: 47bc384ef78158df7bdc68df0f06aef9
    :realsig: (int) const
    :digest: 983846d75f0550512dff4fb5a701c54b

/ Returns ``true`` if position *pos* is a valid cursor position.

In a Unicode context some positions in the text are not valid cursor positions, because the position is inside a Unicode surrogate or a grapheme cluster.

A grapheme cluster is a sequence of two or more Unicode characters that form one indivisible entity on the screen. For example the latin character `Ä' can be represented in Unicode by two characters, `A' (0x41), and the combining diaeresis (0x308). A text cursor can only validly be positioned before or after these two characters, never between them since that wouldn't make sense. In indic languages every syllable forms a grapheme cluster.
