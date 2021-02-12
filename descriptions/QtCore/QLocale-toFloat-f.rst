.. sip:method-description::
    :status: todo
    :pysig: b6ff8212391c3070193e6f282d4b18de
    :realsig: (const QString&,bool*) const
    :digest: ec12e4fbf6f0de84389fc137fc58a983

Returns the float represented by the localized string *s*.

Returns an infinity if the conversion overflows or 0.0 if the conversion fails for any other reason (e.g. underflow).

If *ok* is not ``nullptr``, failure is reported by setting \*\ *ok* to ``false``, and success by setting \*\ *ok* to ``true``.

This function does not fall back to the 'C' locale if the string cannot be interpreted in this locale.

This function ignores leading and trailing whitespace.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.toDouble`, :sip:ref:`~PyQt6.QtCore.QLocale.toInt`, :sip:ref:`~PyQt6.QtCore.QLocale.toString`.
