.. sip:method-description::
    :status: todo
    :pysig: 4f0d4ac1a4825fe915a3ee30656a58bb
    :realsig: (QSysInfo::Endian,bool*) const
    :digest: e8d3ef06e0d10f749f42c763ae9d6775

Returns the array of bit converted to an int. The conversion is based on *endianness*. Converts up to the first 32 bits of the array to ``quint32`` and returns it, obeying *endianness*. If *ok* is not a null pointer, and the array has more than 32 bits, *ok* is set to false and this function returns zero; otherwise, it's set to true.
