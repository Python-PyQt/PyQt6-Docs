.. sip:enum-member-description::
    :status: todo
    :value: 0x80
    :digest: e551e87f6d2a51eeb11289226be9c5dd

This is a flag that can be combined with any one of the above connection types, using a bitwise OR. When  is set, QObject::connect() will fail if the connection already exists (i.e. if the same signal is already connected to the same slot for the same pair of objects). This flag was introduced in Qt 4.6.
