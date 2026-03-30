.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: () const
    :digest: d3f5603822f331d27b8d4a1bca31873d

Returns a copy of this byte array that has spacing characters removed from the start and end, and in which each sequence of internal spacing characters is replaced with a single space.

The spacing characters are those for which the standard C++ ``isspace()`` function returns ``true`` in the C locale; these are the ASCII characters tabulation '``\t``', line feed '``\n``', carriage return '``\r``', vertical tabulation '``\v``', form feed '``\f``', and space ' '.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 315-317

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.trimmed`, QChar::SpecialCharacter, :ref:`qbytearray-spacing-characters`.
