.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: ce53b9f8d921af7d34a7972c314a7033

Appends *category* to an axis. The maximum value on the axis will be changed to match the last *category*. If no categories were previously defined, the minimum value on the axis will also be changed to match *category*.

A category has to be a valid QString and it cannot be duplicated. Duplicated categories will not be appended.
