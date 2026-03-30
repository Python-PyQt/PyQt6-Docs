:orphan:

.. sip:class:: PyQt6.QtCore.QFile
    :inherits: :sip:ref:`~PyQt6.QtCore.QFileDevice`
    :description: QtCore/QFile-c.rst

    .. sip:method:: PyQt6.QtCore.QFile.__init__
        :description: QtCore/QFile-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QFile.__init__
        :args:
            str|None
        :description: QtCore/QFile-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QFile.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtCore/QFile-__init__-f-2.rst

    .. sip:method:: PyQt6.QtCore.QFile.__init__
        :args:
            str|None
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtCore/QFile-__init__-f-3.rst

    .. sip:method:: PyQt6.QtCore.QFile.copy
        :args:
            str|None
        :returns:
            bool
        :description: QtCore/QFile-copy-f.rst

    .. sip:method:: PyQt6.QtCore.QFile.copy
        :args:
            str|None
            str|None
        :returns:
            bool
        :static:
        :description: QtCore/QFile-copy-f-1.rst

    .. sip:method:: PyQt6.QtCore.QFile.decodeName
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`|bytes|bytearray|memoryview
        :returns:
            str
        :static:
        :description: QtCore/QFile-decodeName-f.rst

    .. sip:method:: PyQt6.QtCore.QFile.decodeName
        :args:
            str
        :returns:
            str
        :static:
        :description: QtCore/QFile-decodeName-f-1.rst

    .. sip:method:: PyQt6.QtCore.QFile.encodeName
        :args:
            str|None
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :static:
        :description: QtCore/QFile-encodeName-f.rst

    .. sip:method:: PyQt6.QtCore.QFile.exists
        :returns:
            bool
        :description: QtCore/QFile-exists-f.rst

    .. sip:method:: PyQt6.QtCore.QFile.exists
        :args:
            str|None
        :returns:
            bool
        :static:
        :description: QtCore/QFile-exists-f-1.rst

    .. sip:method:: PyQt6.QtCore.QFile.fileName
        :returns:
            str
        :description: QtCore/QFile-fileName-f.rst

    .. sip:method:: PyQt6.QtCore.QFile.link
        :args:
            str|None
        :returns:
            bool
        :description: QtCore/QFile-link-f.rst

    .. sip:method:: PyQt6.QtCore.QFile.link
        :args:
            str|None
            str|None
        :returns:
            bool
        :static:
        :description: QtCore/QFile-link-f-1.rst

    .. sip:method:: PyQt6.QtCore.QFile.moveToTrash
        :returns:
            bool
        :description: QtCore/QFile-moveToTrash-f.rst

    .. sip:method:: PyQt6.QtCore.QFile.moveToTrash
        :args:
            str|None
        :returns:
            bool
            str
        :static:
        :description: QtCore/QFile-moveToTrash-f-1.rst

    .. sip:method:: PyQt6.QtCore.QFile.open
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag`
        :returns:
            bool
        :description: QtCore/QFile-open-f-2.rst

    .. sip:method:: PyQt6.QtCore.QFile.open
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag`
            :sip:ref:`~PyQt6.QtCore.QFileDevice.Permission`
        :returns:
            bool
        :description: QtCore/QFile-open-f-4.rst

    .. sip:method:: PyQt6.QtCore.QFile.open
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QIODeviceBase.OpenModeFlag`
            handleFlags: :sip:ref:`~PyQt6.QtCore.QFileDevice.FileHandleFlag` = :sip:ref:`~PyQt6.QtCore.QFileDevice.FileHandleFlag.DontCloseHandle`
        :returns:
            bool
        :description: QtCore/QFile-open-f-3.rst

    .. sip:method:: PyQt6.QtCore.QFile.permissions
        :returns:
            :sip:ref:`~PyQt6.QtCore.QFileDevice.Permission`
        :description: QtCore/QFile-permissions-f-2.rst

    .. sip:method:: PyQt6.QtCore.QFile.permissions
        :args:
            str|None
        :returns:
            :sip:ref:`~PyQt6.QtCore.QFileDevice.Permission`
        :static:
        :description: QtCore/QFile-permissions-f.rst

    .. sip:method:: PyQt6.QtCore.QFile.remove
        :returns:
            bool
        :description: QtCore/QFile-remove-f.rst

    .. sip:method:: PyQt6.QtCore.QFile.remove
        :args:
            str|None
        :returns:
            bool
        :static:
        :description: QtCore/QFile-remove-f-1.rst

    .. sip:method:: PyQt6.QtCore.QFile.rename
        :args:
            str|None
        :returns:
            bool
        :description: QtCore/QFile-rename-f.rst

    .. sip:method:: PyQt6.QtCore.QFile.rename
        :args:
            str|None
            str|None
        :returns:
            bool
        :static:
        :description: QtCore/QFile-rename-f-1.rst

    .. sip:method:: PyQt6.QtCore.QFile.resize
        :args:
            int
        :returns:
            bool
        :description: QtCore/QFile-resize-f.rst

    .. sip:method:: PyQt6.QtCore.QFile.resize
        :args:
            str|None
            int
        :returns:
            bool
        :static:
        :description: QtCore/QFile-resize-f-1.rst

    .. sip:method:: PyQt6.QtCore.QFile.setFileName
        :args:
            str|None
        :description: QtCore/QFile-setFileName-f.rst

    .. sip:method:: PyQt6.QtCore.QFile.setPermissions
        :args:
            :sip:ref:`~PyQt6.QtCore.QFileDevice.Permission`
        :returns:
            bool
        :description: QtCore/QFile-setPermissions-f-2.rst

    .. sip:method:: PyQt6.QtCore.QFile.setPermissions
        :args:
            str|None
            :sip:ref:`~PyQt6.QtCore.QFileDevice.Permission`
        :returns:
            bool
        :static:
        :description: QtCore/QFile-setPermissions-f.rst

    .. sip:method:: PyQt6.QtCore.QFile.size
        :returns:
            int
        :description: QtCore/QFile-size-f.rst

    .. sip:method:: PyQt6.QtCore.QFile.supportsMoveToTrash
        :returns:
            bool
        :static:
        :description: QtCore/QFile-supportsMoveToTrash-f.rst

    .. sip:method:: PyQt6.QtCore.QFile.symLinkTarget
        :returns:
            str
        :description: QtCore/QFile-symLinkTarget-f.rst

    .. sip:method:: PyQt6.QtCore.QFile.symLinkTarget
        :args:
            str|None
        :returns:
            str
        :static:
        :description: QtCore/QFile-symLinkTarget-f-1.rst
