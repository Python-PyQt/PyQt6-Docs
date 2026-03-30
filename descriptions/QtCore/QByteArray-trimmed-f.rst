.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: () const
    :digest: ff9dd2a8e615c8cdc01b6ac30d4bddbb

Returns a copy of this byte array with spacing characters removed from the start and end.

The spacing characters are those for which the standard C++ ``isspace()`` function returns ``true`` in the C locale; these are the ASCII characters tabulation '``\t``', line feed '``\n``', carriage return '``\r``', vertical tabulation '``\v``', form feed '``\f``', and space ' '.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 322-324

Unlike :sip:ref:`~PyQt6.QtCore.QByteArray.simplified`, trimmed() leaves internal spacing unchanged.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.simplified`, QChar::SpecialCharacter, :ref:`qbytearray-spacing-characters`.
