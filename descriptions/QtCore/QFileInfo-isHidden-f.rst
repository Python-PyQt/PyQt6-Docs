.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 313232d459e41981e9c8f1af40e9bc41

Returns ``true`` if the file system entry this :sip:ref:`~PyQt6.QtCore.QFileInfo` refers to is `hidden'; otherwise returns ``false``.

**Note:** This function returns ``true`` for the special entries "." and ".." on Unix, even though :sip:ref:`~PyQt6.QtCore.QDir.entryList` treats them as shown. And note that, since this function inspects the file name, on Unix it will inspect the name of the symlink, if this file is a symlink, not the target's name.

On Windows, this function returns ``true`` if the target file is hidden (not the symlink).
