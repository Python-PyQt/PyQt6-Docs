.. sip:method-description::
    :status: todo
    :pysig: 56bc90fb2ef12e920fef7683cf80f69d
    :realsig: (QIODeviceBase::OpenMode,QFileDevice::Permissions)
    :digest: 959ea9fc92548c8bafc829a1f7a5df16

This is an overloaded function.

If the file does not exist and *mode* implies creating it, it is created with the specified *permissions*.

On POSIX systems the actual permissions are influenced by the value of ``umask``.

On Windows the permissions are emulated using ACLs. These ACLs may be in non-canonical order when the group is granted less permissions than others. Files and directories with such permissions will generate warnings when the Security tab of the Properties dialog is opened. Granting the group all permissions granted to others avoids such warnings.

.. seealso:: QIODevice::OpenMode, :sip:ref:`~PyQt6.QtCore.QFile.setFileName`, QT_USE_NODISCARD_FILE_OPEN.
