.. sip:method-description::
    :status: todo
    :pysig: 9d2496c01394f04863ec354dfad3b4be
    :realsig: (const QString&)
    :digest: dcbde06220e2deb4098658f1019dfaff

Removes the *service* from the list of services being watched by this object. Note that D-Bus notifications are asynchronous, so there may still be signals pending delivery about *service*. Those signals will still be emitted whenever the D-Bus messages are processed.

This function returns ``true`` if any services were removed.
