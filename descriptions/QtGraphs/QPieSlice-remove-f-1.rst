.. sip:method-description::
    :status: todo
    :pysig: f0c7d5396d6a5d6a682b5b229fc1d36f
    :realsig: (QPieSlice*)
    :digest: 80f4e48b15aac941df3858b68d960efc

Removes a single sub slice, specified by *slice*, from the slice and deletes it permanently.

The pointer cannot be referenced after this call.

Returns ``true`` if the removal succeeds.
