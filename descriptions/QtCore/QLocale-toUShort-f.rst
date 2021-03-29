.. sip:method-description::
    :status: todo
    :pysig: 01a14469e152a0ff2a4996affe14e914
    :realsig: (const QString&,bool*) const
    :digest: 72e61cddc4cc9851bd7bb0e8321fe068

Returns the unsigned short int represented by the localized string *s*.

If the conversion fails the function returns 0.

If *ok* is not ``nullptr``, failure is reported by setting \*\ *ok* to ``false``, and success by setting \*\ *ok* to ``true``.

This function ignores leading and trailing whitespace.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.toShort`, :sip:ref:`~PyQt6.QtCore.QLocale.toString`.
