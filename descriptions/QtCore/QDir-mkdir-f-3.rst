.. sip:method-description::
    :status: todo
    :pysig: 58fdea0483bca48d4ed61ebbb256e1c7
    :realsig: (const QString&, QFileDevice::Permissions) const
    :digest: e41a63548c65d34878268cbc0afbb08f

Creates a sub-directory called *dirName*.

Returns ``true`` on success; otherwise returns ``false``.

If the directory already exists when this function is called, it will return ``false``.

The permissions of the created directory are set to *permissions*.

On POSIX systems the permissions are influenced by the value of ``umask``.

On Windows the permissions are emulated using ACLs. These ACLs may be in non-canonical order when the group is granted less permissions than others. Files and directories with such permissions will generate warnings when the Security tab of the Properties dialog is opened. Granting the group all permissions granted to others avoids such warnings.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.rmdir`.
