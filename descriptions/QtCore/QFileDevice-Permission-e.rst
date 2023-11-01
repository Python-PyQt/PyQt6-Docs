.. sip:enum-description::
    :status: todo
    :digest: 6ba751c7378445466607399b26963362

This enum is used by the permission() function to report the permissions and ownership of a file. The values may be OR-ed together to test multiple permissions and ownership values.

**Warning:** Because of differences in the platforms supported by Qt, the semantics of ReadUser, WriteUser and ExeUser are platform-dependent: On Unix, the rights of the owner of the file are returned and on Windows the rights of the current user are returned. This behavior might change in a future Qt version.

**Note:** On NTFS file systems, ownership and permissions checking is disabled by default for performance reasons. To enable it, include the following line:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-ntfsp.py
    :lines: 55-55

Permission checking is then turned on and off by incrementing and decrementing ``qt_ntfs_permission_lookup`` by 1.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-ntfsp.py
    :lines: 59-60

**Note:** Since this is a non-atomic global variable, it is only safe to increment or decrement ``qt_ntfs_permission_lookup`` before any threads other than the main thread have started or after every thread other than the main thread has ended.

**Note:** From Qt 6.6 the variable ``qt_ntfs_permission_lookup`` is deprecated. Please use the following alternatives.

The safe and easy way to manage permission checks is to use the RAII class ``QNtfsPermissionCheckGuard``.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-ntfsp.py

If you need more fine-grained control, it is possible to manage the permission with the following functions instead:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-ntfsp.py
