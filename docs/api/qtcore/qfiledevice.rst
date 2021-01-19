:orphan:

.. sip:class:: PyQt6.QtCore.QFileDevice
    :inherits: :sip:ref:`~PyQt6.QtCore.QIODevice`
    :description: QtCore/QFileDevice-c.rst

    .. sip:enum:: PyQt6.QtCore.QFileDevice.FileError
        :description: QtCore/QFileDevice-FileError-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.FileError.AbortError
            :description: QtCore/QFileDevice-FileError-AbortError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.FileError.CopyError
            :description: QtCore/QFileDevice-FileError-CopyError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.FileError.FatalError
            :description: QtCore/QFileDevice-FileError-FatalError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.FileError.NoError
            :description: QtCore/QFileDevice-FileError-NoError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.FileError.OpenError
            :description: QtCore/QFileDevice-FileError-OpenError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.FileError.PermissionsError
            :description: QtCore/QFileDevice-FileError-PermissionsError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.FileError.PositionError
            :description: QtCore/QFileDevice-FileError-PositionError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.FileError.ReadError
            :description: QtCore/QFileDevice-FileError-ReadError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.FileError.RemoveError
            :description: QtCore/QFileDevice-FileError-RemoveError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.FileError.RenameError
            :description: QtCore/QFileDevice-FileError-RenameError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.FileError.ResizeError
            :description: QtCore/QFileDevice-FileError-ResizeError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.FileError.ResourceError
            :description: QtCore/QFileDevice-FileError-ResourceError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.FileError.TimeOutError
            :description: QtCore/QFileDevice-FileError-TimeOutError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.FileError.UnspecifiedError
            :description: QtCore/QFileDevice-FileError-UnspecifiedError-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.FileError.WriteError
            :description: QtCore/QFileDevice-FileError-WriteError-v.rst

    .. sip:enum:: PyQt6.QtCore.QFileDevice.FileHandleFlags
        :description: QtCore/QFileDevice-FileHandleFlags-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.FileHandleFlags.AutoCloseHandle
            :description: QtCore/QFileDevice-FileHandleFlags-AutoCloseHandle-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.FileHandleFlags.DontCloseHandle
            :description: QtCore/QFileDevice-FileHandleFlags-DontCloseHandle-v.rst

    .. sip:enum:: PyQt6.QtCore.QFileDevice.FileTime
        :description: QtCore/QFileDevice-FileTime-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.FileTime.FileAccessTime
            :description: QtCore/QFileDevice-FileTime-FileAccessTime-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.FileTime.FileBirthTime
            :description: QtCore/QFileDevice-FileTime-FileBirthTime-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.FileTime.FileMetadataChangeTime
            :description: QtCore/QFileDevice-FileTime-FileMetadataChangeTime-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.FileTime.FileModificationTime
            :description: QtCore/QFileDevice-FileTime-FileModificationTime-v.rst

    .. sip:enum:: PyQt6.QtCore.QFileDevice.MemoryMapFlags
        :description: QtCore/QFileDevice-MemoryMapFlags-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.MemoryMapFlags.MapPrivateOption
            :description: QtCore/QFileDevice-MemoryMapFlags-MapPrivateOption-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.MemoryMapFlags.NoOptions
            :description: QtCore/QFileDevice-MemoryMapFlags-NoOptions-v.rst

    .. sip:enum:: PyQt6.QtCore.QFileDevice.Permissions
        :description: QtCore/QFileDevice-Permissions-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.Permissions.ExeGroup
            :description: QtCore/QFileDevice-Permissions-ExeGroup-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.Permissions.ExeOther
            :description: QtCore/QFileDevice-Permissions-ExeOther-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.Permissions.ExeOwner
            :description: QtCore/QFileDevice-Permissions-ExeOwner-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.Permissions.ExeUser
            :description: QtCore/QFileDevice-Permissions-ExeUser-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.Permissions.ReadGroup
            :description: QtCore/QFileDevice-Permissions-ReadGroup-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.Permissions.ReadOther
            :description: QtCore/QFileDevice-Permissions-ReadOther-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.Permissions.ReadOwner
            :description: QtCore/QFileDevice-Permissions-ReadOwner-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.Permissions.ReadUser
            :description: QtCore/QFileDevice-Permissions-ReadUser-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.Permissions.WriteGroup
            :description: QtCore/QFileDevice-Permissions-WriteGroup-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.Permissions.WriteOther
            :description: QtCore/QFileDevice-Permissions-WriteOther-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.Permissions.WriteOwner
            :description: QtCore/QFileDevice-Permissions-WriteOwner-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.Permissions.WriteUser
            :description: QtCore/QFileDevice-Permissions-WriteUser-v.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.atEnd
        :returns:
            bool
        :description: QtCore/QFileDevice-atEnd-f.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.close
        :description: QtCore/QFileDevice-close-f.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.error
        :returns:
            :sip:ref:`~PyQt6.QtCore.QFileDevice.FileError`
        :description: QtCore/QFileDevice-error-f.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.fileName
        :returns:
            str
        :description: QtCore/QFileDevice-fileName-f.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.fileTime
        :args:
            :sip:ref:`~PyQt6.QtCore.QFileDevice.FileTime`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtCore/QFileDevice-fileTime-f.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.flush
        :returns:
            bool
        :description: QtCore/QFileDevice-flush-f.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.handle
        :returns:
            int
        :description: QtCore/QFileDevice-handle-f.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.isSequential
        :returns:
            bool
        :description: QtCore/QFileDevice-isSequential-f.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.map
        :args:
            int
            int
            flags: :sip:ref:`~PyQt6.QtCore.QFileDevice.MemoryMapFlags` = :sip:ref:`~PyQt6.QtCore.QFileDevice.MemoryMapFlags.NoOptions`
        :returns:
            sip.voidptr
        :description: QtCore/QFileDevice-map-f.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.permissions
        :returns:
            :sip:ref:`~PyQt6.QtCore.QFileDevice.Permissions`
        :description: QtCore/QFileDevice-permissions-f.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.pos
        :returns:
            int
        :description: QtCore/QFileDevice-pos-f.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.readData
        :args:
            int
        :returns:
            bytes
        :description: QtCore/QFileDevice-readData-f.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.readLineData
        :args:
            int
        :returns:
            bytes
        :description: QtCore/QFileDevice-readLineData-f.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.resize
        :args:
            int
        :returns:
            bool
        :description: QtCore/QFileDevice-resize-f.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.seek
        :args:
            int
        :returns:
            bool
        :description: QtCore/QFileDevice-seek-f.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.setFileTime
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QDateTime`, datetime.datetime]
            :sip:ref:`~PyQt6.QtCore.QFileDevice.FileTime`
        :returns:
            bool
        :description: QtCore/QFileDevice-setFileTime-f.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.setPermissions
        :args:
            :sip:ref:`~PyQt6.QtCore.QFileDevice.Permissions`
        :returns:
            bool
        :description: QtCore/QFileDevice-setPermissions-f.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.size
        :returns:
            int
        :description: QtCore/QFileDevice-size-f.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.unmap
        :args:
            sip.voidptr
        :returns:
            bool
        :description: QtCore/QFileDevice-unmap-f.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.unsetError
        :description: QtCore/QFileDevice-unsetError-f.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.writeData
        :args:
            buffer
        :returns:
            int
        :description: QtCore/QFileDevice-writeData-f.rst
