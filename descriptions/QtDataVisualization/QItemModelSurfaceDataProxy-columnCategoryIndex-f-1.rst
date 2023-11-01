.. sip:method-description::
    :status: todo
    :pysig: 70ce07b225801abde2cb8f5bcae9bb3a
    :realsig: (const QString&)
    :digest: a2f754b8b755622db4e3754765930539

Returns the index of the specified *category* in the column categories list. If the category is not found, -1 is returned.

**Note:** If the automatic column categories generation is in use, this method will not return a valid index before the data in the model is resolved for the first time.
