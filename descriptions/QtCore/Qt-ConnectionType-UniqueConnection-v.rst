.. sip:enum-member-description::
    :status: todo
    :value: 0x80
    :digest: 1e9cca4ce39b55a8e3c274e5e75a4a7b

This is a flag that can be combined with any one of the above connection types, using a bitwise OR. When Qt::UniqueConnection is set, QObject::connect() will fail if the connection already exists (i.e. if the same signal is already connected to the same slot for the same pair of objects). This flag was introduced in Qt 4.6.
