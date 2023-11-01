.. sip:method-description::
    :status: todo
    :pysig: 1ab98a4411fb7d10d5134d664f82b37e
    :realsig: (const QString&)
    :digest: 2fe58fe536d658221d6f90bb032eb174

Creates the file *fileName* and copies all contents from the current collection file into the newly created file, and returns true if successful; otherwise returns false.

The copying process makes sure that file references to Qt Collection files (``.qch``) files are updated accordingly.
