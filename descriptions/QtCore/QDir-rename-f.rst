.. sip:method-description::
    :status: todo
    :pysig: ddd634297b2e52e60c1db514902761b2
    :realsig: (const QString&,const QString&)
    :digest: 7ab53d07a5a0c4741ba9dd2e19b555c9

Renames a file or directory from *oldName* to *newName*, and returns true if successful; otherwise returns ``false``.

On most file systems,  fails only if *oldName* does not exist, or if a file with the new name already exists. However, there are also other reasons why  can fail. For example, on at least one file system  fails if *newName* points to an open file.

If *oldName* is a file (not a directory) that can't be renamed right away, Qt will try to copy *oldName* to *newName* and remove *oldName*.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFile.rename`.
