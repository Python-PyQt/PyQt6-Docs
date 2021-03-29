.. sip:class-description::
    :status: todo
    :brief: Interface for monitoring files and directories for modifications
    :digest: 335daad66bf4f5bcb12bc80e576d096e

The :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher` class provides an interface for monitoring files and directories for modifications.

:sip:ref:`~PyQt6.QtCore.QFileSystemWatcher` monitors the file system for changes to files and directories by watching a list of specified paths.

Call :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.addPath` to watch a particular file or directory. Multiple paths can be added using the :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.addPaths` function. Existing paths can be removed by using the :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.removePath` and :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.removePaths` functions.

:sip:ref:`~PyQt6.QtCore.QFileSystemWatcher` examines each path added to it. Files that have been added to the :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher` can be accessed using the :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.files` function, and directories using the :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.directories` function.

The :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.fileChanged` signal is emitted when a file has been modified, renamed or removed from disk. Similarly, the :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.directoryChanged` signal is emitted when a directory or its contents is modified or removed. Note that :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher` stops monitoring files once they have been renamed or removed from disk, and directories once they have been removed from disk.

* **Notes**:

  * On systems running a Linux kernel without inotify support, file systems that contain watched paths cannot be unmounted.

  * The act of monitoring files and directories for modifications consumes system resources. This implies there is a limit to the number of files and directories your process can monitor simultaneously. On all BSD variants, for example, an open file descriptor is required for each monitored file. Some system limits the number of open file descriptors to 256 by default. This means that :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.addPath` and :sip:ref:`~PyQt6.QtCore.QFileSystemWatcher.addPaths` will fail if your process tries to add more than 256 files or directories to the file system monitor. Also note that your process may have other file descriptors open in addition to the ones for files being monitored, and these other open descriptors also count in the total. macOS uses a different backend and does not suffer from this issue.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFile`, :sip:ref:`~PyQt6.QtCore.QDir`.
