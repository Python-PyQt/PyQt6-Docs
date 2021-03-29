.. sip:method-description::
    :status: todo
    :pysig: 4c35c6b51bc2a5b1cb547d1af033255f
    :realsig: (bool*) const
    :digest: 70b4638a693aef26c7b645a64030fd93

Returns the byte array converted to a ``float`` value.

Returns an infinity if the conversion overflows or 0.0 if the conversion fails for other reasons (e.g. underflow).

If *ok* is not ``nullptr``, failure is reported by setting \*\ *ok* to ``false``, and success by setting \*\ *ok* to ``true``.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 366-371

**Warning:** The :sip:ref:`~PyQt6.QtCore.QByteArray` content may only contain valid numerical characters which includes the plus/minus sign, the character e used in scientific notation, and the decimal point. Including the unit or additional characters leads to a conversion error.

**Note:** The conversion of the number is performed in the default C locale, regardless of the user's locale. Use :sip:ref:`~PyQt6.QtCore.QLocale` to perform locale-aware conversions between numbers and strings.

This function ignores leading and trailing whitespace.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.number`.
