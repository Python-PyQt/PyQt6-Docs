.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: () const
    :digest: b9c7ede8f2cf1601c137f2fd5cdb7e86

Returns the device for this volume.

For example, on Unix filesystems (including macOS), this returns the devpath like ``/dev/sda0`` for local storages. On Windows, it returns the UNC path starting with ``\\\\?\\`` for local storages (in other words, the volume GUID).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QStorageInfo.rootPath`, :sip:ref:`~PyQt6.QtCore.QStorageInfo.subvolume`.
