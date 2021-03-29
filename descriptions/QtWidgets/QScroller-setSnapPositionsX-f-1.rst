.. sip:method-description::
    :status: todo
    :pysig: 6a1bb6ed41f44b60e7bd83b0e9945aa7
    :realsig: (qreal,qreal)
    :digest: 1acb71760d64ca7d574b387539db81de

Set the snap positions for the horizontal axis to regular spaced intervals. The first snap position is at *first*. The next at *first* + *interval*. This can be used to implement a list header. This overwrites all previously set snap positions and also a previously set snapping interval. Snapping can be deactivated by setting an interval of 0.0
