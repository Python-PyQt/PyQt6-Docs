.. sip:method-description::
    :status: todo
    :pysig: 70103cb4bc89de9c0d1cdd3af536d4ff
    :realsig: (const QString&, bool*) const
    :digest: 8256c138e48b9a72acfd59a37c8c1c7a

Returns the float represented by the localized string *s*.

Returns an infinity if the conversion overflows or 0.0 if the conversion fails for any other reason (e.g. underflow).

If *ok* is not ``nullptr``, failure is reported by setting \*\ *ok* to ``false``, and success by setting \*\ *ok* to ``true``.

This function ignores leading and trailing whitespace.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.toDouble`, :sip:ref:`~PyQt6.QtCore.QLocale.toInt`, :sip:ref:`~PyQt6.QtCore.QLocale.toString`.
