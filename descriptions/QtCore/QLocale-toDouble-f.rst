.. sip:method-description::
    :status: todo
    :pysig: b6ff8212391c3070193e6f282d4b18de
    :realsig: (const QString&,bool*) const
    :digest: ac8bdfaa628520b3331d63240b3d1b42

Returns the double represented by the localized string *s*.

Returns an infinity if the conversion overflows or 0.0 if the conversion fails for any other reason (e.g. underflow).

If *ok* is not ``nullptr``, failure is reported by setting \*\ *ok* to ``false``, and success by setting \*\ *ok* to ``true``.

This function does not fall back to the 'C' locale if the string cannot be interpreted in this locale.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qlocale.py
    :lines: 93-106

Notice that the last conversion returns 1234.0, because '.' is the thousands group separator in the German locale.

This function ignores leading and trailing whitespace.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.toFloat`, :sip:ref:`~PyQt6.QtCore.QLocale.toInt`, :sip:ref:`~PyQt6.QtCore.QLocale.toString`.
