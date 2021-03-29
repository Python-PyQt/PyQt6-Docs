.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 502562ba9b4a2b447b0194e20032e8c7

Returns the seat with which the device is associated, if known; otherwise empty.

Devices that are intended to be used together by one user may be configured to have the same seat name. That is only possible on Wayland and X11 platforms so far.
