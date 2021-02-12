.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: e102f8d03426a4626d45f30657e64aff

Transforms the revision into an integer value, encoding the minor version into the least significant byte, and the major version into the second least significant byte.

``Integer`` needs to be at least 16 bits wide, and must not have a sign bit in the least significant 16 bits.

.. seealso:: fromEncodedVersion().
