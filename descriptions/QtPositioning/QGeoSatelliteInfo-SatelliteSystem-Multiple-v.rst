.. sip:enum-member-description::
    :status: todo
    :value: 0xFF
    :digest: 96e6f2fa866204878056e968909495b5

This type normally indicates that the information is received from a device that supports multiple satellite systems, and the satellite system is not explicitly specified. Depending on the data source, you might use other information to determine the actual system type. One example of the usage of this type is an NMEA $GNGSA message, which contains the IDs of the satellites being used, but does not explicitly mention their system types.
