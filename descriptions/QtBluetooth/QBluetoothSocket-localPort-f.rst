.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: e26651d72d3b3d6d733ade1506a66474

Returns the port number of the local socket if available, otherwise returns 0. Although some platforms may differ the socket must generally be connected to guarantee the return of a valid port number.

On Android and macOS, this feature is not supported and returns 0.
