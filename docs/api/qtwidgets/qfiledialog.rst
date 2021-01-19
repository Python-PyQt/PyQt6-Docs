:orphan:

.. sip:class:: PyQt6.QtWidgets.QFileDialog
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QDialog`
    :description: QtWidgets/QFileDialog-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QFileDialog.AcceptMode
        :description: QtWidgets/QFileDialog-AcceptMode-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFileDialog.AcceptMode.AcceptOpen
            :description: QtWidgets/QFileDialog-AcceptMode-AcceptOpen-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFileDialog.AcceptMode.AcceptSave
            :description: QtWidgets/QFileDialog-AcceptMode-AcceptSave-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QFileDialog.DialogLabel
        :description: QtWidgets/QFileDialog-DialogLabel-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFileDialog.DialogLabel.Accept
            :description: QtWidgets/QFileDialog-DialogLabel-Accept-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFileDialog.DialogLabel.FileName
            :description: QtWidgets/QFileDialog-DialogLabel-FileName-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFileDialog.DialogLabel.FileType
            :description: QtWidgets/QFileDialog-DialogLabel-FileType-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFileDialog.DialogLabel.LookIn
            :description: QtWidgets/QFileDialog-DialogLabel-LookIn-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFileDialog.DialogLabel.Reject
            :description: QtWidgets/QFileDialog-DialogLabel-Reject-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QFileDialog.FileMode
        :description: QtWidgets/QFileDialog-FileMode-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFileDialog.FileMode.AnyFile
            :description: QtWidgets/QFileDialog-FileMode-AnyFile-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFileDialog.FileMode.Directory
            :description: QtWidgets/QFileDialog-FileMode-Directory-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFileDialog.FileMode.ExistingFile
            :description: QtWidgets/QFileDialog-FileMode-ExistingFile-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFileDialog.FileMode.ExistingFiles
            :description: QtWidgets/QFileDialog-FileMode-ExistingFiles-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QFileDialog.Options
        :description: QtWidgets/QFileDialog-Options-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFileDialog.Options.DontConfirmOverwrite
            :description: QtWidgets/QFileDialog-Options-DontConfirmOverwrite-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFileDialog.Options.DontResolveSymlinks
            :description: QtWidgets/QFileDialog-Options-DontResolveSymlinks-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFileDialog.Options.DontUseCustomDirectoryIcons
            :description: QtWidgets/QFileDialog-Options-DontUseCustomDirectoryIcons-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFileDialog.Options.DontUseNativeDialog
            :description: QtWidgets/QFileDialog-Options-DontUseNativeDialog-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFileDialog.Options.HideNameFilterDetails
            :description: QtWidgets/QFileDialog-Options-HideNameFilterDetails-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFileDialog.Options.ReadOnly
            :description: QtWidgets/QFileDialog-Options-ReadOnly-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFileDialog.Options.ShowDirsOnly
            :description: QtWidgets/QFileDialog-Options-ShowDirsOnly-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QFileDialog.ViewMode
        :description: QtWidgets/QFileDialog-ViewMode-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFileDialog.ViewMode.Detail
            :description: QtWidgets/QFileDialog-ViewMode-Detail-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QFileDialog.ViewMode.List
            :description: QtWidgets/QFileDialog-ViewMode-List-v.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.__init__
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtCore.Qt.WindowFlags`
        :description: QtWidgets/QFileDialog-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
            caption: str = ''
            directory: str = ''
            filter: str = ''
        :description: QtWidgets/QFileDialog-__init__-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.accept
        :description: QtWidgets/QFileDialog-accept-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.acceptMode
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QFileDialog.AcceptMode`
        :description: QtWidgets/QFileDialog-acceptMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.changeEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtWidgets/QFileDialog-changeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.defaultSuffix
        :returns:
            str
        :description: QtWidgets/QFileDialog-defaultSuffix-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.directory
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDir`
        :description: QtWidgets/QFileDialog-directory-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.directoryUrl
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtWidgets/QFileDialog-directoryUrl-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.done
        :args:
            int
        :description: QtWidgets/QFileDialog-done-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.fileMode
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QFileDialog.FileMode`
        :description: QtWidgets/QFileDialog-fileMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.filter
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDir.Filters`
        :description: QtWidgets/QFileDialog-filter-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.getExistingDirectory
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
            caption: str = ''
            directory: str = ''
            options: :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Options` = :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Options.ShowDirsOnly`
        :returns:
            str
        :static:
        :description: QtWidgets/QFileDialog-getExistingDirectory-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.getExistingDirectoryUrl
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
            caption: str = ''
            directory: :sip:ref:`~PyQt6.QtCore.QUrl` = QUrl()
            options: :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Options` = :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Options.ShowDirsOnly`
            supportedSchemes: Iterable[str] = []
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :static:
        :description: QtWidgets/QFileDialog-getExistingDirectoryUrl-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.getOpenFileName
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
            caption: str = ''
            directory: str = ''
            filter: str = ''
            initialFilter: str = ''
            options: :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Options` = QFileDialog.Options()
        :returns:
            Tuple[str, str]
        :static:
        :description: QtWidgets/QFileDialog-getOpenFileName-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.getOpenFileNames
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
            caption: str = ''
            directory: str = ''
            filter: str = ''
            initialFilter: str = ''
            options: :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Options` = QFileDialog.Options()
        :returns:
            Tuple[List[str], str]
        :static:
        :description: QtWidgets/QFileDialog-getOpenFileNames-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.getOpenFileUrl
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
            caption: str = ''
            directory: :sip:ref:`~PyQt6.QtCore.QUrl` = QUrl()
            filter: str = ''
            initialFilter: str = ''
            options: :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Options` = QFileDialog.Options()
            supportedSchemes: Iterable[str] = []
        :returns:
            Tuple[:sip:ref:`~PyQt6.QtCore.QUrl`, str]
        :static:
        :description: QtWidgets/QFileDialog-getOpenFileUrl-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.getOpenFileUrls
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
            caption: str = ''
            directory: :sip:ref:`~PyQt6.QtCore.QUrl` = QUrl()
            filter: str = ''
            initialFilter: str = ''
            options: :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Options` = QFileDialog.Options()
            supportedSchemes: Iterable[str] = []
        :returns:
            Tuple[List[:sip:ref:`~PyQt6.QtCore.QUrl`], str]
        :static:
        :description: QtWidgets/QFileDialog-getOpenFileUrls-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.getSaveFileName
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
            caption: str = ''
            directory: str = ''
            filter: str = ''
            initialFilter: str = ''
            options: :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Options` = QFileDialog.Options()
        :returns:
            Tuple[str, str]
        :static:
        :description: QtWidgets/QFileDialog-getSaveFileName-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.getSaveFileUrl
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
            caption: str = ''
            directory: :sip:ref:`~PyQt6.QtCore.QUrl` = QUrl()
            filter: str = ''
            initialFilter: str = ''
            options: :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Options` = QFileDialog.Options()
            supportedSchemes: Iterable[str] = []
        :returns:
            Tuple[:sip:ref:`~PyQt6.QtCore.QUrl`, str]
        :static:
        :description: QtWidgets/QFileDialog-getSaveFileUrl-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.history
        :returns:
            List[str]
        :description: QtWidgets/QFileDialog-history-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.iconProvider
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAbstractFileIconProvider`
        :description: QtWidgets/QFileDialog-iconProvider-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.itemDelegate
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate`
        :description: QtWidgets/QFileDialog-itemDelegate-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.labelText
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QFileDialog.DialogLabel`
        :returns:
            str
        :description: QtWidgets/QFileDialog-labelText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.mimeTypeFilters
        :returns:
            List[str]
        :description: QtWidgets/QFileDialog-mimeTypeFilters-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.nameFilters
        :returns:
            List[str]
        :description: QtWidgets/QFileDialog-nameFilters-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.open
        :description: QtWidgets/QFileDialog-open-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.open
        :args:
            PYQT_SLOT
        :description: QtWidgets/QFileDialog-open-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.options
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Options`
        :description: QtWidgets/QFileDialog-options-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.proxyModel
        :returns:
            :sip:ref:`~PyQt6.QtCore.QAbstractProxyModel`
        :description: QtWidgets/QFileDialog-proxyModel-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.restoreState
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :returns:
            bool
        :description: QtWidgets/QFileDialog-restoreState-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.saveFileContent
        :args:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
            fileNameHint: str = ''
        :static:
        :description: QtWidgets/QFileDialog-saveFileContent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.saveState
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtWidgets/QFileDialog-saveState-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.selectedFiles
        :returns:
            List[str]
        :description: QtWidgets/QFileDialog-selectedFiles-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.selectedMimeTypeFilter
        :returns:
            str
        :description: QtWidgets/QFileDialog-selectedMimeTypeFilter-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.selectedNameFilter
        :returns:
            str
        :description: QtWidgets/QFileDialog-selectedNameFilter-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.selectedUrls
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QUrl`]
        :description: QtWidgets/QFileDialog-selectedUrls-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.selectFile
        :args:
            str
        :description: QtWidgets/QFileDialog-selectFile-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.selectMimeTypeFilter
        :args:
            str
        :description: QtWidgets/QFileDialog-selectMimeTypeFilter-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.selectNameFilter
        :args:
            str
        :description: QtWidgets/QFileDialog-selectNameFilter-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.selectUrl
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtWidgets/QFileDialog-selectUrl-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.setAcceptMode
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QFileDialog.AcceptMode`
        :description: QtWidgets/QFileDialog-setAcceptMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.setDefaultSuffix
        :args:
            str
        :description: QtWidgets/QFileDialog-setDefaultSuffix-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.setDirectory
        :args:
            str
        :description: QtWidgets/QFileDialog-setDirectory-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.setDirectory
        :args:
            :sip:ref:`~PyQt6.QtCore.QDir`
        :description: QtWidgets/QFileDialog-setDirectory-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.setDirectoryUrl
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtWidgets/QFileDialog-setDirectoryUrl-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.setFileMode
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QFileDialog.FileMode`
        :description: QtWidgets/QFileDialog-setFileMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.setFilter
        :args:
            :sip:ref:`~PyQt6.QtCore.QDir.Filters`
        :description: QtWidgets/QFileDialog-setFilter-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.setHistory
        :args:
            Iterable[str]
        :description: QtWidgets/QFileDialog-setHistory-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.setIconProvider
        :args:
            :sip:ref:`~PyQt6.QtGui.QAbstractFileIconProvider`
        :description: QtWidgets/QFileDialog-setIconProvider-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.setItemDelegate
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate`
        :description: QtWidgets/QFileDialog-setItemDelegate-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.setLabelText
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QFileDialog.DialogLabel`
            str
        :description: QtWidgets/QFileDialog-setLabelText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.setMimeTypeFilters
        :args:
            Iterable[str]
        :description: QtWidgets/QFileDialog-setMimeTypeFilters-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.setNameFilter
        :args:
            str
        :description: QtWidgets/QFileDialog-setNameFilter-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.setNameFilters
        :args:
            Iterable[str]
        :description: QtWidgets/QFileDialog-setNameFilters-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.setOption
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Options`
            on: bool = True
        :description: QtWidgets/QFileDialog-setOption-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.setOptions
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Options`
        :description: QtWidgets/QFileDialog-setOptions-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.setProxyModel
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractProxyModel`
        :description: QtWidgets/QFileDialog-setProxyModel-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.setSidebarUrls
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCore.QUrl`]
        :description: QtWidgets/QFileDialog-setSidebarUrls-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.setSupportedSchemes
        :args:
            Iterable[str]
        :description: QtWidgets/QFileDialog-setSupportedSchemes-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.setViewMode
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QFileDialog.ViewMode`
        :description: QtWidgets/QFileDialog-setViewMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.setVisible
        :args:
            bool
        :description: QtWidgets/QFileDialog-setVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.sidebarUrls
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QUrl`]
        :description: QtWidgets/QFileDialog-sidebarUrls-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.supportedSchemes
        :returns:
            List[str]
        :description: QtWidgets/QFileDialog-supportedSchemes-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.testOption
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QFileDialog.Options`
        :returns:
            bool
        :description: QtWidgets/QFileDialog-testOption-f.rst

    .. sip:method:: PyQt6.QtWidgets.QFileDialog.viewMode
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QFileDialog.ViewMode`
        :description: QtWidgets/QFileDialog-viewMode-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QFileDialog.currentChanged
        :args:
            str
        :description: QtWidgets/QFileDialog-currentChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QFileDialog.currentUrlChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtWidgets/QFileDialog-currentUrlChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QFileDialog.directoryEntered
        :args:
            str
        :description: QtWidgets/QFileDialog-directoryEntered-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QFileDialog.directoryUrlEntered
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtWidgets/QFileDialog-directoryUrlEntered-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QFileDialog.fileSelected
        :args:
            str
        :description: QtWidgets/QFileDialog-fileSelected-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QFileDialog.filesSelected
        :args:
            Iterable[str]
        :description: QtWidgets/QFileDialog-filesSelected-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QFileDialog.filterSelected
        :args:
            str
        :description: QtWidgets/QFileDialog-filterSelected-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QFileDialog.urlSelected
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtWidgets/QFileDialog-urlSelected-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QFileDialog.urlsSelected
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCore.QUrl`]
        :description: QtWidgets/QFileDialog-urlsSelected-s.rst
