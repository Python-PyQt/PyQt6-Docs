.. sip:method-description::
    :status: todo
    :pysig: faa33805051e5416b4235b8b31813f63
    :realsig: (qsizetype, QPieSlice*)
    :digest: 94aa64ffa95a3d4b9965d2a1b8ff6090

Inserts the sub slice specified by *slice* to the slice before the sub slice at the position specified by *index*. Sub slice ownership is passed to the slice.

Returns ``true`` if inserting succeeds.
