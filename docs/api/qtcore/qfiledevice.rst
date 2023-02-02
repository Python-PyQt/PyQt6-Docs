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

    .. sip:enum:: PyQt6.QtCore.QFileDevice.FileHandleFlag
        :description: QtCore/QFileDevice-FileHandleFlag-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.FileHandleFlag.AutoCloseHandle
            :description: QtCore/QFileDevice-FileHandleFlag-AutoCloseHandle-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.FileHandleFlag.DontCloseHandle
            :description: QtCore/QFileDevice-FileHandleFlag-DontCloseHandle-v.rst

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

    .. sip:enum:: PyQt6.QtCore.QFileDevice.MemoryMapFlag
        :description: QtCore/QFileDevice-MemoryMapFlag-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.MemoryMapFlag.MapPrivateOption
            :description: QtCore/QFileDevice-MemoryMapFlag-MapPrivateOption-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.MemoryMapFlag.NoOptions
            :description: QtCore/QFileDevice-MemoryMapFlag-NoOptions-v.rst

    .. sip:enum:: PyQt6.QtCore.QFileDevice.Permission
        :description: QtCore/QFileDevice-Permission-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.Permission.ExeGroup
            :description: QtCore/QFileDevice-Permission-ExeGroup-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.Permission.ExeOther
            :description: QtCore/QFileDevice-Permission-ExeOther-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.Permission.ExeOwner
            :description: QtCore/QFileDevice-Permission-ExeOwner-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.Permission.ExeUser
            :description: QtCore/QFileDevice-Permission-ExeUser-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.Permission.ReadGroup
            :description: QtCore/QFileDevice-Permission-ReadGroup-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.Permission.ReadOther
            :description: QtCore/QFileDevice-Permission-ReadOther-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.Permission.ReadOwner
            :description: QtCore/QFileDevice-Permission-ReadOwner-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.Permission.ReadUser
            :description: QtCore/QFileDevice-Permission-ReadUser-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.Permission.WriteGroup
            :description: QtCore/QFileDevice-Permission-WriteGroup-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.Permission.WriteOther
            :description: QtCore/QFileDevice-Permission-WriteOther-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.Permission.WriteOwner
            :description: QtCore/QFileDevice-Permission-WriteOwner-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QFileDevice.Permission.WriteUser
            :description: QtCore/QFileDevice-Permission-WriteUser-v.rst

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
            flags: :sip:ref:`~PyQt6.QtCore.QFileDevice.MemoryMapFlag` = :sip:ref:`~PyQt6.QtCore.QFileDevice.MemoryMapFlag.NoOptions`
        :returns:
            :py:class:`~PyQt6.sip.voidptr`
        :description: QtCore/QFileDevice-map-f-2.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.permissions
        :returns:
            :sip:ref:`~PyQt6.QtCore.QFileDevice.Permission`
        :description: QtCore/QFileDevice-permissions-f-1.rst

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
            :sip:ref:`~PyQt6.QtCore.QFileDevice.Permission`
        :returns:
            bool
        :description: QtCore/QFileDevice-setPermissions-f-1.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.size
        :returns:
            int
        :description: QtCore/QFileDevice-size-f.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.unmap
        :args:
            :py:class:`~PyQt6.sip.voidptr`
        :returns:
            bool
        :description: QtCore/QFileDevice-unmap-f-1.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.unsetError
        :description: QtCore/QFileDevice-unsetError-f.rst

    .. sip:method:: PyQt6.QtCore.QFileDevice.writeData
        :args:
            Union[bytes, bytearray, memoryview, PyQt6.sip.array, PyQt6.sip.voidptr]
        :returns:
            int
        :description: QtCore/QFileDevice-writeData-f-1.rst
