.. sip:method-description::
    :status: todo
    :pysig: 01a14469e152a0ff2a4996affe14e914
    :realsig: (const QString&,bool*) const
    :digest: e6e18b8c6816c6b68827db04afe9da27

Returns the unsigned long long int represented by the localized string *s*.

If the conversion fails the function returns 0.

If *ok* is not ``nullptr``, failure is reported by setting \*\ *ok* to ``false``, and success by setting \*\ *ok* to ``true``.

This function ignores leading and trailing whitespace.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.toLongLong`, :sip:ref:`~PyQt6.QtCore.QLocale.toInt`, :sip:ref:`~PyQt6.QtCore.QLocale.toDouble`, :sip:ref:`~PyQt6.QtCore.QLocale.toString`.
