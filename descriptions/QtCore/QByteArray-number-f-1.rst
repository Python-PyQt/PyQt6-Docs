.. sip:method-description::
    :status: todo
    :pysig: 3bab94b6398a4d48acc3dbcf33b0e84c
    :realsig: (double,char,int)
    :digest: 11ea4d171d5c3a4c6ebdc864162702bd

This is an overloaded function.

Returns a byte array that contains the printed value of *n*, formatted in format *f* with precision *prec*.

Argument *n* is formatted according to the *f* format specified, which is ``g`` by default, and can be any of the following:

+--------+----------------------------------------------------------+
| Format | Meaning                                                  |
+========+==========================================================+
| ``e``  | format as [-]9.9e[+|-]999                                |
+--------+----------------------------------------------------------+
| ``E``  | format as [-]9.9E[+|-]999                                |
+--------+----------------------------------------------------------+
| ``f``  | format as [-]9.9                                         |
+--------+----------------------------------------------------------+
| ``g``  | use ``e`` or ``f`` format, whichever is the most concise |
+--------+----------------------------------------------------------+
| ``G``  | use ``E`` or ``f`` format, whichever is the most concise |
+--------+----------------------------------------------------------+

With 'e', 'E', and 'f', *prec* is the number of digits after the decimal point. With 'g' and 'G', *prec* is the maximum number of significant digits (trailing zeroes are omitted).

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 402-403

**Note:** The format of the number is not localized; the default C locale is used regardless of the user's locale. Use :sip:ref:`~PyQt6.QtCore.QLocale` to perform locale-aware conversions between numbers and strings.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.toDouble`.
