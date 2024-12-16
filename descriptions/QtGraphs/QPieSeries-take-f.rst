.. sip:method-description::
    :status: todo
    :pysig: f0c7d5396d6a5d6a682b5b229fc1d36f
    :realsig: (QPieSlice*)
    :digest: b491fac73a2b07f68bdc25d02c9baeba

Takes a single slice, specified by *slice*, from the series. Does not delete the slice object.

**Note:** The series remains the slice's parent object. You must set the parent object to take full ownership.

Returns ``true`` if the take operation was successful.
