.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 0a9885d3c035ff7ca55a9fd70c29c48d

Returns ``true`` if the object points to a junction; otherwise returns ``false``.

Junctions only exist on Windows' NTFS file system, and are typically created by the ``mklink`` command. They can be thought of as symlinks for directories, and can only be created for absolute paths on the local volume.
