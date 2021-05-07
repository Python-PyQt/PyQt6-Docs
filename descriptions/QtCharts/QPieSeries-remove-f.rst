.. sip:method-description::
    :status: todo
    :pysig: 9cce4adad6acf31ad2adba2a770fcc5a
    :realsig: (QPieSlice*)
    :digest: 07726b96551b7f635bbe800f22c2a53b

Removes a single slice, specified by *slice*, from the series and deletes it permanently.

The pointer cannot be referenced after this call.

Returns ``true`` if the removal succeeds.
