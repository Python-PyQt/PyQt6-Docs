.. sip:enum-description::
    :status: todo
    :realname: QFileDevice::Permission
    :digest: 75bc284cdff8231ff94ec6ff9b80c2dc

This enum is used by the permission() function to report the permissions and ownership of a file. The values may be OR-ed together to test multiple permissions and ownership values.

**Warning:** Because of differences in the platforms supported by Qt, the semantics of ,  and  are platform-dependent: On Unix, the rights of the owner of the file are returned and on Windows the rights of the current user are returned. This behavior might change in a future Qt version.

**Note:** On NTFS file systems, ownership and permissions checking is disabled by default for performance reasons. To enable it, include the following line:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-ntfsp.py
    :lines: 55-55

Permission checking is then turned on and off by incrementing and decrementing ``qt_ntfs_permission_lookup`` by 1.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-ntfsp.py
    :lines: 59-60
