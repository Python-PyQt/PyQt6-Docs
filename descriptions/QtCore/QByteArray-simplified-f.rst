.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: () const
    :digest: ad63fe6f87e2b0e6423def3f3fd19f30

Returns a copy of this byte array that has spacing characters removed from the start and end, and in which each sequence of internal spacing characters is replaced with a single space.

The spacing characters are those for which the standard C++ ``isspace()`` function returns ``true`` in the C locale; these are the ASCII characters tabulation '\\t', line feed '\\n', carriage return '\\r', vertical tabulation '\\v', form feed '\\f', and space ' '.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 315-317

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.trimmed`, QChar::SpecialCharacter, :ref:`qbytearray-spacing-characters`.
