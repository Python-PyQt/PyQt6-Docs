.. sip:method-description::
    :status: todo
    :pysig: d34cc616a21a61b8d64f4cad282ca459
    :realsig: (const QString&, bool*) const
    :digest: 8de39d256fde332c0f2c1d84a001cd84

Returns the double represented by the localized string *s*.

Returns an infinity if the conversion overflows or 0.0 if the conversion fails for any other reason (e.g. underflow).

If *ok* is not ``nullptr``, failure is reported by setting \*\ *ok* to ``false``, and success by setting \*\ *ok* to ``true``.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qlocale.py
    :lines: 93-106

Notice that the last conversion returns 1234.0, because '.' is the thousands group separator in the German locale.

This function ignores leading and trailing whitespace.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.toFloat`, :sip:ref:`~PyQt6.QtCore.QLocale.toInt`, :sip:ref:`~PyQt6.QtCore.QLocale.toString`.
