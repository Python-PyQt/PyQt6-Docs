.. sip:method-description::
    :status: todo
    :pysig: 502f7d3e77c89e5ef63bfbd42eaccbfd
    :realsig: (const QString&)
    :digest: 1aca36acae6062740e345a231c213c6b

Removes the specified *path* from the file system watcher.

If the watch is successfully removed, true is returned.

Reasons for watch removal failing are generally system-dependent, but may be due to the path having already been deleted, for example.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.removePaths`, :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.addPath`.
