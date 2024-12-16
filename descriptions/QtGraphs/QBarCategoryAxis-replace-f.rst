.. sip:method-description::
    :status: todo
    :pysig: 6fb60876b5136c816ecc1a895d3012c0
    :realsig: (const QString&, const QString&)
    :digest: 90a5b251de29cb483dfdd88c0d89067e

Replaces *oldCategory* with *newCategory*. If *oldCategory* does not exist on the axis, nothing is done. *newCategory* has to be a valid QString and it cannot be duplicated. If the minimum or maximum category is replaced, the minimum and maximum values on the axis are updated accordingly.
