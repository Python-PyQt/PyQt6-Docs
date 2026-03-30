.. sip:method-description::
    :status: todo
    :pysig: e6c5088a0c0ce5ed18b12806178d0b0a
    :realsig: (const QString&, bool*) const
    :digest: 21b1689588c1f89d4ffdb5578da43d42

Returns the unsigned long int represented by the localized string *s*.

If the conversion fails the function returns 0.

If *ok* is not ``nullptr``, failure is reported by setting \*\ *ok* to ``false``, and success by setting \*\ *ok* to ``true``.

This function ignores leading and trailing whitespace.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.toLong`, :sip:ref:`~PyQt6.QtCore.QLocale.toInt`, :sip:ref:`~PyQt6.QtCore.QLocale.toDouble`, :sip:ref:`~PyQt6.QtCore.QLocale.toString`.
