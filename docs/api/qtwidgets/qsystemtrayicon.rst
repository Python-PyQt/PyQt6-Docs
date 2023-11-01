:orphan:

.. sip:class:: PyQt6.QtWidgets.QSystemTrayIcon
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtWidgets/QSystemTrayIcon-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QSystemTrayIcon.ActivationReason
        :description: QtWidgets/QSystemTrayIcon-ActivationReason-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QSystemTrayIcon.ActivationReason.Context
            :description: QtWidgets/QSystemTrayIcon-ActivationReason-Context-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QSystemTrayIcon.ActivationReason.DoubleClick
            :description: QtWidgets/QSystemTrayIcon-ActivationReason-DoubleClick-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QSystemTrayIcon.ActivationReason.MiddleClick
            :description: QtWidgets/QSystemTrayIcon-ActivationReason-MiddleClick-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QSystemTrayIcon.ActivationReason.Trigger
            :description: QtWidgets/QSystemTrayIcon-ActivationReason-Trigger-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QSystemTrayIcon.ActivationReason.Unknown
            :description: QtWidgets/QSystemTrayIcon-ActivationReason-Unknown-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QSystemTrayIcon.MessageIcon
        :description: QtWidgets/QSystemTrayIcon-MessageIcon-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QSystemTrayIcon.MessageIcon.Critical
            :description: QtWidgets/QSystemTrayIcon-MessageIcon-Critical-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QSystemTrayIcon.MessageIcon.Information
            :description: QtWidgets/QSystemTrayIcon-MessageIcon-Information-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QSystemTrayIcon.MessageIcon.NoIcon
            :description: QtWidgets/QSystemTrayIcon-MessageIcon-NoIcon-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QSystemTrayIcon.MessageIcon.Warning
            :description: QtWidgets/QSystemTrayIcon-MessageIcon-Warning-v.rst

    .. sip:method:: PyQt6.QtWidgets.QSystemTrayIcon.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtWidgets/QSystemTrayIcon-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSystemTrayIcon.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QIcon`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtWidgets/QSystemTrayIcon-__init__-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QSystemTrayIcon.contextMenu
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QMenu`
        :description: QtWidgets/QSystemTrayIcon-contextMenu-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSystemTrayIcon.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QSystemTrayIcon-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSystemTrayIcon.geometry
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QSystemTrayIcon-geometry-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSystemTrayIcon.hide
        :description: QtWidgets/QSystemTrayIcon-hide-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSystemTrayIcon.icon
        :returns:
            :sip:ref:`~PyQt6.QtGui.QIcon`
        :description: QtWidgets/QSystemTrayIcon-icon-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSystemTrayIcon.isSystemTrayAvailable
        :returns:
            bool
        :static:
        :description: QtWidgets/QSystemTrayIcon-isSystemTrayAvailable-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSystemTrayIcon.isVisible
        :returns:
            bool
        :description: QtWidgets/QSystemTrayIcon-isVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSystemTrayIcon.setContextMenu
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QMenu`
        :description: QtWidgets/QSystemTrayIcon-setContextMenu-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSystemTrayIcon.setIcon
        :args:
            :sip:ref:`~PyQt6.QtGui.QIcon`
        :description: QtWidgets/QSystemTrayIcon-setIcon-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSystemTrayIcon.setToolTip
        :args:
            Optional[str]
        :description: QtWidgets/QSystemTrayIcon-setToolTip-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QSystemTrayIcon.setVisible
        :args:
            bool
        :description: QtWidgets/QSystemTrayIcon-setVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSystemTrayIcon.show
        :description: QtWidgets/QSystemTrayIcon-show-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSystemTrayIcon.showMessage
        :args:
            Optional[str]
            Optional[str]
            icon: :sip:ref:`~PyQt6.QtWidgets.QSystemTrayIcon.MessageIcon` = :sip:ref:`~PyQt6.QtWidgets.QSystemTrayIcon.MessageIcon.Information`
            msecs: int = 10000
        :description: QtWidgets/QSystemTrayIcon-showMessage-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QSystemTrayIcon.showMessage
        :args:
            Optional[str]
            Optional[str]
            :sip:ref:`~PyQt6.QtGui.QIcon`
            msecs: int = 10000
        :description: QtWidgets/QSystemTrayIcon-showMessage-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.QSystemTrayIcon.supportsMessages
        :returns:
            bool
        :static:
        :description: QtWidgets/QSystemTrayIcon-supportsMessages-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSystemTrayIcon.toolTip
        :returns:
            str
        :description: QtWidgets/QSystemTrayIcon-toolTip-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QSystemTrayIcon.activated
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QSystemTrayIcon.ActivationReason`
        :description: QtWidgets/QSystemTrayIcon-activated-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QSystemTrayIcon.messageClicked
        :description: QtWidgets/QSystemTrayIcon-messageClicked-s.rst
