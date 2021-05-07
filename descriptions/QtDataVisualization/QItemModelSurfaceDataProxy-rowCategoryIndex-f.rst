.. sip:method-description::
    :status: todo
    :pysig: 0f9b0ea7a3407ca50e1df7b110b9ad1f
    :realsig: (const QString&)
    :digest: a2f754b8b755622db4e3754765930539

Returns the index of the specified *category* in the row categories list. If the row categories list is empty, -1 is returned.

**Note:** If the automatic row categories generation is in use, this method will not return a valid index before the data in the model is resolved for the first time.
