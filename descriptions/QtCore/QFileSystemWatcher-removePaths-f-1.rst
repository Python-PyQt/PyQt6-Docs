.. sip:method-description::
    :status: todo
    :pysig: dcfa9e4ca08aedcff95d263365ff52ff
    :realsig: (const QStringList&)
    :digest: ebf59a1cd9943172eaf167453ca19c55

Removes the specified *paths* from the file system watcher.

The return value is a list of paths which were not able to be unwatched successfully.

Reasons for watch removal failing are generally system-dependent, but may be due to the path having already been deleted, for example.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.removePath`, :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.addPaths`.
