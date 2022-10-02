.. sip:enum-member-description::
    :status: todo
    :value: 21
    :digest: ab927d1f075d93be2841c2ed6c85e690

The frame is stored using an 8-bit per component planar YUV format with the U and V planes horizontally and vertically sub-sampled. This is similar to the Format_YUV420P type, except that the lines of the U and V planes are interleaved, i.e. each line of U data is followed by a line of V data creating a single line of the same stride as the Y data.
