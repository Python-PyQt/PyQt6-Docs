:orphan:

.. sip:class:: PyQt6.QtCore.QDir
    :description: QtCore/QDir-c.rst

    .. sip:enum:: PyQt6.QtCore.QDir.Filters
        :description: QtCore/QDir-Filters-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filters.AccessMask
            :description: QtCore/QDir-Filters-AccessMask-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filters.AllDirs
            :description: QtCore/QDir-Filters-AllDirs-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filters.AllEntries
            :description: QtCore/QDir-Filters-AllEntries-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filters.CaseSensitive
            :description: QtCore/QDir-Filters-CaseSensitive-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filters.Dirs
            :description: QtCore/QDir-Filters-Dirs-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filters.Drives
            :description: QtCore/QDir-Filters-Drives-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filters.Executable
            :description: QtCore/QDir-Filters-Executable-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filters.Files
            :description: QtCore/QDir-Filters-Files-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filters.Hidden
            :description: QtCore/QDir-Filters-Hidden-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filters.Modified
            :description: QtCore/QDir-Filters-Modified-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filters.NoDot
            :description: QtCore/QDir-Filters-NoDot-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filters.NoDotAndDotDot
            :description: QtCore/QDir-Filters-NoDotAndDotDot-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filters.NoDotDot
            :description: QtCore/QDir-Filters-NoDotDot-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filters.NoFilter
            :description: QtCore/QDir-Filters-NoFilter-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filters.NoSymLinks
            :description: QtCore/QDir-Filters-NoSymLinks-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filters.PermissionMask
            :description: QtCore/QDir-Filters-PermissionMask-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filters.Readable
            :description: QtCore/QDir-Filters-Readable-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filters.System
            :description: QtCore/QDir-Filters-System-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filters.TypeMask
            :description: QtCore/QDir-Filters-TypeMask-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filters.Writable
            :description: QtCore/QDir-Filters-Writable-v.rst

    .. sip:enum:: PyQt6.QtCore.QDir.SortFlags
        :description: QtCore/QDir-SortFlags-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.SortFlags.DirsFirst
            :description: QtCore/QDir-SortFlags-DirsFirst-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.SortFlags.DirsLast
            :description: QtCore/QDir-SortFlags-DirsLast-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.SortFlags.IgnoreCase
            :description: QtCore/QDir-SortFlags-IgnoreCase-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.SortFlags.LocaleAware
            :description: QtCore/QDir-SortFlags-LocaleAware-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.SortFlags.Name
            :description: QtCore/QDir-SortFlags-Name-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.SortFlags.NoSort
            :description: QtCore/QDir-SortFlags-NoSort-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.SortFlags.Reversed
            :description: QtCore/QDir-SortFlags-Reversed-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.SortFlags.Size
            :description: QtCore/QDir-SortFlags-Size-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.SortFlags.SortByMask
            :description: QtCore/QDir-SortFlags-SortByMask-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.SortFlags.Time
            :description: QtCore/QDir-SortFlags-Time-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.SortFlags.Type
            :description: QtCore/QDir-SortFlags-Type-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.SortFlags.Unsorted
            :description: QtCore/QDir-SortFlags-Unsorted-v.rst

    .. sip:method:: PyQt6.QtCore.QDir.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QDir`
        :description: QtCore/QDir-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.__init__
        :args:
            path: str = ''
        :description: QtCore/QDir-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.__init__
        :args:
            str
            str
            sort: :sip:ref:`~PyQt6.QtCore.QDir.SortFlags` = QDir.SortFlags(QDir.Name|QDir.IgnoreCase)
            filters: :sip:ref:`~PyQt6.QtCore.QDir.Filters` = :sip:ref:`~PyQt6.QtCore.QDir.Filters.AllEntries`
        :description: QtCore/QDir-__init__-f-2.rst

    .. sip:method:: PyQt6.QtCore.QDir.absoluteFilePath
        :args:
            str
        :returns:
            str
        :description: QtCore/QDir-absoluteFilePath-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.absolutePath
        :returns:
            str
        :description: QtCore/QDir-absolutePath-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.addSearchPath
        :args:
            str
            str
        :static:
        :description: QtCore/QDir-addSearchPath-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.canonicalPath
        :returns:
            str
        :description: QtCore/QDir-canonicalPath-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.cd
        :args:
            str
        :returns:
            bool
        :description: QtCore/QDir-cd-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.cdUp
        :returns:
            bool
        :description: QtCore/QDir-cdUp-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.cleanPath
        :args:
            str
        :returns:
            str
        :static:
        :description: QtCore/QDir-cleanPath-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.__contains__
        :args:
            str
        :returns:
            int
        :description: QtCore/QDir-__contains__-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.count
        :returns:
            int
        :description: QtCore/QDir-count-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.current
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDir`
        :static:
        :description: QtCore/QDir-current-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.currentPath
        :returns:
            str
        :static:
        :description: QtCore/QDir-currentPath-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.dirName
        :returns:
            str
        :description: QtCore/QDir-dirName-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.drives
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QFileInfo`]
        :static:
        :description: QtCore/QDir-drives-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.entryInfoList
        :args:
            filters: :sip:ref:`~PyQt6.QtCore.QDir.Filters` = :sip:ref:`~PyQt6.QtCore.QDir.Filters.NoFilter`
            sort: :sip:ref:`~PyQt6.QtCore.QDir.SortFlags` = :sip:ref:`~PyQt6.QtCore.QDir.SortFlags.NoSort`
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QFileInfo`]
        :description: QtCore/QDir-entryInfoList-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.entryInfoList
        :args:
            Iterable[str]
            filters: :sip:ref:`~PyQt6.QtCore.QDir.Filters` = :sip:ref:`~PyQt6.QtCore.QDir.Filters.NoFilter`
            sort: :sip:ref:`~PyQt6.QtCore.QDir.SortFlags` = :sip:ref:`~PyQt6.QtCore.QDir.SortFlags.NoSort`
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QFileInfo`]
        :description: QtCore/QDir-entryInfoList-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.entryList
        :args:
            filters: :sip:ref:`~PyQt6.QtCore.QDir.Filters` = :sip:ref:`~PyQt6.QtCore.QDir.Filters.NoFilter`
            sort: :sip:ref:`~PyQt6.QtCore.QDir.SortFlags` = :sip:ref:`~PyQt6.QtCore.QDir.SortFlags.NoSort`
        :returns:
            List[str]
        :description: QtCore/QDir-entryList-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.entryList
        :args:
            Iterable[str]
            filters: :sip:ref:`~PyQt6.QtCore.QDir.Filters` = :sip:ref:`~PyQt6.QtCore.QDir.Filters.NoFilter`
            sort: :sip:ref:`~PyQt6.QtCore.QDir.SortFlags` = :sip:ref:`~PyQt6.QtCore.QDir.SortFlags.NoSort`
        :returns:
            List[str]
        :description: QtCore/QDir-entryList-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.__eq__
        :args:
            :sip:ref:`~PyQt6.QtCore.QDir`
        :returns:
            bool
        :description: QtCore/QDir-__eq__-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.exists
        :returns:
            bool
        :description: QtCore/QDir-exists-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.exists
        :args:
            str
        :returns:
            bool
        :description: QtCore/QDir-exists-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.filePath
        :args:
            str
        :returns:
            str
        :description: QtCore/QDir-filePath-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.filter
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDir.Filters`
        :description: QtCore/QDir-filter-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.fromNativeSeparators
        :args:
            str
        :returns:
            str
        :static:
        :description: QtCore/QDir-fromNativeSeparators-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.__getitem__
        :args:
            int
        :returns:
            str
        :description: QtCore/QDir-__getitem__-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.__getitem__
        :args:
            slice
        :returns:
            List[str]
        :description: QtCore/QDir-__getitem__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.home
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDir`
        :static:
        :description: QtCore/QDir-home-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.homePath
        :returns:
            str
        :static:
        :description: QtCore/QDir-homePath-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.isAbsolute
        :returns:
            bool
        :description: QtCore/QDir-isAbsolute-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.isAbsolutePath
        :args:
            str
        :returns:
            bool
        :static:
        :description: QtCore/QDir-isAbsolutePath-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.isEmpty
        :args:
            filters: :sip:ref:`~PyQt6.QtCore.QDir.Filters` = QDir.Filters(QDir.AllEntries|QDir.NoDotAndDotDot)
        :returns:
            bool
        :description: QtCore/QDir-isEmpty-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.isReadable
        :returns:
            bool
        :description: QtCore/QDir-isReadable-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.isRelative
        :returns:
            bool
        :description: QtCore/QDir-isRelative-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.isRelativePath
        :args:
            str
        :returns:
            bool
        :static:
        :description: QtCore/QDir-isRelativePath-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.isRoot
        :returns:
            bool
        :description: QtCore/QDir-isRoot-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.__len__
        :returns:
            int
        :description: QtCore/QDir-__len__-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.listSeparator
        :returns:
            str
        :static:
        :description: QtCore/QDir-listSeparator-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.makeAbsolute
        :returns:
            bool
        :description: QtCore/QDir-makeAbsolute-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.match
        :args:
            Iterable[str]
            str
        :returns:
            bool
        :static:
        :description: QtCore/QDir-match-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.match
        :args:
            str
            str
        :returns:
            bool
        :static:
        :description: QtCore/QDir-match-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.mkdir
        :args:
            str
        :returns:
            bool
        :description: QtCore/QDir-mkdir-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.mkpath
        :args:
            str
        :returns:
            bool
        :description: QtCore/QDir-mkpath-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.nameFilters
        :returns:
            List[str]
        :description: QtCore/QDir-nameFilters-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.nameFiltersFromString
        :args:
            str
        :returns:
            List[str]
        :static:
        :description: QtCore/QDir-nameFiltersFromString-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.__ne__
        :args:
            :sip:ref:`~PyQt6.QtCore.QDir`
        :returns:
            bool
        :description: QtCore/QDir-__ne__-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.path
        :returns:
            str
        :description: QtCore/QDir-path-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.refresh
        :description: QtCore/QDir-refresh-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.relativeFilePath
        :args:
            str
        :returns:
            str
        :description: QtCore/QDir-relativeFilePath-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.remove
        :args:
            str
        :returns:
            bool
        :description: QtCore/QDir-remove-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.removeRecursively
        :returns:
            bool
        :description: QtCore/QDir-removeRecursively-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.rename
        :args:
            str
            str
        :returns:
            bool
        :description: QtCore/QDir-rename-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.rmdir
        :args:
            str
        :returns:
            bool
        :description: QtCore/QDir-rmdir-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.rmpath
        :args:
            str
        :returns:
            bool
        :description: QtCore/QDir-rmpath-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.root
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDir`
        :static:
        :description: QtCore/QDir-root-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.rootPath
        :returns:
            str
        :static:
        :description: QtCore/QDir-rootPath-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.searchPaths
        :args:
            str
        :returns:
            List[str]
        :static:
        :description: QtCore/QDir-searchPaths-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.separator
        :returns:
            str
        :static:
        :description: QtCore/QDir-separator-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.setCurrent
        :args:
            str
        :returns:
            bool
        :static:
        :description: QtCore/QDir-setCurrent-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.setFilter
        :args:
            :sip:ref:`~PyQt6.QtCore.QDir.Filters`
        :description: QtCore/QDir-setFilter-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.setNameFilters
        :args:
            Iterable[str]
        :description: QtCore/QDir-setNameFilters-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.setPath
        :args:
            str
        :description: QtCore/QDir-setPath-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.setSearchPaths
        :args:
            str
            Iterable[str]
        :static:
        :description: QtCore/QDir-setSearchPaths-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.setSorting
        :args:
            :sip:ref:`~PyQt6.QtCore.QDir.SortFlags`
        :description: QtCore/QDir-setSorting-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.sorting
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDir.SortFlags`
        :description: QtCore/QDir-sorting-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.swap
        :args:
            :sip:ref:`~PyQt6.QtCore.QDir`
        :description: QtCore/QDir-swap-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.temp
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDir`
        :static:
        :description: QtCore/QDir-temp-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.tempPath
        :returns:
            str
        :static:
        :description: QtCore/QDir-tempPath-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.toNativeSeparators
        :args:
            str
        :returns:
            str
        :static:
        :description: QtCore/QDir-toNativeSeparators-f.rst
