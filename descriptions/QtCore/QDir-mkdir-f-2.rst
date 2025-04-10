.. sip:method-description::
    :status: todo
    :pysig: 1ab98a4411fb7d10d5134d664f82b37e
    :realsig: (const QString&) const
    :digest: 03e68d5aa9355ae7d96890b051fda057

This is an overloaded function.

Creates a sub-directory called *dirName* with the platform-specific default permissions.

Returns ``true`` on success; returns ``false`` if the operation failed or the directory already existed.

On Windows, by default, a new directory inherits its permissions from its parent directory. Permissions are emulated using ACLs. These ACLs may be in non-canonical order when the group is granted less permissions than others. Files and directories with such permissions will generate warnings when the Security tab of the Properties dialog is opened. Granting the group all permissions granted to others avoids such warnings.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.rmdir`, :sip:ref:`~PyQt6.QtCore.QDir.mkpath`, :sip:ref:`~PyQt6.QtCore.QDir.rmpath`.
