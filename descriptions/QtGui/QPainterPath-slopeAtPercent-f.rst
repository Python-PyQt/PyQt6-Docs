.. sip:method-description::
    :status: todo
    :pysig: 6a1bb6ed41f44b60e7bd83b0e9945aa7
    :realsig: (qreal) const
    :digest: c0a4e48ad640a8fe63ac9aff6712b00b

Returns the slope of the path at the percentage *t*. The argument *t* has to be between 0 and 1.

Note that similarly to other percent methods, the percentage measurement is not linear with regards to the length, if curves are present in the path. When curves are present the percentage argument is mapped to the t parameter of the Bezier equations.
