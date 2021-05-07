.. sip:method-description::
    :status: todo
    :pysig: 95d7ba721e6682cd5b2e2b012c7af273
    :realsig: (int,QBarSet*)
    :digest: 318f9244dac7f92d2e00b673151c6b69

Inserts a bar set specified by *set* to a series at the position specified by *index* and takes ownership of the set. If the set is null or already belongs to the series, it will not be appended. Returns ``true`` if inserting succeeds.
