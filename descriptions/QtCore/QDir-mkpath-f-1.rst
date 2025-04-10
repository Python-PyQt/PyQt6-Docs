.. sip:method-description::
    :status: todo
    :pysig: 1ab98a4411fb7d10d5134d664f82b37e
    :realsig: (const QString&) const
    :digest: 6663c62f573e7b4900a8d84d2661664d

Creates a directory named *dirPath*.

If *dirPath* doesn't already exist, this method will create it - along with any nonexistent parent directories - with the default permissions.

Returns ``true`` on success or if *dirPath* already existed; otherwise returns ``false``.

On Windows, by default, a new directory inherits its permissions from its parent directory. Permissions are emulated using ACLs. These ACLs may be in non-canonical order when the group is granted less permissions than others. Files and directories with such permissions will generate warnings when the Security tab of the Properties dialog is opened. Granting the group all permissions granted to others avoids such warnings.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.rmpath`, :sip:ref:`~PyQt6.QtCore.QDir.mkdir`, :sip:ref:`~PyQt6.QtCore.QDir.rmdir`.
