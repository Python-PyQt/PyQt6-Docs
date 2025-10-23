:orphan:

.. sip:class:: PyQt6.QtCore.QDir
    :description: QtCore/QDir-c.rst

    .. sip:enum:: PyQt6.QtCore.QDir.Filter
        :description: QtCore/QDir-Filter-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filter.AccessMask
            :description: QtCore/QDir-Filter-AccessMask-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filter.AllDirs
            :description: QtCore/QDir-Filter-AllDirs-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filter.AllEntries
            :description: QtCore/QDir-Filter-AllEntries-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filter.CaseSensitive
            :description: QtCore/QDir-Filter-CaseSensitive-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filter.Dirs
            :description: QtCore/QDir-Filter-Dirs-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filter.Drives
            :description: QtCore/QDir-Filter-Drives-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filter.Executable
            :description: QtCore/QDir-Filter-Executable-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filter.Files
            :description: QtCore/QDir-Filter-Files-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filter.Hidden
            :description: QtCore/QDir-Filter-Hidden-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filter.Modified
            :description: QtCore/QDir-Filter-Modified-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filter.NoDot
            :description: QtCore/QDir-Filter-NoDot-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filter.NoDotAndDotDot
            :description: QtCore/QDir-Filter-NoDotAndDotDot-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filter.NoDotDot
            :description: QtCore/QDir-Filter-NoDotDot-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filter.NoFilter
            :description: QtCore/QDir-Filter-NoFilter-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filter.NoSymLinks
            :description: QtCore/QDir-Filter-NoSymLinks-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filter.PermissionMask
            :description: QtCore/QDir-Filter-PermissionMask-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filter.Readable
            :description: QtCore/QDir-Filter-Readable-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filter.System
            :description: QtCore/QDir-Filter-System-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filter.TypeMask
            :description: QtCore/QDir-Filter-TypeMask-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.Filter.Writable
            :description: QtCore/QDir-Filter-Writable-v.rst

    .. sip:enum:: PyQt6.QtCore.QDir.SortFlag
        :description: QtCore/QDir-SortFlag-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.SortFlag.DirsFirst
            :description: QtCore/QDir-SortFlag-DirsFirst-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.SortFlag.DirsLast
            :description: QtCore/QDir-SortFlag-DirsLast-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.SortFlag.IgnoreCase
            :description: QtCore/QDir-SortFlag-IgnoreCase-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.SortFlag.LocaleAware
            :description: QtCore/QDir-SortFlag-LocaleAware-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.SortFlag.Name
            :description: QtCore/QDir-SortFlag-Name-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.SortFlag.NoSort
            :description: QtCore/QDir-SortFlag-NoSort-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.SortFlag.Reversed
            :description: QtCore/QDir-SortFlag-Reversed-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.SortFlag.Size
            :description: QtCore/QDir-SortFlag-Size-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.SortFlag.SortByMask
            :description: QtCore/QDir-SortFlag-SortByMask-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.SortFlag.Time
            :description: QtCore/QDir-SortFlag-Time-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.SortFlag.Type
            :description: QtCore/QDir-SortFlag-Type-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QDir.SortFlag.Unsorted
            :description: QtCore/QDir-SortFlag-Unsorted-v.rst

    .. sip:method:: PyQt6.QtCore.QDir.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QDir`
        :description: QtCore/QDir-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.__init__
        :args:
            path: Optional[str] = ''
        :description: QtCore/QDir-__init__-f-4.rst

    .. sip:method:: PyQt6.QtCore.QDir.__init__
        :args:
            Optional[str]
            Optional[str]
            sort: :sip:ref:`~PyQt6.QtCore.QDir.SortFlag` = QDir.SortFlags(QDir.Name|QDir.IgnoreCase)
            filters: :sip:ref:`~PyQt6.QtCore.QDir.Filter` = :sip:ref:`~PyQt6.QtCore.QDir.Filter.AllEntries`
        :description: QtCore/QDir-__init__-f-5.rst

    .. sip:method:: PyQt6.QtCore.QDir.absoluteFilePath
        :args:
            Optional[str]
        :returns:
            str
        :description: QtCore/QDir-absoluteFilePath-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.absolutePath
        :returns:
            str
        :description: QtCore/QDir-absolutePath-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.addSearchPath
        :args:
            Optional[str]
            Optional[str]
        :static:
        :description: QtCore/QDir-addSearchPath-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.canonicalPath
        :returns:
            str
        :description: QtCore/QDir-canonicalPath-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.cd
        :args:
            Optional[str]
        :returns:
            bool
        :description: QtCore/QDir-cd-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.cdUp
        :returns:
            bool
        :description: QtCore/QDir-cdUp-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.cleanPath
        :args:
            Optional[str]
        :returns:
            str
        :static:
        :description: QtCore/QDir-cleanPath-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.__contains__
        :args:
            Optional[str]
        :returns:
            int
        :description: QtCore/QDir-__contains__-f-1.rst

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
            list[:sip:ref:`~PyQt6.QtCore.QFileInfo`]
        :static:
        :description: QtCore/QDir-drives-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.entryInfoList
        :args:
            filters: :sip:ref:`~PyQt6.QtCore.QDir.Filter` = :sip:ref:`~PyQt6.QtCore.QDir.Filter.NoFilter`
            sort: :sip:ref:`~PyQt6.QtCore.QDir.SortFlag` = :sip:ref:`~PyQt6.QtCore.QDir.SortFlag.NoSort`
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QFileInfo`]
        :description: QtCore/QDir-entryInfoList-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.entryInfoList
        :args:
            Iterable[Optional[str]]
            filters: :sip:ref:`~PyQt6.QtCore.QDir.Filter` = :sip:ref:`~PyQt6.QtCore.QDir.Filter.NoFilter`
            sort: :sip:ref:`~PyQt6.QtCore.QDir.SortFlag` = :sip:ref:`~PyQt6.QtCore.QDir.SortFlag.NoSort`
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QFileInfo`]
        :description: QtCore/QDir-entryInfoList-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.entryList
        :args:
            filters: :sip:ref:`~PyQt6.QtCore.QDir.Filter` = :sip:ref:`~PyQt6.QtCore.QDir.Filter.NoFilter`
            sort: :sip:ref:`~PyQt6.QtCore.QDir.SortFlag` = :sip:ref:`~PyQt6.QtCore.QDir.SortFlag.NoSort`
        :returns:
            list[str]
        :description: QtCore/QDir-entryList-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.entryList
        :args:
            Iterable[Optional[str]]
            filters: :sip:ref:`~PyQt6.QtCore.QDir.Filter` = :sip:ref:`~PyQt6.QtCore.QDir.Filter.NoFilter`
            sort: :sip:ref:`~PyQt6.QtCore.QDir.SortFlag` = :sip:ref:`~PyQt6.QtCore.QDir.SortFlag.NoSort`
        :returns:
            list[str]
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
            Optional[str]
        :returns:
            bool
        :description: QtCore/QDir-exists-f-2.rst

    .. sip:method:: PyQt6.QtCore.QDir.filePath
        :args:
            Optional[str]
        :returns:
            str
        :description: QtCore/QDir-filePath-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.filter
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDir.Filter`
        :description: QtCore/QDir-filter-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.fromNativeSeparators
        :args:
            Optional[str]
        :returns:
            str
        :static:
        :description: QtCore/QDir-fromNativeSeparators-f-1.rst

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
            list[str]
        :description: QtCore/QDir-__getitem__-f-2.rst

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
            Optional[str]
        :returns:
            bool
        :static:
        :description: QtCore/QDir-isAbsolutePath-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.isEmpty
        :args:
            filters: :sip:ref:`~PyQt6.QtCore.QDir.Filter` = QDir.Filters(QDir.AllEntries|QDir.NoDotAndDotDot)
        :returns:
            bool
        :description: QtCore/QDir-isEmpty-f-1.rst

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
            Optional[str]
        :returns:
            bool
        :static:
        :description: QtCore/QDir-isRelativePath-f-1.rst

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
            Iterable[Optional[str]]
            Optional[str]
        :returns:
            bool
        :static:
        :description: QtCore/QDir-match-f-2.rst

    .. sip:method:: PyQt6.QtCore.QDir.match
        :args:
            Optional[str]
            Optional[str]
        :returns:
            bool
        :static:
        :description: QtCore/QDir-match-f-3.rst

    .. sip:method:: PyQt6.QtCore.QDir.mkdir
        :args:
            Optional[str]
        :returns:
            bool
        :description: QtCore/QDir-mkdir-f-2.rst

    .. sip:method:: PyQt6.QtCore.QDir.mkdir
        :args:
            Optional[str]
            :sip:ref:`~PyQt6.QtCore.QFileDevice.Permission`
        :returns:
            bool
        :description: QtCore/QDir-mkdir-f-3.rst

    .. sip:method:: PyQt6.QtCore.QDir.mkpath
        :args:
            Optional[str]
        :returns:
            bool
        :description: QtCore/QDir-mkpath-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.mkpath
        :args:
            Optional[str]
            :sip:ref:`~PyQt6.QtCore.QFileDevice.Permission`
        :returns:
            bool
        :description: QtCore/QDir-mkpath-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.nameFilters
        :returns:
            list[str]
        :description: QtCore/QDir-nameFilters-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.nameFiltersFromString
        :args:
            Optional[str]
        :returns:
            list[str]
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
            Optional[str]
        :returns:
            str
        :description: QtCore/QDir-relativeFilePath-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.remove
        :args:
            Optional[str]
        :returns:
            bool
        :description: QtCore/QDir-remove-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.removeRecursively
        :returns:
            bool
        :description: QtCore/QDir-removeRecursively-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.rename
        :args:
            Optional[str]
            Optional[str]
        :returns:
            bool
        :description: QtCore/QDir-rename-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.rmdir
        :args:
            Optional[str]
        :returns:
            bool
        :description: QtCore/QDir-rmdir-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.rmpath
        :args:
            Optional[str]
        :returns:
            bool
        :description: QtCore/QDir-rmpath-f-1.rst

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
            Optional[str]
        :returns:
            list[str]
        :static:
        :description: QtCore/QDir-searchPaths-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.separator
        :returns:
            str
        :static:
        :description: QtCore/QDir-separator-f.rst

    .. sip:method:: PyQt6.QtCore.QDir.setCurrent
        :args:
            Optional[str]
        :returns:
            bool
        :static:
        :description: QtCore/QDir-setCurrent-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.setFilter
        :args:
            :sip:ref:`~PyQt6.QtCore.QDir.Filter`
        :description: QtCore/QDir-setFilter-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.setNameFilters
        :args:
            Iterable[Optional[str]]
        :description: QtCore/QDir-setNameFilters-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.setPath
        :args:
            Optional[str]
        :description: QtCore/QDir-setPath-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.setSearchPaths
        :args:
            Optional[str]
            Iterable[Optional[str]]
        :static:
        :description: QtCore/QDir-setSearchPaths-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.setSorting
        :args:
            :sip:ref:`~PyQt6.QtCore.QDir.SortFlag`
        :description: QtCore/QDir-setSorting-f-1.rst

    .. sip:method:: PyQt6.QtCore.QDir.sorting
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDir.SortFlag`
        :description: QtCore/QDir-sorting-f-1.rst

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
            Optional[str]
        :returns:
            str
        :static:
        :description: QtCore/QDir-toNativeSeparators-f-1.rst
