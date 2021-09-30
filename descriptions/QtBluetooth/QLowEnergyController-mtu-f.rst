.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 8fb91aedcd51579a35e5ea1cf5e38efa

Returns the MTU size.

During connection setup, the ATT MTU size is negotiated. This method provides the result of this negotiation. It can be used to optimize packet sizes in some situations. The maximum amount of data which can be transferred in a single packet is **mtu-3** bytes. 3 bytes are required for the ATT protocol header.

Before the connection setup and MTU negotiation, the default value of ``23`` will be returned.

Not every platform exposes the MTU value. On those platforms (e.g. Linux) this function always returns ``-1``.
