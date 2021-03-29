.. sip:method-description::
    :status: todo
    :pysig: 0a871eb5bad5f979df093da393588be8
    :realsig: (qreal) const
    :digest: 3328c9771a7ca4d52509554966b0ad89

Returns the point at at the percentage *t* of the current path. The argument *t* has to be between 0 and 1.

Note that similarly to other percent methods, the percentage measurement is not linear with regards to the length, if curves are present in the path. When curves are present the percentage argument is mapped to the t parameter of the Bezier equations.
