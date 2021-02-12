.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 9ca4a9983e2c651ff37f409d1792346e

Returns ``true`` if this is a null variant, false otherwise.

A variant is considered null if it contains no initialized value or a null pointer.

**Note:** This behavior has been changed from Qt 5, where  would also return true if the variant contained an object of a builtin type with an  method that returned true for that object.

.. seealso:: convert(int).
