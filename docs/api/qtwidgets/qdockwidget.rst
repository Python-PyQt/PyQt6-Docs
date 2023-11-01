:orphan:

.. sip:class:: PyQt6.QtWidgets.QDockWidget
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QWidget`
    :description: QtWidgets/QDockWidget-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QDockWidget.DockWidgetFeature
        :description: QtWidgets/QDockWidget-DockWidgetFeature-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetClosable
            :description: QtWidgets/QDockWidget-DockWidgetFeature-DockWidgetClosable-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetFloatable
            :description: QtWidgets/QDockWidget-DockWidgetFeature-DockWidgetFloatable-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetMovable
            :description: QtWidgets/QDockWidget-DockWidgetFeature-DockWidgetMovable-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetVerticalTitleBar
            :description: QtWidgets/QDockWidget-DockWidgetFeature-DockWidgetVerticalTitleBar-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QDockWidget.DockWidgetFeature.NoDockWidgetFeatures
            :description: QtWidgets/QDockWidget-DockWidgetFeature-NoDockWidgetFeatures-v.rst

    .. sip:method:: PyQt6.QtWidgets.QDockWidget.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
            flags: :sip:ref:`~PyQt6.QtCore.Qt.WindowType` = Qt.WindowFlags()
        :description: QtWidgets/QDockWidget-__init__-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QDockWidget.__init__
        :args:
            Optional[str]
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
            flags: :sip:ref:`~PyQt6.QtCore.Qt.WindowType` = Qt.WindowFlags()
        :description: QtWidgets/QDockWidget-__init__-f-4.rst

    .. sip:method:: PyQt6.QtWidgets.QDockWidget.allowedAreas
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.DockWidgetArea`
        :description: QtWidgets/QDockWidget-allowedAreas-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QDockWidget.changeEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtWidgets/QDockWidget-changeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDockWidget.closeEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QCloseEvent`
        :description: QtWidgets/QDockWidget-closeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDockWidget.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QDockWidget-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDockWidget.features
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QDockWidget.DockWidgetFeature`
        :description: QtWidgets/QDockWidget-features-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QDockWidget.initStyleOption
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionDockWidget`
        :description: QtWidgets/QDockWidget-initStyleOption-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDockWidget.isAreaAllowed
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.DockWidgetArea`
        :returns:
            bool
        :description: QtWidgets/QDockWidget-isAreaAllowed-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QDockWidget.isFloating
        :returns:
            bool
        :description: QtWidgets/QDockWidget-isFloating-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDockWidget.paintEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QPaintEvent`
        :description: QtWidgets/QDockWidget-paintEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDockWidget.setAllowedAreas
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.DockWidgetArea`
        :description: QtWidgets/QDockWidget-setAllowedAreas-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QDockWidget.setFeatures
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QDockWidget.DockWidgetFeature`
        :description: QtWidgets/QDockWidget-setFeatures-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QDockWidget.setFloating
        :args:
            bool
        :description: QtWidgets/QDockWidget-setFloating-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDockWidget.setTitleBarWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QDockWidget-setTitleBarWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDockWidget.setWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QDockWidget-setWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDockWidget.titleBarWidget
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QDockWidget-titleBarWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDockWidget.toggleViewAction
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtWidgets/QDockWidget-toggleViewAction-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDockWidget.widget
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QDockWidget-widget-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QDockWidget.allowedAreasChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.DockWidgetArea`
        :description: QtWidgets/QDockWidget-allowedAreasChanged-s-1.rst

    .. sip:signal:: PyQt6.QtWidgets.QDockWidget.dockLocationChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.DockWidgetArea`
        :description: QtWidgets/QDockWidget-dockLocationChanged-s-1.rst

    .. sip:signal:: PyQt6.QtWidgets.QDockWidget.featuresChanged
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QDockWidget.DockWidgetFeature`
        :description: QtWidgets/QDockWidget-featuresChanged-s-1.rst

    .. sip:signal:: PyQt6.QtWidgets.QDockWidget.topLevelChanged
        :args:
            bool
        :description: QtWidgets/QDockWidget-topLevelChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QDockWidget.visibilityChanged
        :args:
            bool
        :description: QtWidgets/QDockWidget-visibilityChanged-s.rst
