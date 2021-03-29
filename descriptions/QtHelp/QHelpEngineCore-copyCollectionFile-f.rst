.. sip:method-description::
    :status: todo
    :pysig: 9d2496c01394f04863ec354dfad3b4be
    :realsig: (const QString&)
    :digest: 2fe58fe536d658221d6f90bb032eb174

Creates the file *fileName* and copies all contents from the current collection file into the newly created file, and returns true if successful; otherwise returns false.

The copying process makes sure that file references to Qt Collection files (``.qch``) files are updated accordingly.
