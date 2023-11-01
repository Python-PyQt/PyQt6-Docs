:orphan:

.. sip:class:: PyQt6.QtWidgets.QTabWidget
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QWidget`
    :description: QtWidgets/QTabWidget-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QTabWidget.TabPosition
        :description: QtWidgets/QTabWidget-TabPosition-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTabWidget.TabPosition.East
            :description: QtWidgets/QTabWidget-TabPosition-East-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTabWidget.TabPosition.North
            :description: QtWidgets/QTabWidget-TabPosition-North-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTabWidget.TabPosition.South
            :description: QtWidgets/QTabWidget-TabPosition-South-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTabWidget.TabPosition.West
            :description: QtWidgets/QTabWidget-TabPosition-West-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QTabWidget.TabShape
        :description: QtWidgets/QTabWidget-TabShape-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTabWidget.TabShape.Rounded
            :description: QtWidgets/QTabWidget-TabShape-Rounded-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTabWidget.TabShape.Triangular
            :description: QtWidgets/QTabWidget-TabShape-Triangular-v.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QTabWidget-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.addTab
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            Optional[str]
        :returns:
            int
        :description: QtWidgets/QTabWidget-addTab-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.addTab
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtGui.QIcon`
            Optional[str]
        :returns:
            int
        :description: QtWidgets/QTabWidget-addTab-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.changeEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtWidgets/QTabWidget-changeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.clear
        :description: QtWidgets/QTabWidget-clear-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.cornerWidget
        :args:
            corner: :sip:ref:`~PyQt6.QtCore.Qt.Corner` = :sip:ref:`~PyQt6.QtCore.Qt.Corner.TopRightCorner`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QTabWidget-cornerWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.count
        :returns:
            int
        :description: QtWidgets/QTabWidget-count-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.currentIndex
        :returns:
            int
        :description: QtWidgets/QTabWidget-currentIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.currentWidget
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QTabWidget-currentWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.documentMode
        :returns:
            bool
        :description: QtWidgets/QTabWidget-documentMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.elideMode
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.TextElideMode`
        :description: QtWidgets/QTabWidget-elideMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QTabWidget-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.hasHeightForWidth
        :returns:
            bool
        :description: QtWidgets/QTabWidget-hasHeightForWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.heightForWidth
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QTabWidget-heightForWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.iconSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QTabWidget-iconSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.indexOf
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :returns:
            int
        :description: QtWidgets/QTabWidget-indexOf-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.initStyleOption
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionTabWidgetFrame`
        :description: QtWidgets/QTabWidget-initStyleOption-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.insertTab
        :args:
            int
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            Optional[str]
        :returns:
            int
        :description: QtWidgets/QTabWidget-insertTab-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.insertTab
        :args:
            int
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtGui.QIcon`
            Optional[str]
        :returns:
            int
        :description: QtWidgets/QTabWidget-insertTab-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.isMovable
        :returns:
            bool
        :description: QtWidgets/QTabWidget-isMovable-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.isTabEnabled
        :args:
            int
        :returns:
            bool
        :description: QtWidgets/QTabWidget-isTabEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.isTabVisible
        :args:
            int
        :returns:
            bool
        :description: QtWidgets/QTabWidget-isTabVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.keyPressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtWidgets/QTabWidget-keyPressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.__len__
        :returns:
            int
        :description: QtWidgets/QTabWidget-__len__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.minimumSizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QTabWidget-minimumSizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.paintEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QPaintEvent`
        :description: QtWidgets/QTabWidget-paintEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.removeTab
        :args:
            int
        :description: QtWidgets/QTabWidget-removeTab-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.resizeEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QResizeEvent`
        :description: QtWidgets/QTabWidget-resizeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.setCornerWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            corner: :sip:ref:`~PyQt6.QtCore.Qt.Corner` = :sip:ref:`~PyQt6.QtCore.Qt.Corner.TopRightCorner`
        :description: QtWidgets/QTabWidget-setCornerWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.setCurrentIndex
        :args:
            int
        :description: QtWidgets/QTabWidget-setCurrentIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.setCurrentWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QTabWidget-setCurrentWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.setDocumentMode
        :args:
            bool
        :description: QtWidgets/QTabWidget-setDocumentMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.setElideMode
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.TextElideMode`
        :description: QtWidgets/QTabWidget-setElideMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.setIconSize
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QTabWidget-setIconSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.setMovable
        :args:
            bool
        :description: QtWidgets/QTabWidget-setMovable-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.setTabBar
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTabBar`
        :description: QtWidgets/QTabWidget-setTabBar-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.setTabBarAutoHide
        :args:
            bool
        :description: QtWidgets/QTabWidget-setTabBarAutoHide-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.setTabEnabled
        :args:
            int
            bool
        :description: QtWidgets/QTabWidget-setTabEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.setTabIcon
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QIcon`
        :description: QtWidgets/QTabWidget-setTabIcon-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.setTabPosition
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTabWidget.TabPosition`
        :description: QtWidgets/QTabWidget-setTabPosition-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.setTabsClosable
        :args:
            bool
        :description: QtWidgets/QTabWidget-setTabsClosable-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.setTabShape
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTabWidget.TabShape`
        :description: QtWidgets/QTabWidget-setTabShape-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.setTabText
        :args:
            int
            Optional[str]
        :description: QtWidgets/QTabWidget-setTabText-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.setTabToolTip
        :args:
            int
            Optional[str]
        :description: QtWidgets/QTabWidget-setTabToolTip-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.setTabVisible
        :args:
            int
            bool
        :description: QtWidgets/QTabWidget-setTabVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.setTabWhatsThis
        :args:
            int
            Optional[str]
        :description: QtWidgets/QTabWidget-setTabWhatsThis-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.setUsesScrollButtons
        :args:
            bool
        :description: QtWidgets/QTabWidget-setUsesScrollButtons-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.showEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QShowEvent`
        :description: QtWidgets/QTabWidget-showEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.sizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QTabWidget-sizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.tabBar
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTabBar`
        :description: QtWidgets/QTabWidget-tabBar-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.tabBarAutoHide
        :returns:
            bool
        :description: QtWidgets/QTabWidget-tabBarAutoHide-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.tabIcon
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QIcon`
        :description: QtWidgets/QTabWidget-tabIcon-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.tabInserted
        :args:
            int
        :description: QtWidgets/QTabWidget-tabInserted-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.tabPosition
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTabWidget.TabPosition`
        :description: QtWidgets/QTabWidget-tabPosition-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.tabRemoved
        :args:
            int
        :description: QtWidgets/QTabWidget-tabRemoved-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.tabsClosable
        :returns:
            bool
        :description: QtWidgets/QTabWidget-tabsClosable-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.tabShape
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTabWidget.TabShape`
        :description: QtWidgets/QTabWidget-tabShape-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.tabText
        :args:
            int
        :returns:
            str
        :description: QtWidgets/QTabWidget-tabText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.tabToolTip
        :args:
            int
        :returns:
            str
        :description: QtWidgets/QTabWidget-tabToolTip-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.tabWhatsThis
        :args:
            int
        :returns:
            str
        :description: QtWidgets/QTabWidget-tabWhatsThis-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.usesScrollButtons
        :returns:
            bool
        :description: QtWidgets/QTabWidget-usesScrollButtons-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTabWidget.widget
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QTabWidget-widget-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QTabWidget.currentChanged
        :args:
            int
        :description: QtWidgets/QTabWidget-currentChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTabWidget.tabBarClicked
        :args:
            int
        :description: QtWidgets/QTabWidget-tabBarClicked-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTabWidget.tabBarDoubleClicked
        :args:
            int
        :description: QtWidgets/QTabWidget-tabBarDoubleClicked-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTabWidget.tabCloseRequested
        :args:
            int
        :description: QtWidgets/QTabWidget-tabCloseRequested-s.rst
