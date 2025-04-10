.. sip:method-description::
    :status: todo
    :pysig: 58fdea0483bca48d4ed61ebbb256e1c7
    :realsig: (const QString&, QFileDevice::Permissions) const
    :digest: 93d7e9fbfa89574cc332638e9357fb65

Creates a sub-directory called *dirName* with the given *permissions*.

Returns ``true`` on success; returns ``false`` if the operation failed or the directory already existed.

On POSIX systems *permissions* are modified by the `
                             <https://pubs.opengroup.org/onlinepubs/9799919799/functions/umask.html>`_ (file creation mask) of the current process, which means some permission bits might be disabled.

On Windows, by default, a new directory inherits its permissions from its parent directory. *permissions* are emulated using ACLs. These ACLs may be in non-canonical order when the group is granted less permissions than others. Files and directories with such permissions will generate warnings when the Security tab of the Properties dialog is opened. Granting the group all permissions granted to others avoids such warnings.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDir.rmdir`, :sip:ref:`~PyQt6.QtCore.QDir.mkpath`, :sip:ref:`~PyQt6.QtCore.QDir.rmpath`.
