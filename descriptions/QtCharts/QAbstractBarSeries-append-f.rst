.. sip:method-description::
    :status: todo
    :pysig: 201bb307b6ac3a682b13dad52e1b4798
    :realsig: (QBarSet*)
    :digest: 9348e959b8e1f84d0345bb73236a002e

Adds a set of bars specified by *set* to the bar series and takes ownership of it. If the set is null or it already belongs to the series, it will not be appended. Returns ``true`` if appending succeeded.
