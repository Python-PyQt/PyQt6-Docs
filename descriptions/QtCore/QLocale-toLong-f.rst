.. sip:method-description::
    :status: todo
    :pysig: 01a14469e152a0ff2a4996affe14e914
    :realsig: (const QString&,bool*) const
    :digest: 4a7b05b57dbc15e8c8442924a85fcc8e

Returns the long int represented by the localized string *s*.

If the conversion fails the function returns 0.

If *ok* is not ``nullptr``, failure is reported by setting \*\ *ok* to ``false``, and success by setting \*\ *ok* to ``true``.

This function ignores leading and trailing whitespace.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.toInt`, :sip:ref:`~PyQt6.QtCore.QLocale.toULong`, :sip:ref:`~PyQt6.QtCore.QLocale.toDouble`, :sip:ref:`~PyQt6.QtCore.QLocale.toString`.
