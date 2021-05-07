.. sip:enum-member-description::
    :status: todo
    :value: 0x0001
    :digest: 90a60922fe3fac1587ecc08d7c15db1a

The mapped memory will be private, so any modifications will not be visible to other processes and will not be written to disk. Any such modifications will be lost when the memory is unmapped. It is unspecified whether modifications made to the file made after the mapping is created will be visible through the mapped memory. This enum value was introduced in Qt 5.4.
