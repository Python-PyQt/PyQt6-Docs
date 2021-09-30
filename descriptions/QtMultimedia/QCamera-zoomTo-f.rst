.. sip:method-description::
    :status: todo
    :pysig: 6a1bb6ed41f44b60e7bd83b0e9945aa7
    :realsig: (float,float)
    :digest: 975873701125b11bd962a12d11348941

Zooms to a zoom factor *factor* using *rate*.

The *rate* is specified in powers of two per second. At a rate of 1 it would take 2 seconds to go from a zoom factor of 1 to 4.

**Note:** Using a specific rate is not supported on all cameras. If not supported, zooming will happen as fast as possible.
