.. sip:method-description::
    :status: todo
    :pysig: f0c7d5396d6a5d6a682b5b229fc1d36f
    :realsig: (QPieSlice*)
    :digest: 07726b96551b7f635bbe800f22c2a53b

Removes a single slice, specified by *slice*, from the series and deletes it permanently.

The pointer cannot be referenced after this call.

Returns ``true`` if the removal succeeds.
