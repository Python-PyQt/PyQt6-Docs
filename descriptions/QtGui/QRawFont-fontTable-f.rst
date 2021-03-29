.. sip:method-description::
    :status: todo
    :pysig: 037e8b81052efa4cc6b703dc1a3e78a2
    :realsig: (const char*) const
    :digest: 4f3bfa79172013a7cf4f8cbfc9c41bbc

Retrieves the sfnt table named *tagName* from the underlying physical font, or an empty byte array if no such table was found. The returned font table's byte order is Big Endian, like the sfnt format specifies. The *tagName* must be four characters long and should be formatted in the default endianness of the current platform.
