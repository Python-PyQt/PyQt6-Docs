.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (QRgb)
    :digest: 9c0289cadb894b28af48ff7d81655716

Returns a gray value (0 to 255) from the given ARGB quadruplet *rgb*.

The gray value is calculated using the formula (R \* 11 + G \* 16 + B \* 5)/32; the alpha-channel is ignored.
