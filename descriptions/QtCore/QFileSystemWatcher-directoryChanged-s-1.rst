.. sip:signal-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: e22d419ca4c4bf29e3a14edf02d2ca6b

This signal is emitted when the directory at a specified *path* is modified (e.g., when a file is added or deleted) or removed from disk. Note that if there are several changes during a short period of time, some of the changes might not emit this signal. However, the last change in the sequence of changes will always generate this signal.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.fileChanged`.
