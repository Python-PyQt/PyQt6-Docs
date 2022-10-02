.. sip:method-description::
    :status: todo
    :pysig: dfba094f75fa496c6483821bc9ac9b18
    :realsig: (bool*,int) const
    :digest: 5a6b7f1ae2ba7e1e809156cbefa0778b

Returns the byte array converted to an ``int`` using base *base*, which is ten by default. Bases 0 and 2 through 36 are supported, using letters for digits beyond 9; A is ten, B is eleven and so on.

If *base* is 0, the base is determined automatically using the following rules: If the byte array begins with "0x", it is assumed to be hexadecimal (base 16); otherwise, if it begins with "0b", it is assumed to be binary (base 2); otherwise, if it begins with "0", it is assumed to be octal (base 8); otherwise it is assumed to be decimal.

Returns 0 if the conversion fails.

If *ok* is not ``nullptr``, failure is reported by setting \*\ *ok* to ``false``, and success by setting \*\ *ok* to ``true``.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 341-344

**Note:** The conversion of the number is performed in the default C locale, regardless of the user's locale. Use :sip:ref:`~PyQt6.QtCore.QLocale` to perform locale-aware conversions between numbers and strings.

**Note:** Support for the "0b" prefix was added in Qt 6.4.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.number`.
