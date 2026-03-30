.. sip:method-description::
    :status: todo
    :pysig: f0c7d5396d6a5d6a682b5b229fc1d36f
    :realsig: (QPieSlice*)
    :digest: 4b5edd318b115962c80eec5e11bfbc33

Takes a single sub slice, specified by *slice*, from the series. Does not delete the slice object.

**Note:** The slice remains the slice's parent object. You must set the parent object to take full ownership.

Returns ``true`` if the take operation was successful.
