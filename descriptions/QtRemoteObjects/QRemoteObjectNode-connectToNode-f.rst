.. sip:method-description::
    :status: todo
    :pysig: 690ff780a2b2b089099cc8704f4803c0
    :realsig: (const QUrl&)
    :digest: fcab56596ffbc54d38a6b1a9c12b08ba

Connects a client node to the host node at *address*.

Connections will remain valid until the host node is deleted or no longer accessible over a network.

Once a client is connected to a host, valid Replicas can then be acquired if the corresponding Source is being remoted.

Return ``true`` on success, ``false`` otherwise (usually an unrecognized url, or connecting to already connected address).
