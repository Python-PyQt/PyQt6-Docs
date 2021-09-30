.. sip:method-description::
    :status: todo
    :pysig: e4d59d2a16d27f5368f1aec20a3c7147
    :realsig: (QByteArrayView,qsizetype) const
    :digest: 0b00e3e9e2f328e2db18967d1826d970

Returns the index position of the start of the last occurrence of the sequence of bytes viewed by *bv* in this byte array, searching backward from index position *from*. If *from* is -1, the search starts at the last character; if *from* is -2, at the next to last character and so on. Returns -1 if no match is found.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 247-252

**Note:** When searching for a 0-length *bv*, the match at the end of the data is excluded from the search by a negative *from*, even though ``-1`` is normally thought of as searching from the end of the byte array: the match at the end is *after* the last character, so it is excluded. To include such a final empty match, either give a positive value for *from* or omit the *from* parameter entirely.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.indexOf`, :sip:ref:`~PyQt6.QtCore.QByteArray.contains`, :sip:ref:`~PyQt6.QtCore.QByteArray.count`.
