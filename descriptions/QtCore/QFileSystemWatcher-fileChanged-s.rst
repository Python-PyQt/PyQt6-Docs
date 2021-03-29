.. sip:signal-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 601e5646e2b3d27db28153d6ce6a8b96

This signal is emitted when the file at the specified *path* is modified, renamed or removed from disk.

**Note:** As a safety measure, many applications save an open file by writing a new file and then deleting the old one. In your slot function, you can check ``watcher.files().contains(path)``. If it returns ``false``, check whether the file still exists and then call ``addPath()`` to continue watching it.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.directoryChanged`.
