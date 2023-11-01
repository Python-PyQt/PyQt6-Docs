.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 875a2430e1a0512ae0941ae8228133d5

Returns the exponent separator for this locale.

This is a token used to separate mantissa from exponent in some floating-point numeric representations. It is (since Qt 6.0) returned as a string because, in some locales, it is not a single character - for example, it may consist of a multiplication sign and a representation of the "ten to the power" operator.

.. seealso:: toString(double, char, int).
