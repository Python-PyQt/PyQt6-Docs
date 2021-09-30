.. sip:method-description::
    :status: todo
    :pysig: 5af8e8362183e915ee0679f3ea3db3d0
    :realsig: (double,char,int) const
    :digest: e70f27f684ccd6cbe06f865e2f0f76e0

This is an overloaded function.

Returns a string representing the floating-point number *f*.

The form of the representation is controlled by the *format* and *precision* parameters.

The *format* defaults to ``'g'``. It can be any of the following:

+---------+----------------------------------------------------------+
| Format  | Meaning                                                  |
+=========+==========================================================+
| ``'e'`` | format as [-]9.9e[+|-]999                                |
+---------+----------------------------------------------------------+
| ``'E'`` | format as [-]9.9E[+|-]999                                |
+---------+----------------------------------------------------------+
| ``'f'`` | format as [-]9.9                                         |
+---------+----------------------------------------------------------+
| ``'g'`` | use ``'e'`` or ``'f'`` format, whichever is more concise |
+---------+----------------------------------------------------------+
| ``'G'`` | use ``'E'`` or ``'f'`` format, whichever is more concise |
+---------+----------------------------------------------------------+

For the ``'e'``, ``'E'``, and ``'f'`` formats, the *precision* represents the number of digits *after* the decimal point. For the ``'g'`` and ``'G'`` formats, the *precision* represents the maximum number of significant digits (trailing zeroes are omitted). The special *precision* value :sip:ref:`~PyQt6.QtCore.QLocale.FloatingPointPrecisionOption.FloatingPointShortest` selects the shortest representation that, when read as a number, gets back the original floating-point value. Aside from that, any negative *precision* is ignored in favor of the default, 6.

For the ``'e'``, ``'f'`` and ``'g'`` formats, positive infinity is represented as "inf", negative infinity as "-inf" and floating-point NaN (not-a-number) values are represented as "nan". For the ``'E'`` and ``'G'`` formats, "INF" and "NAN" are used instead. This does not vary with locale.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.toDouble`, :sip:ref:`~PyQt6.QtCore.QLocale.numberOptions`, :sip:ref:`~PyQt6.QtCore.QLocale.exponential`, :sip:ref:`~PyQt6.QtCore.QLocale.decimalPoint`, :sip:ref:`~PyQt6.QtCore.QLocale.zeroDigit`, :sip:ref:`~PyQt6.QtCore.QLocale.positiveSign`, :sip:ref:`~PyQt6.QtCore.QLocale.percent`, :sip:ref:`~PyQt6.QtCore.QLocale.toCurrencyString`, :sip:ref:`~PyQt6.QtCore.QLocale.formattedDataSize`, :sip:ref:`~PyQt6.QtCore.QLocale.FloatingPointPrecisionOption`.
