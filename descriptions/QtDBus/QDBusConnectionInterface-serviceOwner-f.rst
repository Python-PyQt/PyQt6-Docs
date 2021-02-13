.. sip:method-description::
    :status: todo
    :pysig: b3295a2215af587ae9f6d1d88bd11477
    :realsig: (const QString&) const
    :digest: 41d749037ee82d986792002e411d2093

Returns the unique connection name of the primary owner of the name *name*. If the requested name doesn't have an owner, returns a ``org.freedesktop.DBus.Error.NameHasNoOwner`` error.
