.. sip:enum-member-description::
    :status: todo
    :value: 21
    :digest: f92e9f7a4440594897985bc932dedaa8

The frame is stored using an 8-bit per component planar YUV format with the U and V planes horizontally and vertically sub-sampled. This is similar to the  type, except that the lines of the U and V planes are interleaved, i.e. each line of U data is followed by a line of V data creating a single line of the same stride as the Y data.
