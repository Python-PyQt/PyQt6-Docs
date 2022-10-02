.. sip:enum-description::
    :status: todo
    :digest: 98a694f1d6e1ebcfd36187fd36594309

Describes the color range used by the video data. Video data usually comes in either full color range, where all values are being used, or a more limited range traditionally used in YUV video formats, where a subset of all values is being used.

The color range traditionally used by most YUV video formats. For 8 bit formats, the Y component is limited to values between 16 and 235. The U and V components are limited to values between 16 and 240

For higher bit depths multiply these values with 2^(depth-8).

Full color range. All values from 0 to 2^depth - 1 are valid.
