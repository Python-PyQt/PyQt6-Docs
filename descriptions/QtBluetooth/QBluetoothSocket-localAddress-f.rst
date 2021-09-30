.. sip:method-description::
    :status: todo
    :pysig: 15bb6dd4c08c32ed8272c0814d30eefa
    :realsig: () const
    :digest: ebdc509a6046f6c288589f3ada0d0d91

Returns the address of the local device.

Although some platforms may differ the socket must generally be connected to guarantee the return of a valid address. In particular, this is true when dealing with platforms that support multiple local Bluetooth adapters.
