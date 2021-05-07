.. sip:method-description::
    :status: todo
    :pysig: 9cce4adad6acf31ad2adba2a770fcc5a
    :realsig: (QPieSlice*)
    :digest: b491fac73a2b07f68bdc25d02c9baeba

Takes a single slice, specified by *slice*, from the series. Does not delete the slice object.

**Note:** The series remains the slice's parent object. You must set the parent object to take full ownership.

Returns ``true`` if the take operation was successful.
