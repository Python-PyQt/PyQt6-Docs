.. sip:enum-description::
    :status: todo
    :realname: QDir::Filter
    :digest: c35b578166f4d0cf8ede2645a3701d22

This enum describes the filtering options available to :sip:ref:`~PyQt6.QtCore.QDir`; e.g. for :sip:ref:`~PyQt6.QtCore.QDir.entryList` and :sip:ref:`~PyQt6.QtCore.QDir.entryInfoList`. The filter value is specified by combining values from the following list using the bitwise OR operator:

Functions that use Filter enum values to filter lists of files and directories will include symbolic links to files and directories unless you set the  value.

A default constructed :sip:ref:`~PyQt6.QtCore.QDir` will not filter out files based on their permissions, so :sip:ref:`~PyQt6.QtCore.QDir.entryList` and :sip:ref:`~PyQt6.QtCore.QDir.entryInfoList` will return all files that are readable, writable, executable, or any combination of the three. This makes the default easy to write, and at the same time useful.

For example, setting the ``Readable``, ``Writable``, and ``Files`` flags allows all files to be listed for which the application has read access, write access or both. If the ``Dirs`` and ``Drives`` flags are also included in this combination then all drives, directories, all files that the application can read, write, or execute, and symlinks to such files/directories can be listed.

To retrieve the permissions for a directory, use the :sip:ref:`~PyQt6.QtCore.QDir.entryInfoList` function to get the associated :sip:ref:`~PyQt6.QtCore.QFileInfo` objects and then use the :sip:ref:`~PyQt6.QtCore.QFileInfo.permissions` to obtain the permissions and ownership for each file.
