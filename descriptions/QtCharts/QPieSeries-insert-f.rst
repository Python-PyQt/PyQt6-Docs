.. sip:method-description::
    :status: todo
    :pysig: e0b56d1ef6bb5783bb05c0d15869642f
    :realsig: (int,QPieSlice*)
    :digest: 01076ced312920eb0605d3bbf9f237f1

Inserts the slice specified by *slice* to the series before the slice at the position specified by *index*. Slice ownership is passed to the series.

Returns ``true`` if inserting succeeds.
