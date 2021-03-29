.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: () const
    :digest: 5687683d75aeb4cb5e2c0cd8d3359230

Returns a copy of this byte array with spacing characters removed from the start and end.

The spacing characters are those for which the standard C++ ``isspace()`` function returns ``true`` in the C locale; these are the ASCII characters tabulation '\\t', line feed '\\n', carriage return '\\r', vertical tabulation '\\v', form feed '\\f', and space ' '.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 322-324

Unlike :sip:ref:`~PyQt6.QtCore.QByteArray.simplified`,  leaves internal spacing unchanged.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.simplified`, QChar::SpecialCharacter, :ref:`qbytearray-spacing-characters`.
