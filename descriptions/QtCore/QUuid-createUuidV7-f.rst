.. sip:method-description::
    :status: todo
    :pysig: feb5eb0b809686bfed4e30cbacd7fa8e
    :realsig: ()
    :digest: eb3eeaa55f8ab47de54fb2100c742e85

This function returns a new UUID with variant :sip:ref:`~PyQt6.QtCore.QUuid.Variant.DCE` and version :sip:ref:`~PyQt6.QtCore.QUuid.Version.UnixEpoch`.

It uses a time-ordered value field derived from the number of milliseconds since the UNIX Epoch as described by `RFC9562 <https://datatracker.ietf.org/doc/html/rfc9562#name-uuid-version-7>`_.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUuid.variant`, :sip:ref:`~PyQt6.QtCore.QUuid.version`, :sip:ref:`~PyQt6.QtCore.QUuid.createUuidV3`, :sip:ref:`~PyQt6.QtCore.QUuid.createUuidV5`.
