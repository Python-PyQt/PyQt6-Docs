.. sip:enum-member-description::
    :status: todo
    :value: 0x100
    :digest: 2c07bcbb1555d3c6d991a89172497bf7

This is a flag that can be combined with any one of the above connection types, using a bitwise OR. When Qt::SingleShotConnection is set, the slot is going to be called only once; the connection will be automatically broken when the signal is emitted. This flag was introduced in Qt 6.0.
