.. sip:enum-member-description::
    :status: todo
    :value: 23
    :digest: e41bb9b84582cc47de4bdab083c9e6f1

The frame is stored using an 8-bit per component planar YVU format with the V and U planes horizontally and vertically sub-sampled. This is similar to the  type, except that the lines of the V and U planes are interleaved, i.e. each line of V data is followed by a line of U data creating a single line of the same stride as the Y data.
