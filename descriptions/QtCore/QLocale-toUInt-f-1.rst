.. sip:method-description::
    :status: todo
    :pysig: 6aa5d52918050ea965ba38c6dc78e9cb
    :realsig: (const QString&, bool*) const
    :digest: 7469983a41ddbc1cfd1b9f0fe233366b

Returns the unsigned int represented by the localized string *s*.

If the conversion fails the function returns 0.

If *ok* is not ``nullptr``, failure is reported by setting \*\ *ok* to ``false``, and success by setting \*\ *ok* to ``true``.

This function ignores leading and trailing whitespace.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.toInt`, :sip:ref:`~PyQt6.QtCore.QLocale.toString`.
