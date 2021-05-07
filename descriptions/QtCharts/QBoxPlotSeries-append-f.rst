.. sip:method-description::
    :status: todo
    :pysig: 7391025762bc8f48f5353c7e0b1b6e0b
    :realsig: (QBoxSet*)
    :digest: 37b7b63a064d97d02b79b879019d44ae

Adds a single box-and-whiskers item specified by *set* to the series and takes ownership of it. If the item is null or it already belongs to the series, it will not be appended. Returns ``true`` if appending succeeded.
