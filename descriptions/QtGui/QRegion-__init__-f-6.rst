.. sip:method-description::
    :status: todo
    :pysig: a41480ebff5dfaf8a7af72e1def5b0eb
    :realsig: (int,int,int,int,QRegion::RegionType)
    :digest: b9bf855b43cfd2138ca7912121f50b32

Constructs a rectangular or elliptic region.

If *t* is ``Rectangle``, the region is the filled rectangle (\ *x*, *y*, *w*, *h*). If *t* is ``Ellipse``, the region is the filled ellipse with center at (\ *x* + *w* / 2, *y* + *h* / 2) and size (\ *w* ,\ *h*).
