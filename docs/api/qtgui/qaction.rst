:orphan:

.. sip:class:: PyQt6.QtGui.QAction
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtGui/QAction-c.rst

    .. sip:enum:: PyQt6.QtGui.QAction.ActionEvent
        :description: QtGui/QAction-ActionEvent-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QAction.ActionEvent.Hover
            :description: QtGui/QAction-ActionEvent-Hover-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QAction.ActionEvent.Trigger
            :description: QtGui/QAction-ActionEvent-Trigger-v.rst

    .. sip:enum:: PyQt6.QtGui.QAction.MenuRole
        :description: QtGui/QAction-MenuRole-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QAction.MenuRole.AboutQtRole
            :description: QtGui/QAction-MenuRole-AboutQtRole-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QAction.MenuRole.AboutRole
            :description: QtGui/QAction-MenuRole-AboutRole-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QAction.MenuRole.ApplicationSpecificRole
            :description: QtGui/QAction-MenuRole-ApplicationSpecificRole-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QAction.MenuRole.NoRole
            :description: QtGui/QAction-MenuRole-NoRole-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QAction.MenuRole.PreferencesRole
            :description: QtGui/QAction-MenuRole-PreferencesRole-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QAction.MenuRole.QuitRole
            :description: QtGui/QAction-MenuRole-QuitRole-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QAction.MenuRole.TextHeuristicRole
            :description: QtGui/QAction-MenuRole-TextHeuristicRole-v.rst

    .. sip:enum:: PyQt6.QtGui.QAction.Priority
        :description: QtGui/QAction-Priority-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QAction.Priority.HighPriority
            :description: QtGui/QAction-Priority-HighPriority-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QAction.Priority.LowPriority
            :description: QtGui/QAction-Priority-LowPriority-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QAction.Priority.NormalPriority
            :description: QtGui/QAction-Priority-NormalPriority-v.rst

    .. sip:method:: PyQt6.QtGui.QAction.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGui/QAction-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.__init__
        :args:
            Optional[str]
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGui/QAction-__init__-f-3.rst

    .. sip:method:: PyQt6.QtGui.QAction.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QIcon`
            Optional[str]
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGui/QAction-__init__-f-4.rst

    .. sip:method:: PyQt6.QtGui.QAction.actionGroup
        :returns:
            :sip:ref:`~PyQt6.QtGui.QActionGroup`
        :description: QtGui/QAction-actionGroup-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.activate
        :args:
            :sip:ref:`~PyQt6.QtGui.QAction.ActionEvent`
        :description: QtGui/QAction-activate-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.associatedObjects
        :returns:
            List[:sip:ref:`~PyQt6.QtCore.QObject`]
        :description: QtGui/QAction-associatedObjects-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.autoRepeat
        :returns:
            bool
        :description: QtGui/QAction-autoRepeat-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.data
        :returns:
            Any
        :description: QtGui/QAction-data-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtGui/QAction-event-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.font
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtGui/QAction-font-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.hover
        :description: QtGui/QAction-hover-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.icon
        :returns:
            :sip:ref:`~PyQt6.QtGui.QIcon`
        :description: QtGui/QAction-icon-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.iconText
        :returns:
            str
        :description: QtGui/QAction-iconText-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.isCheckable
        :returns:
            bool
        :description: QtGui/QAction-isCheckable-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.isChecked
        :returns:
            bool
        :description: QtGui/QAction-isChecked-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.isEnabled
        :returns:
            bool
        :description: QtGui/QAction-isEnabled-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.isIconVisibleInMenu
        :returns:
            bool
        :description: QtGui/QAction-isIconVisibleInMenu-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.isSeparator
        :returns:
            bool
        :description: QtGui/QAction-isSeparator-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.isShortcutVisibleInContextMenu
        :returns:
            bool
        :description: QtGui/QAction-isShortcutVisibleInContextMenu-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.isVisible
        :returns:
            bool
        :description: QtGui/QAction-isVisible-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.menu
        :returns:
            :sip:ref:`~PyQt6.QtGui.QMenu`
        :description: QtGui/QAction-menu-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.menuRole
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAction.MenuRole`
        :description: QtGui/QAction-menuRole-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.priority
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAction.Priority`
        :description: QtGui/QAction-priority-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.resetEnabled
        :description: QtGui/QAction-resetEnabled-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.setActionGroup
        :args:
            :sip:ref:`~PyQt6.QtGui.QActionGroup`
        :description: QtGui/QAction-setActionGroup-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.setAutoRepeat
        :args:
            bool
        :description: QtGui/QAction-setAutoRepeat-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.setCheckable
        :args:
            bool
        :description: QtGui/QAction-setCheckable-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.setChecked
        :args:
            bool
        :description: QtGui/QAction-setChecked-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.setData
        :args:
            Any
        :description: QtGui/QAction-setData-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.setDisabled
        :args:
            bool
        :description: QtGui/QAction-setDisabled-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.setEnabled
        :args:
            bool
        :description: QtGui/QAction-setEnabled-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.setFont
        :args:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtGui/QAction-setFont-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.setIcon
        :args:
            :sip:ref:`~PyQt6.QtGui.QIcon`
        :description: QtGui/QAction-setIcon-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.setIconText
        :args:
            Optional[str]
        :description: QtGui/QAction-setIconText-f-1.rst

    .. sip:method:: PyQt6.QtGui.QAction.setIconVisibleInMenu
        :args:
            bool
        :description: QtGui/QAction-setIconVisibleInMenu-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.setMenu
        :args:
            :sip:ref:`~PyQt6.QtGui.QMenu`
        :description: QtGui/QAction-setMenu-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.setMenuRole
        :args:
            :sip:ref:`~PyQt6.QtGui.QAction.MenuRole`
        :description: QtGui/QAction-setMenuRole-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.setPriority
        :args:
            :sip:ref:`~PyQt6.QtGui.QAction.Priority`
        :description: QtGui/QAction-setPriority-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.setSeparator
        :args:
            bool
        :description: QtGui/QAction-setSeparator-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.setShortcut
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QKeySequence`, :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey`, Optional[str], int]
        :description: QtGui/QAction-setShortcut-f-1.rst

    .. sip:method:: PyQt6.QtGui.QAction.setShortcutContext
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.ShortcutContext`
        :description: QtGui/QAction-setShortcutContext-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.setShortcuts
        :args:
            Iterable[Union[:sip:ref:`~PyQt6.QtGui.QKeySequence`, :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey`, Optional[str], int]]
        :description: QtGui/QAction-setShortcuts-f-2.rst

    .. sip:method:: PyQt6.QtGui.QAction.setShortcuts
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey`
        :description: QtGui/QAction-setShortcuts-f-1.rst

    .. sip:method:: PyQt6.QtGui.QAction.setShortcutVisibleInContextMenu
        :args:
            bool
        :description: QtGui/QAction-setShortcutVisibleInContextMenu-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.setStatusTip
        :args:
            Optional[str]
        :description: QtGui/QAction-setStatusTip-f-1.rst

    .. sip:method:: PyQt6.QtGui.QAction.setText
        :args:
            Optional[str]
        :description: QtGui/QAction-setText-f-1.rst

    .. sip:method:: PyQt6.QtGui.QAction.setToolTip
        :args:
            Optional[str]
        :description: QtGui/QAction-setToolTip-f-1.rst

    .. sip:method:: PyQt6.QtGui.QAction.setVisible
        :args:
            bool
        :description: QtGui/QAction-setVisible-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.setWhatsThis
        :args:
            Optional[str]
        :description: QtGui/QAction-setWhatsThis-f-1.rst

    .. sip:method:: PyQt6.QtGui.QAction.shortcut
        :returns:
            :sip:ref:`~PyQt6.QtGui.QKeySequence`
        :description: QtGui/QAction-shortcut-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.shortcutContext
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.ShortcutContext`
        :description: QtGui/QAction-shortcutContext-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.shortcuts
        :returns:
            List[:sip:ref:`~PyQt6.QtGui.QKeySequence`]
        :description: QtGui/QAction-shortcuts-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.showStatusText
        :args:
            object: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :returns:
            bool
        :description: QtGui/QAction-showStatusText-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.statusTip
        :returns:
            str
        :description: QtGui/QAction-statusTip-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.text
        :returns:
            str
        :description: QtGui/QAction-text-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.toggle
        :description: QtGui/QAction-toggle-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.toolTip
        :returns:
            str
        :description: QtGui/QAction-toolTip-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.trigger
        :description: QtGui/QAction-trigger-f.rst

    .. sip:method:: PyQt6.QtGui.QAction.whatsThis
        :returns:
            str
        :description: QtGui/QAction-whatsThis-f.rst

    .. sip:signal:: PyQt6.QtGui.QAction.changed
        :description: QtGui/QAction-changed-s.rst

    .. sip:signal:: PyQt6.QtGui.QAction.checkableChanged
        :args:
            bool
        :description: QtGui/QAction-checkableChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QAction.enabledChanged
        :args:
            bool
        :description: QtGui/QAction-enabledChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QAction.hovered
        :description: QtGui/QAction-hovered-s.rst

    .. sip:signal:: PyQt6.QtGui.QAction.toggled
        :args:
            bool
        :description: QtGui/QAction-toggled-s.rst

    .. sip:signal:: PyQt6.QtGui.QAction.triggered
        :args:
            checked: bool = False
        :description: QtGui/QAction-triggered-s.rst

    .. sip:signal:: PyQt6.QtGui.QAction.visibleChanged
        :description: QtGui/QAction-visibleChanged-s.rst
