:orphan:

.. sip:class:: PyQt6.QtDesigner.QDesignerFormWindowInterface
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QWidget`
    :description: QtDesigner/QDesignerFormWindowInterface-c.rst

    .. sip:enum:: PyQt6.QtDesigner.QDesignerFormWindowInterface.FeatureFlag
        :description: QtDesigner/QDesignerFormWindowInterface-FeatureFlag-e.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowInterface.FeatureFlag.DefaultFeature
            :description: QtDesigner/QDesignerFormWindowInterface-FeatureFlag-DefaultFeature-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowInterface.FeatureFlag.EditFeature
            :description: QtDesigner/QDesignerFormWindowInterface-FeatureFlag-EditFeature-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowInterface.FeatureFlag.GridFeature
            :description: QtDesigner/QDesignerFormWindowInterface-FeatureFlag-GridFeature-v.rst

        .. sip:enum-member:: PyQt6.QtDesigner.QDesignerFormWindowInterface.FeatureFlag.TabOrderFeature
            :description: QtDesigner/QDesignerFormWindowInterface-FeatureFlag-TabOrderFeature-v.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
            flags: :sip:ref:`~PyQt6.QtCore.Qt.WindowType` = {}
        :description: QtDesigner/QDesignerFormWindowInterface-__init__-f-1.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.absoluteDir
        :returns:
            :sip:ref:`~PyQt6.QtCore.QDir`
        :description: QtDesigner/QDesignerFormWindowInterface-absoluteDir-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.activateResourceFilePaths
        :args:
            Iterable[str]
        :returns:
            int
            str
        :description: QtDesigner/QDesignerFormWindowInterface-activateResourceFilePaths-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.activeResourceFilePaths
        :returns:
            List[str]
        :description: QtDesigner/QDesignerFormWindowInterface-activeResourceFilePaths-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.addResourceFile
        :args:
            str
        :description: QtDesigner/QDesignerFormWindowInterface-addResourceFile-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.author
        :returns:
            str
        :description: QtDesigner/QDesignerFormWindowInterface-author-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.checkContents
        :returns:
            List[str]
        :description: QtDesigner/QDesignerFormWindowInterface-checkContents-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.clearSelection
        :args:
            update: bool = True
        :description: QtDesigner/QDesignerFormWindowInterface-clearSelection-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.comment
        :returns:
            str
        :description: QtDesigner/QDesignerFormWindowInterface-comment-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.contents
        :returns:
            str
        :description: QtDesigner/QDesignerFormWindowInterface-contents-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.core
        :returns:
            :sip:ref:`~PyQt6.QtDesigner.QDesignerFormEditorInterface`
        :description: QtDesigner/QDesignerFormWindowInterface-core-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.cursor
        :returns:
            :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowCursorInterface`
        :description: QtDesigner/QDesignerFormWindowInterface-cursor-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.emitSelectionChanged
        :description: QtDesigner/QDesignerFormWindowInterface-emitSelectionChanged-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.exportMacro
        :returns:
            str
        :description: QtDesigner/QDesignerFormWindowInterface-exportMacro-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.features
        :returns:
            :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.FeatureFlag`
        :description: QtDesigner/QDesignerFormWindowInterface-features-f-1.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.fileName
        :returns:
            str
        :description: QtDesigner/QDesignerFormWindowInterface-fileName-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.findFormWindow
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :returns:
            :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface`
        :static:
        :description: QtDesigner/QDesignerFormWindowInterface-findFormWindow-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.findFormWindow
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :returns:
            :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface`
        :static:
        :description: QtDesigner/QDesignerFormWindowInterface-findFormWindow-f-1.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.formContainer
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtDesigner/QDesignerFormWindowInterface-formContainer-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.grid
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtDesigner/QDesignerFormWindowInterface-grid-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.hasFeature
        :args:
            :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.FeatureFlag`
        :returns:
            bool
        :description: QtDesigner/QDesignerFormWindowInterface-hasFeature-f-1.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.includeHints
        :returns:
            List[str]
        :description: QtDesigner/QDesignerFormWindowInterface-includeHints-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.isDirty
        :returns:
            bool
        :description: QtDesigner/QDesignerFormWindowInterface-isDirty-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.isManaged
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :returns:
            bool
        :description: QtDesigner/QDesignerFormWindowInterface-isManaged-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.layoutDefault
        :returns:
            int
            int
        :description: QtDesigner/QDesignerFormWindowInterface-layoutDefault-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.layoutFunction
        :returns:
            str
            str
        :description: QtDesigner/QDesignerFormWindowInterface-layoutFunction-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.mainContainer
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtDesigner/QDesignerFormWindowInterface-mainContainer-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.manageWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtDesigner/QDesignerFormWindowInterface-manageWidget-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.pixmapFunction
        :returns:
            str
        :description: QtDesigner/QDesignerFormWindowInterface-pixmapFunction-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.removeResourceFile
        :args:
            str
        :description: QtDesigner/QDesignerFormWindowInterface-removeResourceFile-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.resourceFiles
        :returns:
            List[str]
        :description: QtDesigner/QDesignerFormWindowInterface-resourceFiles-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.selectWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            select: bool = True
        :description: QtDesigner/QDesignerFormWindowInterface-selectWidget-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.setAuthor
        :args:
            str
        :description: QtDesigner/QDesignerFormWindowInterface-setAuthor-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.setComment
        :args:
            str
        :description: QtDesigner/QDesignerFormWindowInterface-setComment-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.setContents
        :args:
            str
        :returns:
            bool
        :description: QtDesigner/QDesignerFormWindowInterface-setContents-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.setContents
        :args:
            :sip:ref:`~PyQt6.QtCore.QIODevice`
            errorMessage: str = ''
        :returns:
            bool
        :description: QtDesigner/QDesignerFormWindowInterface-setContents-f-1.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.setDirty
        :args:
            bool
        :description: QtDesigner/QDesignerFormWindowInterface-setDirty-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.setExportMacro
        :args:
            str
        :description: QtDesigner/QDesignerFormWindowInterface-setExportMacro-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.setFeatures
        :args:
            :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.FeatureFlag`
        :description: QtDesigner/QDesignerFormWindowInterface-setFeatures-f-1.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.setFileName
        :args:
            str
        :description: QtDesigner/QDesignerFormWindowInterface-setFileName-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.setGrid
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtDesigner/QDesignerFormWindowInterface-setGrid-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.setIncludeHints
        :args:
            Iterable[str]
        :description: QtDesigner/QDesignerFormWindowInterface-setIncludeHints-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.setLayoutDefault
        :args:
            int
            int
        :description: QtDesigner/QDesignerFormWindowInterface-setLayoutDefault-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.setLayoutFunction
        :args:
            str
            str
        :description: QtDesigner/QDesignerFormWindowInterface-setLayoutFunction-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.setMainContainer
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtDesigner/QDesignerFormWindowInterface-setMainContainer-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.setPixmapFunction
        :args:
            str
        :description: QtDesigner/QDesignerFormWindowInterface-setPixmapFunction-f.rst

    .. sip:method:: PyQt6.QtDesigner.QDesignerFormWindowInterface.unmanageWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtDesigner/QDesignerFormWindowInterface-unmanageWidget-f.rst

    .. sip:signal:: PyQt6.QtDesigner.QDesignerFormWindowInterface.aboutToUnmanageWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtDesigner/QDesignerFormWindowInterface-aboutToUnmanageWidget-s.rst

    .. sip:signal:: PyQt6.QtDesigner.QDesignerFormWindowInterface.activated
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtDesigner/QDesignerFormWindowInterface-activated-s.rst

    .. sip:signal:: PyQt6.QtDesigner.QDesignerFormWindowInterface.changed
        :description: QtDesigner/QDesignerFormWindowInterface-changed-s.rst

    .. sip:signal:: PyQt6.QtDesigner.QDesignerFormWindowInterface.featureChanged
        :args:
            :sip:ref:`~PyQt6.QtDesigner.QDesignerFormWindowInterface.FeatureFlag`
        :description: QtDesigner/QDesignerFormWindowInterface-featureChanged-s-1.rst

    .. sip:signal:: PyQt6.QtDesigner.QDesignerFormWindowInterface.fileNameChanged
        :args:
            str
        :description: QtDesigner/QDesignerFormWindowInterface-fileNameChanged-s.rst

    .. sip:signal:: PyQt6.QtDesigner.QDesignerFormWindowInterface.geometryChanged
        :description: QtDesigner/QDesignerFormWindowInterface-geometryChanged-s.rst

    .. sip:signal:: PyQt6.QtDesigner.QDesignerFormWindowInterface.mainContainerChanged
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtDesigner/QDesignerFormWindowInterface-mainContainerChanged-s.rst

    .. sip:signal:: PyQt6.QtDesigner.QDesignerFormWindowInterface.objectRemoved
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtDesigner/QDesignerFormWindowInterface-objectRemoved-s.rst

    .. sip:signal:: PyQt6.QtDesigner.QDesignerFormWindowInterface.resourceFilesChanged
        :description: QtDesigner/QDesignerFormWindowInterface-resourceFilesChanged-s.rst

    .. sip:signal:: PyQt6.QtDesigner.QDesignerFormWindowInterface.selectionChanged
        :description: QtDesigner/QDesignerFormWindowInterface-selectionChanged-s.rst

    .. sip:signal:: PyQt6.QtDesigner.QDesignerFormWindowInterface.widgetManaged
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtDesigner/QDesignerFormWindowInterface-widgetManaged-s.rst

    .. sip:signal:: PyQt6.QtDesigner.QDesignerFormWindowInterface.widgetRemoved
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtDesigner/QDesignerFormWindowInterface-widgetRemoved-s.rst

    .. sip:signal:: PyQt6.QtDesigner.QDesignerFormWindowInterface.widgetUnmanaged
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtDesigner/QDesignerFormWindowInterface-widgetUnmanaged-s.rst
