:orphan:

.. sip:class:: PyQt6.QtWidgets.QTabBar
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QWidget`
    :description: QtWidgets/QTabBar-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QTabBar.ButtonPosition
        :description: QtWidgets/QTabBar-ButtonPosition-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTabBar.ButtonPosition.LeftSide
            :description: QtWidgets/QTabBar-ButtonPosition-LeftSide-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTabBar.ButtonPosition.RightSide
            :description: QtWidgets/QTabBar-ButtonPosition-RightSide-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QTabBar.SelectionBehavior
        :description: QtWidgets/QTabBar-SelectionBehavior-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTabBar.SelectionBehavior.SelectLeftTab
            :description: QtWidgets/QTabBar-SelectionBehavior-SelectLeftTab-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTabBar.SelectionBehavior.SelectPreviousTab
            :description: QtWidgets/QTabBar-SelectionBehavior-SelectPreviousTab-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTabBar.SelectionBehavior.SelectRightTab
            :description: QtWidgets/QTabBar-SelectionBehavior-SelectRightTab-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QTabBar.Shape
        :description: QtWidgets/QTabBar-Shape-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTabBar.Shape.RoundedEast
            :description: QtWidgets/QTabBar-Shape-RoundedEast-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTabBar.Shape.RoundedNorth
            :description: QtWidgets/QTabBar-Shape-RoundedNorth-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTabBar.Shape.RoundedSouth
            :description: QtWidgets/QTabBar-Shape-RoundedSouth-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTabBar.Shape.RoundedWest
            :description: QtWidgets/QTabBar-Shape-RoundedWest-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTabBar.Shape.TriangularEast
            :description: QtWidgets/QTabBar-Shape-TriangularEast-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTabBar.Shape.TriangularNorth
            :description: QtWidgets/QTabBar-Shape-TriangularNorth-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTabBar.Shape.TriangularSouth
            :description: QtWidgets/QTabBar-Shape-TriangularSouth-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTabBar.Shape.TriangularWest
            :description: QtWidgets/QTabBar-Shape-TriangularWest-v.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QTabBar-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.accessibleTabName
        :args:
            int
        :returns:
            str
        :description: QtWidgets/QTabBar-accessibleTabName-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.addTab
        :args:
            Optional[str]
        :returns:
            int
        :description: QtWidgets/QTabBar-addTab-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.addTab
        :args:
            :sip:ref:`~PyQt6.QtGui.QIcon`
            Optional[str]
        :returns:
            int
        :description: QtWidgets/QTabBar-addTab-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.autoHide
        :returns:
            bool
        :description: QtWidgets/QTabBar-autoHide-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.changeCurrentOnDrag
        :returns:
            bool
        :description: QtWidgets/QTabBar-changeCurrentOnDrag-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.changeEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtWidgets/QTabBar-changeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.count
        :returns:
            int
        :description: QtWidgets/QTabBar-count-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.currentIndex
        :returns:
            int
        :description: QtWidgets/QTabBar-currentIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.documentMode
        :returns:
            bool
        :description: QtWidgets/QTabBar-documentMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.drawBase
        :returns:
            bool
        :description: QtWidgets/QTabBar-drawBase-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.elideMode
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.TextElideMode`
        :description: QtWidgets/QTabBar-elideMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QTabBar-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.expanding
        :returns:
            bool
        :description: QtWidgets/QTabBar-expanding-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.hideEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QHideEvent`
        :description: QtWidgets/QTabBar-hideEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.iconSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QTabBar-iconSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.initStyleOption
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionTab`
            int
        :description: QtWidgets/QTabBar-initStyleOption-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.insertTab
        :args:
            int
            Optional[str]
        :returns:
            int
        :description: QtWidgets/QTabBar-insertTab-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.insertTab
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QIcon`
            Optional[str]
        :returns:
            int
        :description: QtWidgets/QTabBar-insertTab-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.isMovable
        :returns:
            bool
        :description: QtWidgets/QTabBar-isMovable-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.isTabEnabled
        :args:
            int
        :returns:
            bool
        :description: QtWidgets/QTabBar-isTabEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.isTabVisible
        :args:
            int
        :returns:
            bool
        :description: QtWidgets/QTabBar-isTabVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.keyPressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtWidgets/QTabBar-keyPressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.__len__
        :returns:
            int
        :description: QtWidgets/QTabBar-__len__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.minimumSizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QTabBar-minimumSizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.minimumTabSizeHint
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QTabBar-minimumTabSizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.mouseDoubleClickEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QTabBar-mouseDoubleClickEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.mouseMoveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QTabBar-mouseMoveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.mousePressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QTabBar-mousePressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.mouseReleaseEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QTabBar-mouseReleaseEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.moveTab
        :args:
            int
            int
        :description: QtWidgets/QTabBar-moveTab-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.paintEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QPaintEvent`
        :description: QtWidgets/QTabBar-paintEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.removeTab
        :args:
            int
        :description: QtWidgets/QTabBar-removeTab-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.resizeEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QResizeEvent`
        :description: QtWidgets/QTabBar-resizeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.selectionBehaviorOnRemove
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTabBar.SelectionBehavior`
        :description: QtWidgets/QTabBar-selectionBehaviorOnRemove-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.setAccessibleTabName
        :args:
            int
            Optional[str]
        :description: QtWidgets/QTabBar-setAccessibleTabName-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.setAutoHide
        :args:
            bool
        :description: QtWidgets/QTabBar-setAutoHide-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.setChangeCurrentOnDrag
        :args:
            bool
        :description: QtWidgets/QTabBar-setChangeCurrentOnDrag-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.setCurrentIndex
        :args:
            int
        :description: QtWidgets/QTabBar-setCurrentIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.setDocumentMode
        :args:
            bool
        :description: QtWidgets/QTabBar-setDocumentMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.setDrawBase
        :args:
            bool
        :description: QtWidgets/QTabBar-setDrawBase-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.setElideMode
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.TextElideMode`
        :description: QtWidgets/QTabBar-setElideMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.setExpanding
        :args:
            bool
        :description: QtWidgets/QTabBar-setExpanding-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.setIconSize
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QTabBar-setIconSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.setMovable
        :args:
            bool
        :description: QtWidgets/QTabBar-setMovable-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.setSelectionBehaviorOnRemove
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTabBar.SelectionBehavior`
        :description: QtWidgets/QTabBar-setSelectionBehaviorOnRemove-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.setShape
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTabBar.Shape`
        :description: QtWidgets/QTabBar-setShape-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.setTabButton
        :args:
            int
            :sip:ref:`~PyQt6.QtWidgets.QTabBar.ButtonPosition`
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QTabBar-setTabButton-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.setTabData
        :args:
            int
            Any
        :description: QtWidgets/QTabBar-setTabData-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.setTabEnabled
        :args:
            int
            bool
        :description: QtWidgets/QTabBar-setTabEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.setTabIcon
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QIcon`
        :description: QtWidgets/QTabBar-setTabIcon-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.setTabsClosable
        :args:
            bool
        :description: QtWidgets/QTabBar-setTabsClosable-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.setTabText
        :args:
            int
            Optional[str]
        :description: QtWidgets/QTabBar-setTabText-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.setTabTextColor
        :args:
            int
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtWidgets/QTabBar-setTabTextColor-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.setTabToolTip
        :args:
            int
            Optional[str]
        :description: QtWidgets/QTabBar-setTabToolTip-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.setTabVisible
        :args:
            int
            bool
        :description: QtWidgets/QTabBar-setTabVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.setTabWhatsThis
        :args:
            int
            Optional[str]
        :description: QtWidgets/QTabBar-setTabWhatsThis-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.setUsesScrollButtons
        :args:
            bool
        :description: QtWidgets/QTabBar-setUsesScrollButtons-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.shape
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTabBar.Shape`
        :description: QtWidgets/QTabBar-shape-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.showEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QShowEvent`
        :description: QtWidgets/QTabBar-showEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.sizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QTabBar-sizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.tabAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            int
        :description: QtWidgets/QTabBar-tabAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.tabButton
        :args:
            int
            :sip:ref:`~PyQt6.QtWidgets.QTabBar.ButtonPosition`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QTabBar-tabButton-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.tabData
        :args:
            int
        :returns:
            Any
        :description: QtWidgets/QTabBar-tabData-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.tabIcon
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QIcon`
        :description: QtWidgets/QTabBar-tabIcon-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.tabInserted
        :args:
            int
        :description: QtWidgets/QTabBar-tabInserted-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.tabLayoutChange
        :description: QtWidgets/QTabBar-tabLayoutChange-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.tabRect
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QTabBar-tabRect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.tabRemoved
        :args:
            int
        :description: QtWidgets/QTabBar-tabRemoved-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.tabsClosable
        :returns:
            bool
        :description: QtWidgets/QTabBar-tabsClosable-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.tabSizeHint
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QTabBar-tabSizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.tabText
        :args:
            int
        :returns:
            str
        :description: QtWidgets/QTabBar-tabText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.tabTextColor
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtWidgets/QTabBar-tabTextColor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.tabToolTip
        :args:
            int
        :returns:
            str
        :description: QtWidgets/QTabBar-tabToolTip-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.tabWhatsThis
        :args:
            int
        :returns:
            str
        :description: QtWidgets/QTabBar-tabWhatsThis-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.timerEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimerEvent`
        :description: QtWidgets/QTabBar-timerEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.usesScrollButtons
        :returns:
            bool
        :description: QtWidgets/QTabBar-usesScrollButtons-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabBar.wheelEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QWheelEvent`
        :description: QtWidgets/QTabBar-wheelEvent-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QTabBar.currentChanged
        :args:
            int
        :description: QtWidgets/QTabBar-currentChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTabBar.tabBarClicked
        :args:
            int
        :description: QtWidgets/QTabBar-tabBarClicked-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTabBar.tabBarDoubleClicked
        :args:
            int
        :description: QtWidgets/QTabBar-tabBarDoubleClicked-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTabBar.tabCloseRequested
        :args:
            int
        :description: QtWidgets/QTabBar-tabCloseRequested-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTabBar.tabMoved
        :args:
            int
            int
        :description: QtWidgets/QTabBar-tabMoved-s.rst
