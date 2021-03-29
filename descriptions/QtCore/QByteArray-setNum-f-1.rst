.. sip:method-description::
    :status: todo
    :pysig: 9fd787b90c99a23637f0e8f90afb9680
    :realsig: (double,char,int)
    :digest: c07edc8c093d1cf77500223772d5e13a

This is an overloaded function.

Sets the byte array to the printed value of *n*, formatted in format *f* with precision *prec*, and returns a reference to the byte array.

The format *f* can be any of the following:

+--------+----------------------------------------------------------+
| Format | Meaning                                                  |
+========+==========================================================+
| ``e``  | format as [-]9.9e[+|-]999                                |
+--------+----------------------------------------------------------+
| ``E``  | format as [-]9.9E[+|-]999                                |
+--------+----------------------------------------------------------+
| ``f``  | format as [-]9.9                                         |
+--------+----------------------------------------------------------+
| ``g``  | use ``e`` or ``f`` format, whichever is the most concise |
+--------+----------------------------------------------------------+
| ``G``  | use ``E`` or ``f`` format, whichever is the most concise |
+--------+----------------------------------------------------------+

With 'e', 'E', and 'f', *prec* is the number of digits after the decimal point. With 'g' and 'G', *prec* is the maximum number of significant digits (trailing zeroes are omitted).

**Note:** The format of the number is not localized; the default C locale is used regardless of the user's locale. Use :sip:ref:`~PyQt6.QtCore.QLocale` to perform locale-aware conversions between numbers and strings.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.toDouble`.
