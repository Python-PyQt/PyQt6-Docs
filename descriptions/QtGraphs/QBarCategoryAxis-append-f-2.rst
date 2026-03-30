.. sip:method-description::
    :status: todo
    :pysig: 252f2463b17d7b65060495677c920d4c
    :realsig: (const QStringList&)
    :digest: 64957c289582cd0ba9ca24e59635d04e

Appends *categories* to an axis. The maximum value on the axis will be changed to match the last category in *categories*. If no categories were previously defined, the minimum value on the axis will also be changed to match the first category in *categories*.

A category has to be a valid QString and it cannot be duplicated. Duplicated categories will not be appended.
