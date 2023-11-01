.. sip:method-description::
    :status: todo
    :pysig: dd431a34e6382be8567cf5b44f2db6a6
    :realsig: (const QString&)
    :digest: 2a08dd16c2c6ae248008da8ca610de6a

Returns ``true`` if the file specified by *fileName* exists; otherwise returns ``false``.

**Note:** If *fileName* is a symlink that points to a non-existing file, false is returned.
