:orphan:

.. sip:class:: PyQt6.QtCore.QStandardPaths
    :description: QtCore/QStandardPaths-c.rst

    .. sip:enum:: PyQt6.QtCore.QStandardPaths.LocateOption
        :description: QtCore/QStandardPaths-LocateOption-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QStandardPaths.LocateOption.LocateDirectory
            :description: QtCore/QStandardPaths-LocateOption-LocateDirectory-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QStandardPaths.LocateOption.LocateFile
            :description: QtCore/QStandardPaths-LocateOption-LocateFile-v.rst

    .. sip:enum:: PyQt6.QtCore.QStandardPaths.StandardLocation
        :description: QtCore/QStandardPaths-StandardLocation-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QStandardPaths.StandardLocation.AppConfigLocation
            :description: QtCore/QStandardPaths-StandardLocation-AppConfigLocation-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QStandardPaths.StandardLocation.AppDataLocation
            :description: QtCore/QStandardPaths-StandardLocation-AppDataLocation-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QStandardPaths.StandardLocation.ApplicationsLocation
            :description: QtCore/QStandardPaths-StandardLocation-ApplicationsLocation-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QStandardPaths.StandardLocation.AppLocalDataLocation
            :description: QtCore/QStandardPaths-StandardLocation-AppLocalDataLocation-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QStandardPaths.StandardLocation.CacheLocation
            :description: QtCore/QStandardPaths-StandardLocation-CacheLocation-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QStandardPaths.StandardLocation.ConfigLocation
            :description: QtCore/QStandardPaths-StandardLocation-ConfigLocation-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QStandardPaths.StandardLocation.DesktopLocation
            :description: QtCore/QStandardPaths-StandardLocation-DesktopLocation-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QStandardPaths.StandardLocation.DocumentsLocation
            :description: QtCore/QStandardPaths-StandardLocation-DocumentsLocation-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QStandardPaths.StandardLocation.DownloadLocation
            :description: QtCore/QStandardPaths-StandardLocation-DownloadLocation-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QStandardPaths.StandardLocation.FontsLocation
            :description: QtCore/QStandardPaths-StandardLocation-FontsLocation-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QStandardPaths.StandardLocation.GenericCacheLocation
            :description: QtCore/QStandardPaths-StandardLocation-GenericCacheLocation-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QStandardPaths.StandardLocation.GenericConfigLocation
            :description: QtCore/QStandardPaths-StandardLocation-GenericConfigLocation-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QStandardPaths.StandardLocation.GenericDataLocation
            :description: QtCore/QStandardPaths-StandardLocation-GenericDataLocation-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QStandardPaths.StandardLocation.HomeLocation
            :description: QtCore/QStandardPaths-StandardLocation-HomeLocation-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QStandardPaths.StandardLocation.MoviesLocation
            :description: QtCore/QStandardPaths-StandardLocation-MoviesLocation-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QStandardPaths.StandardLocation.MusicLocation
            :description: QtCore/QStandardPaths-StandardLocation-MusicLocation-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QStandardPaths.StandardLocation.PicturesLocation
            :description: QtCore/QStandardPaths-StandardLocation-PicturesLocation-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QStandardPaths.StandardLocation.PublicShareLocation
            :description: QtCore/QStandardPaths-StandardLocation-PublicShareLocation-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QStandardPaths.StandardLocation.RuntimeLocation
            :description: QtCore/QStandardPaths-StandardLocation-RuntimeLocation-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QStandardPaths.StandardLocation.TemplatesLocation
            :description: QtCore/QStandardPaths-StandardLocation-TemplatesLocation-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QStandardPaths.StandardLocation.TempLocation
            :description: QtCore/QStandardPaths-StandardLocation-TempLocation-v.rst

    .. sip:method:: PyQt6.QtCore.QStandardPaths.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QStandardPaths`
        :description: QtCore/QStandardPaths-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QStandardPaths.displayName
        :args:
            :sip:ref:`~PyQt6.QtCore.QStandardPaths.StandardLocation`
        :returns:
            str
        :static:
        :description: QtCore/QStandardPaths-displayName-f.rst

    .. sip:method:: PyQt6.QtCore.QStandardPaths.findExecutable
        :args:
            Optional[str]
            paths: Iterable[Optional[str]] = []
        :returns:
            str
        :static:
        :description: QtCore/QStandardPaths-findExecutable-f-1.rst

    .. sip:method:: PyQt6.QtCore.QStandardPaths.locate
        :args:
            :sip:ref:`~PyQt6.QtCore.QStandardPaths.StandardLocation`
            Optional[str]
            options: :sip:ref:`~PyQt6.QtCore.QStandardPaths.LocateOption` = :sip:ref:`~PyQt6.QtCore.QStandardPaths.LocateOption.LocateFile`
        :returns:
            str
        :static:
        :description: QtCore/QStandardPaths-locate-f-2.rst

    .. sip:method:: PyQt6.QtCore.QStandardPaths.locateAll
        :args:
            :sip:ref:`~PyQt6.QtCore.QStandardPaths.StandardLocation`
            Optional[str]
            options: :sip:ref:`~PyQt6.QtCore.QStandardPaths.LocateOption` = :sip:ref:`~PyQt6.QtCore.QStandardPaths.LocateOption.LocateFile`
        :returns:
            List[str]
        :static:
        :description: QtCore/QStandardPaths-locateAll-f-2.rst

    .. sip:method:: PyQt6.QtCore.QStandardPaths.setTestModeEnabled
        :args:
            bool
        :static:
        :description: QtCore/QStandardPaths-setTestModeEnabled-f.rst

    .. sip:method:: PyQt6.QtCore.QStandardPaths.standardLocations
        :args:
            :sip:ref:`~PyQt6.QtCore.QStandardPaths.StandardLocation`
        :returns:
            List[str]
        :static:
        :description: QtCore/QStandardPaths-standardLocations-f.rst

    .. sip:method:: PyQt6.QtCore.QStandardPaths.writableLocation
        :args:
            :sip:ref:`~PyQt6.QtCore.QStandardPaths.StandardLocation`
        :returns:
            str
        :static:
        :description: QtCore/QStandardPaths-writableLocation-f.rst
