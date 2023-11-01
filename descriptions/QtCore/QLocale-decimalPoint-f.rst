.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 441f63fa489fbcfd25b27719f5f53550

Returns the fractional part separator for this locale.

This is the token that separates the whole number part from the fracional part in the representation of a number which has a fractional part. This is commonly called the "decimal point character" - even though, in many locales, it is not a "point" (or similar dot). It is (since Qt 6.0) returned as a string in case some locale needs more than one UTF-16 code-point to represent its separator.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.groupSeparator`, :sip:ref:`~PyQt6.QtCore.QLocale.toString`.
