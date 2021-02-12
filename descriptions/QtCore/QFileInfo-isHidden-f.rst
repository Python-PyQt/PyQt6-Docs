.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 2492d9bd8a6f24f066b5046467e36f5c

Returns ``true`` if this is a `hidden' file; otherwise returns ``false``.

**Note:** This function returns ``true`` for the special entries "." and ".." on Unix, even though :sip:ref:`~PyQt6.QtCore.QDir.entryList` threats them as shown. And note that, since this function inspects the file name, on Unix it will inspect the name of the symlink, if this file is a symlink, not the target's name.

On Windows, this function returns ``true`` if the target file is hidden (not the symlink).
