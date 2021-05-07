.. sip:method-description::
    :status: todo
    :pysig: de819777a6f52a9a4d93f0260ee40413
    :realsig: (int,QBoxSet*)
    :digest: 44dd6eb11051c1db35c3bb3ff07e41ca

Inserts a box-and-whiskers item specified by *set* to a series at the position specified by *index* and takes ownership of the item. If the item is null or already belongs to the series, it will not be appended. Returns ``true`` if inserting succeeds.
