.. sip:method-description::
    :status: todo
    :pysig: 02457a7b42f9c70b71ac0578f3fab681
    :realsig: (QFont::Tag) const
    :digest: 83363113bd623655f5fd9cc34be088b2

Retrieves the sfnt table specified by *tag* from the underlying physical font, or an empty byte array if no such table was found. The returned font table's byte order is Big Endian, like the sfnt format specifies.
