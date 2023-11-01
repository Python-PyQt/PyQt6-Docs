.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: () const
    :digest: b9c35c6bf8fa34b81ad8bdcda272635e

Returns the subvolume name for this volume.

Some filesystem types allow multiple subvolumes inside one device, which may be mounted in different paths (e.g. 'bind' mounts on Unix, or Btrfs filesystem subvolumes). If the subvolume could be detected, its name is returned by this function. The format of the subvolume name is specific to each filesystem type.

If this volume was not mounted from a subvolume of a larger filesystem or if the subvolume could not be detected, this function returns an empty byte array.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QStorageInfo.device`.
