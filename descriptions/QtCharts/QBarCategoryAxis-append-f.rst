.. sip:method-description::
    :status: todo
    :pysig: 8aa4db8179170d37e11ad02ad96f4d34
    :realsig: (const QStringList&)
    :digest: 64957c289582cd0ba9ca24e59635d04e

Appends *categories* to an axis. The maximum value on the axis will be changed to match the last category in *categories*. If no categories were previously defined, the minimum value on the axis will also be changed to match the first category in *categories*.

A category has to be a valid QString and it cannot be duplicated. Duplicated categories will not be appended.
