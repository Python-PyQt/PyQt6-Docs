.. sip:method-description::
    :status: todo
    :pysig: 75ee07442dbcf5f809e6304efbfd43ce
    :realsig: (const QStringList&)
    :digest: c4739c0e3ce1933cfed14a2f81203a86

Adds each path in *paths* to the file system watcher. Paths are not added if they not exist, or if they are already being monitored by the file system watcher.

If a path specifies a directory, the :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.directoryChanged` signal will be emitted when the path is modified or removed from disk; otherwise the :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.fileChanged` signal is emitted when the path is modified, renamed, or removed.

The return value is a list of paths that could not be watched.

Reasons for a watch failure are generally system-dependent, but may include the resource not existing, access failures, or the total watch count limit, if the platform has one.

**Note:** There may be a system dependent limit to the number of files and directories that can be monitored simultaneously. If this limit has been reached, the excess *paths* will not be monitored, and they will be added to the returned QStringList.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.addPath`, :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.removePaths`.
