.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 16598fffe26b2df36cda932b4413b199

Returns the zero digit character of this locale.

This is a single Unicode character but may be encoded as a surrogate pair, so is (since Qt 6.0) returned as a string. In most locales, other digits follow it in Unicode ordering - however, some number systems, notably those using U+3007 as zero, do not have contiguous digits. Use :sip:ref:`~PyQt6.QtCore.QLocale.toString` to obtain suitable representations of numbers, rather than trying to construct them from this zero digit.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.toString`.
