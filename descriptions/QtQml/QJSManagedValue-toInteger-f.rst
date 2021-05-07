.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 89991de8dcb897bc263eeaeb408964fd

Converts the manged value to an integer. This first converts the value to a number by the rules of :sip:ref:`~PyQt6.QtQml.QJSManagedValue.toNumber`, and then clamps it into the integer range by the rules given for coercing the arguments to JavaScript bit shift operators into 32bit integers.

Internally, the value may already be stored as an integer, in which case a fast path is taken.

**Note:** Conversion of a managed value to a number can throw an exception. In particular, symbols cannot be coerced into numbers, or a custom valueOf() method may throw. In this case the result is 0 and the engine carries an error after the conversion.

**Note:** The JavaScript rules for coercing numbers into 32bit integers are unintuitive.
