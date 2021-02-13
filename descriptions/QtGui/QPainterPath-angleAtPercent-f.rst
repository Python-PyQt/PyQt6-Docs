.. sip:method-description::
    :status: todo
    :pysig: 6a1bb6ed41f44b60e7bd83b0e9945aa7
    :realsig: (qreal) const
    :digest: 906d321cafe3294c8ee423486b680f3d

Returns the angle of the path tangent at the percentage *t*. The argument *t* has to be between 0 and 1.

Positive values for the angles mean counter-clockwise while negative values mean the clockwise direction. Zero degrees is at the 3 o'clock position.

Note that similarly to the other percent methods, the percentage measurement is not linear with regards to the length if curves are present in the path. When curves are present the percentage argument is mapped to the t parameter of the Bezier equations.
