.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 99bcd2ea5bc551ef6aba88032437492d

Returns ``true`` if this is a valid reference to a remote object. It returns ``false`` if there was an error during the creation of this interface (for instance, if the remote application does not exist).

Note: when dealing with remote objects, it is not always possible to determine if it exists when creating a :sip:ref:`~PyQt6.QtDBus.QDBusInterface`.
