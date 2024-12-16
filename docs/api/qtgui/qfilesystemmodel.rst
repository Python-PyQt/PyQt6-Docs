:orphan:

.. sip:class:: PyQt6.QtGui.QFileSystemModel
    :inherits: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
    :description: QtGui/QFileSystemModel-c.rst

    .. sip:enum:: PyQt6.QtGui.QFileSystemModel.Option
        :description: QtGui/QFileSystemModel-Option-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QFileSystemModel.Option.DontResolveSymlinks
            :description: QtGui/QFileSystemModel-Option-DontResolveSymlinks-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QFileSystemModel.Option.DontUseCustomDirectoryIcons
            :description: QtGui/QFileSystemModel-Option-DontUseCustomDirectoryIcons-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QFileSystemModel.Option.DontWatchForChanges
            :description: QtGui/QFileSystemModel-Option-DontWatchForChanges-v.rst

    .. sip:enum:: PyQt6.QtGui.QFileSystemModel.Roles
        :description: QtGui/QFileSystemModel-Roles-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QFileSystemModel.Roles.FileIconRole
            :description: QtGui/QFileSystemModel-Roles-FileIconRole-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QFileSystemModel.Roles.FileInfoRole
            :description: QtGui/QFileSystemModel-Roles-FileInfoRole-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QFileSystemModel.Roles.FileNameRole
            :description: QtGui/QFileSystemModel-Roles-FileNameRole-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QFileSystemModel.Roles.FilePathRole
            :description: QtGui/QFileSystemModel-Roles-FilePathRole-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QFileSystemModel.Roles.FilePermissions
            :description: QtGui/QFileSystemModel-Roles-FilePermissions-v.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGui/QFileSystemModel-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.canFetchMore
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtGui/QFileSystemModel-canFetchMore-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.columnCount
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            int
        :description: QtGui/QFileSystemModel-columnCount-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.data
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`
        :returns:
            Any
        :description: QtGui/QFileSystemModel-data-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.dropMimeData
        :args:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
            :sip:ref:`~PyQt6.QtCore.Qt.DropAction`
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtGui/QFileSystemModel-dropMimeData-f-1.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtGui/QFileSystemModel-event-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.fetchMore
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtGui/QFileSystemModel-fetchMore-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.fileIcon
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QIcon`
        :description: QtGui/QFileSystemModel-fileIcon-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.fileInfo
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QFileInfo`
        :description: QtGui/QFileSystemModel-fileInfo-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.fileName
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            str
        :description: QtGui/QFileSystemModel-fileName-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.filePath
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            str
        :description: QtGui/QFileSystemModel-filePath-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.filter
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDir.Filter`
        :description: QtGui/QFileSystemModel-filter-f-1.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.flags
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.ItemFlag`
        :description: QtGui/QFileSystemModel-flags-f-1.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.hasChildren
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtGui/QFileSystemModel-hasChildren-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.headerData
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`
        :returns:
            Any
        :description: QtGui/QFileSystemModel-headerData-f-1.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.iconProvider
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAbstractFileIconProvider`
        :description: QtGui/QFileSystemModel-iconProvider-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.index
        :args:
            Optional[str]
            column: int = 0
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtGui/QFileSystemModel-index-f-2.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.index
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtGui/QFileSystemModel-index-f-1.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.isDir
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtGui/QFileSystemModel-isDir-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.isReadOnly
        :returns:
            bool
        :description: QtGui/QFileSystemModel-isReadOnly-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.lastModified
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtGui/QFileSystemModel-lastModified-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.lastModified
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            :sip:ref:`~PyQt6.QtCore.QTimeZone`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDateTime`
        :description: QtGui/QFileSystemModel-lastModified-f-1.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.mimeData
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCore.QModelIndex`]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
        :description: QtGui/QFileSystemModel-mimeData-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.mimeTypes
        :returns:
            list[str]
        :description: QtGui/QFileSystemModel-mimeTypes-f-1.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.mkdir
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtGui/QFileSystemModel-mkdir-f-1.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.myComputer
        :args:
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`
        :returns:
            Any
        :description: QtGui/QFileSystemModel-myComputer-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.nameFilterDisables
        :returns:
            bool
        :description: QtGui/QFileSystemModel-nameFilterDisables-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.nameFilters
        :returns:
            list[str]
        :description: QtGui/QFileSystemModel-nameFilters-f-1.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.options
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFileSystemModel.Option`
        :description: QtGui/QFileSystemModel-options-f-1.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.parent
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtGui/QFileSystemModel-parent-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.permissions
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QFileDevice.Permission`
        :description: QtGui/QFileSystemModel-permissions-f-1.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.remove
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtGui/QFileSystemModel-remove-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.resolveSymlinks
        :returns:
            bool
        :description: QtGui/QFileSystemModel-resolveSymlinks-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.rmdir
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtGui/QFileSystemModel-rmdir-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.roleNames
        :returns:
            dict[int, :sip:ref:`~PyQt6.QtCore.QByteArray`]
        :description: QtGui/QFileSystemModel-roleNames-f-1.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.rootDirectory
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDir`
        :description: QtGui/QFileSystemModel-rootDirectory-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.rootPath
        :returns:
            str
        :description: QtGui/QFileSystemModel-rootPath-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.rowCount
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            int
        :description: QtGui/QFileSystemModel-rowCount-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.setData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            Any
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole`
        :returns:
            bool
        :description: QtGui/QFileSystemModel-setData-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.setFilter
        :args:
            :sip:ref:`~PyQt6.QtCore.QDir.Filter`
        :description: QtGui/QFileSystemModel-setFilter-f-1.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.setIconProvider
        :args:
            :sip:ref:`~PyQt6.QtGui.QAbstractFileIconProvider`
        :description: QtGui/QFileSystemModel-setIconProvider-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.setNameFilterDisables
        :args:
            bool
        :description: QtGui/QFileSystemModel-setNameFilterDisables-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.setNameFilters
        :args:
            Iterable[Optional[str]]
        :description: QtGui/QFileSystemModel-setNameFilters-f-1.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.setOption
        :args:
            :sip:ref:`~PyQt6.QtGui.QFileSystemModel.Option`
            on: bool = True
        :description: QtGui/QFileSystemModel-setOption-f-1.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.setOptions
        :args:
            :sip:ref:`~PyQt6.QtGui.QFileSystemModel.Option`
        :description: QtGui/QFileSystemModel-setOptions-f-1.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.setReadOnly
        :args:
            bool
        :description: QtGui/QFileSystemModel-setReadOnly-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.setResolveSymlinks
        :args:
            bool
        :description: QtGui/QFileSystemModel-setResolveSymlinks-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.setRootPath
        :args:
            Optional[str]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtGui/QFileSystemModel-setRootPath-f-1.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.sibling
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtGui/QFileSystemModel-sibling-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.size
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            int
        :description: QtGui/QFileSystemModel-size-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.sort
        :args:
            int
            order: :sip:ref:`~PyQt6.QtCore.Qt.SortOrder` = :sip:ref:`~PyQt6.QtCore.Qt.SortOrder.AscendingOrder`
        :description: QtGui/QFileSystemModel-sort-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.supportedDropActions
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.DropAction`
        :description: QtGui/QFileSystemModel-supportedDropActions-f-1.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.testOption
        :args:
            :sip:ref:`~PyQt6.QtGui.QFileSystemModel.Option`
        :returns:
            bool
        :description: QtGui/QFileSystemModel-testOption-f-1.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.timerEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimerEvent`
        :description: QtGui/QFileSystemModel-timerEvent-f.rst

    .. sip:method:: PyQt6.QtGui.QFileSystemModel.type
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            str
        :description: QtGui/QFileSystemModel-type-f.rst

    .. sip:signal:: PyQt6.QtGui.QFileSystemModel.directoryLoaded
        :args:
            Optional[str]
        :description: QtGui/QFileSystemModel-directoryLoaded-s-1.rst

    .. sip:signal:: PyQt6.QtGui.QFileSystemModel.fileRenamed
        :args:
            Optional[str]
            Optional[str]
            Optional[str]
        :description: QtGui/QFileSystemModel-fileRenamed-s-1.rst

    .. sip:signal:: PyQt6.QtGui.QFileSystemModel.rootPathChanged
        :args:
            Optional[str]
        :description: QtGui/QFileSystemModel-rootPathChanged-s-1.rst
