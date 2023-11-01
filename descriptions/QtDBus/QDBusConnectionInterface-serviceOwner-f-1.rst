.. sip:method-description::
    :status: todo
    :pysig: 76c3e4438585fd77ca965677159dcbb9
    :realsig: (const QString&) const
    :digest: 41d749037ee82d986792002e411d2093

Returns the unique connection name of the primary owner of the name *name*. If the requested name doesn't have an owner, returns a ``org.freedesktop.DBus.Error.NameHasNoOwner`` error.
