.. sip:method-description::
    :status: todo
    :pysig: 992e8d0e5b57a6e4e940f41b84286512
    :realsig: ()
    :digest: f32637ef7d62ee9e5e2ed6a50278c960

Returns the current system time zone IANA ID.

On Windows this ID is translated from the Windows ID using an internal translation table and the user's selected country. As a consequence there is a small chance any Windows install may have IDs not known by Qt, in which case "UTC" will be returned.
