:orphan:

.. sip:class:: PyQt6.QtWidgets.QHeaderView
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView`
    :description: QtWidgets/QHeaderView-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QHeaderView.ResizeMode
        :description: QtWidgets/QHeaderView-ResizeMode-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QHeaderView.ResizeMode.Custom
            :description: QtWidgets/QHeaderView-ResizeMode-Custom-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QHeaderView.ResizeMode.Fixed
            :description: QtWidgets/QHeaderView-ResizeMode-Fixed-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QHeaderView.ResizeMode.Interactive
            :description: QtWidgets/QHeaderView-ResizeMode-Interactive-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QHeaderView.ResizeMode.ResizeToContents
            :description: QtWidgets/QHeaderView-ResizeMode-ResizeToContents-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QHeaderView.ResizeMode.Stretch
            :description: QtWidgets/QHeaderView-ResizeMode-Stretch-v.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QHeaderView-__init__-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.cascadingSectionResizes
        :returns:
            bool
        :description: QtWidgets/QHeaderView-cascadingSectionResizes-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.count
        :returns:
            int
        :description: QtWidgets/QHeaderView-count-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.currentChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QHeaderView-currentChanged-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.dataChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            roles: Iterable[int] = []
        :description: QtWidgets/QHeaderView-dataChanged-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.defaultAlignment
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag`
        :description: QtWidgets/QHeaderView-defaultAlignment-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.defaultSectionSize
        :returns:
            int
        :description: QtWidgets/QHeaderView-defaultSectionSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QHeaderView-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.headerDataChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
            int
            int
        :description: QtWidgets/QHeaderView-headerDataChanged-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.hiddenSectionCount
        :returns:
            int
        :description: QtWidgets/QHeaderView-hiddenSectionCount-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.hideSection
        :args:
            int
        :description: QtWidgets/QHeaderView-hideSection-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.highlightSections
        :returns:
            bool
        :description: QtWidgets/QHeaderView-highlightSections-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.horizontalOffset
        :returns:
            int
        :description: QtWidgets/QHeaderView-horizontalOffset-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.indexAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QHeaderView-indexAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.initialize
        :description: QtWidgets/QHeaderView-initialize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.initializeSections
        :description: QtWidgets/QHeaderView-initializeSections-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.initializeSections
        :args:
            int
            int
        :description: QtWidgets/QHeaderView-initializeSections-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.initStyleOption
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionHeader`
        :description: QtWidgets/QHeaderView-initStyleOption-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.initStyleOptionForIndex
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionHeader`
            int
        :description: QtWidgets/QHeaderView-initStyleOptionForIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.isFirstSectionMovable
        :returns:
            bool
        :description: QtWidgets/QHeaderView-isFirstSectionMovable-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.isIndexHidden
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtWidgets/QHeaderView-isIndexHidden-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.isSectionHidden
        :args:
            int
        :returns:
            bool
        :description: QtWidgets/QHeaderView-isSectionHidden-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.isSortIndicatorClearable
        :returns:
            bool
        :description: QtWidgets/QHeaderView-isSortIndicatorClearable-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.isSortIndicatorShown
        :returns:
            bool
        :description: QtWidgets/QHeaderView-isSortIndicatorShown-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.__len__
        :returns:
            int
        :description: QtWidgets/QHeaderView-__len__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.length
        :returns:
            int
        :description: QtWidgets/QHeaderView-length-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.logicalIndex
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QHeaderView-logicalIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.logicalIndexAt
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QHeaderView-logicalIndexAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.logicalIndexAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            int
        :description: QtWidgets/QHeaderView-logicalIndexAt-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.logicalIndexAt
        :args:
            int
            int
        :returns:
            int
        :description: QtWidgets/QHeaderView-logicalIndexAt-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.maximumSectionSize
        :returns:
            int
        :description: QtWidgets/QHeaderView-maximumSectionSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.minimumSectionSize
        :returns:
            int
        :description: QtWidgets/QHeaderView-minimumSectionSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.mouseDoubleClickEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QHeaderView-mouseDoubleClickEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.mouseMoveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QHeaderView-mouseMoveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.mousePressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QHeaderView-mousePressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.mouseReleaseEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QHeaderView-mouseReleaseEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.moveCursor
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.CursorAction`
            :sip:ref:`~PyQt6.QtCore.Qt.KeyboardModifier`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QHeaderView-moveCursor-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.moveSection
        :args:
            int
            int
        :description: QtWidgets/QHeaderView-moveSection-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.offset
        :returns:
            int
        :description: QtWidgets/QHeaderView-offset-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.orientation
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
        :description: QtWidgets/QHeaderView-orientation-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.paintEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QPaintEvent`
        :description: QtWidgets/QHeaderView-paintEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.paintSection
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtCore.QRect`
            int
        :description: QtWidgets/QHeaderView-paintSection-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.reset
        :description: QtWidgets/QHeaderView-reset-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.resetDefaultSectionSize
        :description: QtWidgets/QHeaderView-resetDefaultSectionSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.resizeContentsPrecision
        :returns:
            int
        :description: QtWidgets/QHeaderView-resizeContentsPrecision-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.resizeSection
        :args:
            int
            int
        :description: QtWidgets/QHeaderView-resizeSection-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.resizeSections
        :description: QtWidgets/QHeaderView-resizeSections-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.resizeSections
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QHeaderView.ResizeMode`
        :description: QtWidgets/QHeaderView-resizeSections-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.restoreState
        :args:
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :returns:
            bool
        :description: QtWidgets/QHeaderView-restoreState-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.rowsInserted
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtWidgets/QHeaderView-rowsInserted-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.saveState
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtWidgets/QHeaderView-saveState-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.scrollContentsBy
        :args:
            int
            int
        :description: QtWidgets/QHeaderView-scrollContentsBy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.scrollTo
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.ScrollHint`
        :description: QtWidgets/QHeaderView-scrollTo-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.sectionPosition
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QHeaderView-sectionPosition-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.sectionResizeMode
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QHeaderView.ResizeMode`
        :description: QtWidgets/QHeaderView-sectionResizeMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.sectionsAboutToBeRemoved
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtWidgets/QHeaderView-sectionsAboutToBeRemoved-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.sectionsClickable
        :returns:
            bool
        :description: QtWidgets/QHeaderView-sectionsClickable-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.sectionsHidden
        :returns:
            bool
        :description: QtWidgets/QHeaderView-sectionsHidden-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.sectionsInserted
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
        :description: QtWidgets/QHeaderView-sectionsInserted-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.sectionSize
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QHeaderView-sectionSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.sectionSizeFromContents
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QHeaderView-sectionSizeFromContents-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.sectionSizeHint
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QHeaderView-sectionSizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.sectionsMovable
        :returns:
            bool
        :description: QtWidgets/QHeaderView-sectionsMovable-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.sectionsMoved
        :returns:
            bool
        :description: QtWidgets/QHeaderView-sectionsMoved-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.sectionViewportPosition
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QHeaderView-sectionViewportPosition-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.setCascadingSectionResizes
        :args:
            bool
        :description: QtWidgets/QHeaderView-setCascadingSectionResizes-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.setDefaultAlignment
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag`
        :description: QtWidgets/QHeaderView-setDefaultAlignment-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.setDefaultSectionSize
        :args:
            int
        :description: QtWidgets/QHeaderView-setDefaultSectionSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.setFirstSectionMovable
        :args:
            bool
        :description: QtWidgets/QHeaderView-setFirstSectionMovable-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.setHighlightSections
        :args:
            bool
        :description: QtWidgets/QHeaderView-setHighlightSections-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.setMaximumSectionSize
        :args:
            int
        :description: QtWidgets/QHeaderView-setMaximumSectionSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.setMinimumSectionSize
        :args:
            int
        :description: QtWidgets/QHeaderView-setMinimumSectionSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.setModel
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
        :description: QtWidgets/QHeaderView-setModel-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.setOffset
        :args:
            int
        :description: QtWidgets/QHeaderView-setOffset-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.setOffsetToLastSection
        :description: QtWidgets/QHeaderView-setOffsetToLastSection-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.setOffsetToSectionPosition
        :args:
            int
        :description: QtWidgets/QHeaderView-setOffsetToSectionPosition-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.setResizeContentsPrecision
        :args:
            int
        :description: QtWidgets/QHeaderView-setResizeContentsPrecision-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.setSectionHidden
        :args:
            int
            bool
        :description: QtWidgets/QHeaderView-setSectionHidden-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.setSectionResizeMode
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QHeaderView.ResizeMode`
        :description: QtWidgets/QHeaderView-setSectionResizeMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.setSectionResizeMode
        :args:
            int
            :sip:ref:`~PyQt6.QtWidgets.QHeaderView.ResizeMode`
        :description: QtWidgets/QHeaderView-setSectionResizeMode-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.setSectionsClickable
        :args:
            bool
        :description: QtWidgets/QHeaderView-setSectionsClickable-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.setSectionsMovable
        :args:
            bool
        :description: QtWidgets/QHeaderView-setSectionsMovable-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.setSelection
        :args:
            :sip:ref:`~PyQt6.QtCore.QRect`
            :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlag`
        :description: QtWidgets/QHeaderView-setSelection-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.setSortIndicator
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.Qt.SortOrder`
        :description: QtWidgets/QHeaderView-setSortIndicator-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.setSortIndicatorClearable
        :args:
            bool
        :description: QtWidgets/QHeaderView-setSortIndicatorClearable-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.setSortIndicatorShown
        :args:
            bool
        :description: QtWidgets/QHeaderView-setSortIndicatorShown-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.setStretchLastSection
        :args:
            bool
        :description: QtWidgets/QHeaderView-setStretchLastSection-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.setVisible
        :args:
            bool
        :description: QtWidgets/QHeaderView-setVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.showSection
        :args:
            int
        :description: QtWidgets/QHeaderView-showSection-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.sizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QHeaderView-sizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.sortIndicatorOrder
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.SortOrder`
        :description: QtWidgets/QHeaderView-sortIndicatorOrder-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.sortIndicatorSection
        :returns:
            int
        :description: QtWidgets/QHeaderView-sortIndicatorSection-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.stretchLastSection
        :returns:
            bool
        :description: QtWidgets/QHeaderView-stretchLastSection-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.stretchSectionCount
        :returns:
            int
        :description: QtWidgets/QHeaderView-stretchSectionCount-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.swapSections
        :args:
            int
            int
        :description: QtWidgets/QHeaderView-swapSections-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.updateGeometries
        :description: QtWidgets/QHeaderView-updateGeometries-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.updateSection
        :args:
            int
        :description: QtWidgets/QHeaderView-updateSection-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.verticalOffset
        :returns:
            int
        :description: QtWidgets/QHeaderView-verticalOffset-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.viewportEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QHeaderView-viewportEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.visualIndex
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QHeaderView-visualIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.visualIndexAt
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QHeaderView-visualIndexAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.visualRect
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QHeaderView-visualRect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QHeaderView.visualRegionForSelection
        :args:
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QRegion`
        :description: QtWidgets/QHeaderView-visualRegionForSelection-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QHeaderView.geometriesChanged
        :description: QtWidgets/QHeaderView-geometriesChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QHeaderView.sectionClicked
        :args:
            int
        :description: QtWidgets/QHeaderView-sectionClicked-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QHeaderView.sectionCountChanged
        :args:
            int
            int
        :description: QtWidgets/QHeaderView-sectionCountChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QHeaderView.sectionDoubleClicked
        :args:
            int
        :description: QtWidgets/QHeaderView-sectionDoubleClicked-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QHeaderView.sectionEntered
        :args:
            int
        :description: QtWidgets/QHeaderView-sectionEntered-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QHeaderView.sectionHandleDoubleClicked
        :args:
            int
        :description: QtWidgets/QHeaderView-sectionHandleDoubleClicked-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QHeaderView.sectionMoved
        :args:
            int
            int
            int
        :description: QtWidgets/QHeaderView-sectionMoved-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QHeaderView.sectionPressed
        :args:
            int
        :description: QtWidgets/QHeaderView-sectionPressed-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QHeaderView.sectionResized
        :args:
            int
            int
            int
        :description: QtWidgets/QHeaderView-sectionResized-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QHeaderView.sortIndicatorChanged
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.Qt.SortOrder`
        :description: QtWidgets/QHeaderView-sortIndicatorChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QHeaderView.sortIndicatorClearableChanged
        :args:
            bool
        :description: QtWidgets/QHeaderView-sortIndicatorClearableChanged-s.rst
