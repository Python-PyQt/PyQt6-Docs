.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 3560c86162858b6d8dff427467820351

Returns the digit-grouping separator for this locale.

This is a token used to break up long sequences of digits, in the representation of a number, to make it easier to read. In some locales it may be empty, indicating that digits should not be broken up into groups in this way. In others it may be a spacing character. It is (since Qt 6.0) returned as a string in case some locale needs more than one UTF-16 code-point to represent its separator.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.decimalPoint`, :sip:ref:`~PyQt6.QtCore.QLocale.toString`.
