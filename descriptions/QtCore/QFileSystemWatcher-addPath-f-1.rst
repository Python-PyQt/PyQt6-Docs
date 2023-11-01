.. sip:method-description::
    :status: todo
    :pysig: 1ab98a4411fb7d10d5134d664f82b37e
    :realsig: (const QString&)
    :digest: 8fc4bc0c2a68c9b125edaa4b4d21b70c

Adds *path* to the file system watcher if *path* exists. The path is not added if it does not exist, or if it is already being monitored by the file system watcher.

If *path* specifies a directory, the :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.directoryChanged` signal will be emitted when *path* is modified or removed from disk; otherwise the :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.fileChanged` signal is emitted when *path* is modified, renamed or removed.

If the watch was successful, true is returned.

Reasons for a watch failure are generally system-dependent, but may include the resource not existing, access failures, or the total watch count limit, if the platform has one.

**Note:** There may be a system dependent limit to the number of files and directories that can be monitored simultaneously. If this limit is been reached, *path* will not be monitored, and false is returned.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.addPaths`, :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.removePath`.
