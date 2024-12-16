.. sip:method-description::
    :status: todo
    :pysig: faa33805051e5416b4235b8b31813f63
    :realsig: (qsizetype, QPieSlice*)
    :digest: 01076ced312920eb0605d3bbf9f237f1

Inserts the slice specified by *slice* to the series before the slice at the position specified by *index*. Slice ownership is passed to the series.

Returns ``true`` if inserting succeeds.
