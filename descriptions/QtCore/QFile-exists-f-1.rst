.. sip:method-description::
    :status: todo
    :pysig: 787ad3d0f6e2063950bbbf6e050908f3
    :realsig: (const QString&)
    :digest: 2a08dd16c2c6ae248008da8ca610de6a

Returns ``true`` if the file specified by *fileName* exists; otherwise returns ``false``.

**Note:** If *fileName* is a symlink that points to a non-existing file, false is returned.
