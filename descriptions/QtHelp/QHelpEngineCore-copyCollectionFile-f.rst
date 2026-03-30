.. sip:method-description::
    :status: todo
    :pysig: 502f7d3e77c89e5ef63bfbd42eaccbfd
    :realsig: (const QString&)
    :digest: 2fe58fe536d658221d6f90bb032eb174

Creates the file *fileName* and copies all contents from the current collection file into the newly created file, and returns true if successful; otherwise returns false.

The copying process makes sure that file references to Qt Collection files (``.qch``) files are updated accordingly.
