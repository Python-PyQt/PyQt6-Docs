.. sip:enum-member-description::
    :status: todo
    :value: 23
    :digest: 19cc2cbec1859577dde0f26a00ac45bc

The frame is stored using an 8-bit per component planar YVU format with the V and U planes horizontally and vertically sub-sampled. This is similar to the Format_YV12 type, except that the lines of the V and U planes are interleaved, i.e. each line of V data is followed by a line of U data creating a single line of the same stride as the Y data.
