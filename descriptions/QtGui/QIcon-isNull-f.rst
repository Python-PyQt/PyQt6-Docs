.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: e8a2afa88c22293ca0127da050902c7d

Returns ``true`` if the icon is empty; otherwise returns ``false``.

An icon is empty if it has neither a pixmap nor a filename.

Note: Even a non-null icon might not be able to create valid pixmaps, eg. if the file does not exist or cannot be read.
