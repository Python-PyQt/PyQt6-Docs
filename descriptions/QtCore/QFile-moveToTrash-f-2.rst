.. sip:method-description::
    :status: todo
    :pysig: 50d17f6f521250cb9c7a582402c47b28
    :realsig: (const QString&, QString*)
    :digest: 457d4ef4101b63dd74d980867d58d750

This is an overloaded function.

Moves the file specified by :sip:ref:`~PyQt6.QtCore.QFile.fileName` to the trash. Returns ``true`` if successful, and sets *pathInTrash* (if provided) to the path at which the file can be found within the trash; otherwise returns ``false``.

The time for this function to run is independent of the size of the file being trashed. If this function is called on a directory, it may be proportional to the number of files being trashed.

This function uses the Windows and macOS APIs to perform the trashing on those two operating systems. Elsewhere (Unix systems), this function implements the FreeDesktop.org Trash specification version 1.0.

**Note:** When using the FreeDesktop.org Trash implementation, this function will fail if it is unable to move the files to the trash location by way of file renames and hardlinks. This condition arises if the file being trashed resides on a volume (mount point) on which the current user does not have permission to create the ``.Trash`` directory, or with some unusual filesystem types or configurations (such as sub-volumes that aren't themselves mount points).

**Note:** On systems where the system API doesn't report the path of the file in the trash, *pathInTrash* will be set to the null string once the file has been moved. On systems that don't have a trash can, this function always returns false.
