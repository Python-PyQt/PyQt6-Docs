:orphan:

.. sip:class:: PyQt6.QtWidgets.QApplication
    :inherits: :sip:ref:`~PyQt6.QtGui.QGuiApplication`
    :description: QtWidgets/QApplication-c.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.__init__
        :args:
            List[str]
        :description: QtWidgets/QApplication-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.aboutQt
        :static:
        :description: QtWidgets/QApplication-aboutQt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.activeModalWidget
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :static:
        :description: QtWidgets/QApplication-activeModalWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.activePopupWidget
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :static:
        :description: QtWidgets/QApplication-activePopupWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.activeWindow
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :static:
        :description: QtWidgets/QApplication-activeWindow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.alert
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            msecs: int = 0
        :static:
        :description: QtWidgets/QApplication-alert-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.allWidgets
        :returns:
            List[:sip:ref:`~PyQt6.QtWidgets.QWidget`]
        :static:
        :description: QtWidgets/QApplication-allWidgets-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.autoSipEnabled
        :returns:
            bool
        :description: QtWidgets/QApplication-autoSipEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.beep
        :static:
        :description: QtWidgets/QApplication-beep-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.closeAllWindows
        :static:
        :description: QtWidgets/QApplication-closeAllWindows-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.cursorFlashTime
        :returns:
            int
        :static:
        :description: QtWidgets/QApplication-cursorFlashTime-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.doubleClickInterval
        :returns:
            int
        :static:
        :description: QtWidgets/QApplication-doubleClickInterval-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QApplication-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.exec
        :returns:
            int
        :static:
        :description: QtWidgets/QApplication-exec-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.focusWidget
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :static:
        :description: QtWidgets/QApplication-focusWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.font
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :static:
        :description: QtWidgets/QApplication-font-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.font
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :static:
        :description: QtWidgets/QApplication-font-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.font
        :args:
            str
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :static:
        :description: QtWidgets/QApplication-font-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.isEffectEnabled
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.UIEffect`
        :returns:
            bool
        :static:
        :description: QtWidgets/QApplication-isEffectEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.keyboardInputInterval
        :returns:
            int
        :static:
        :description: QtWidgets/QApplication-keyboardInputInterval-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.notify
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QApplication-notify-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.palette
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPalette`
        :static:
        :description: QtWidgets/QApplication-palette-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.palette
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPalette`
        :static:
        :description: QtWidgets/QApplication-palette-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.palette
        :args:
            str
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPalette`
        :static:
        :description: QtWidgets/QApplication-palette-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.setActiveWindow
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :static:
        :description: QtWidgets/QApplication-setActiveWindow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.setAutoSipEnabled
        :args:
            bool
        :description: QtWidgets/QApplication-setAutoSipEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.setCursorFlashTime
        :args:
            int
        :static:
        :description: QtWidgets/QApplication-setCursorFlashTime-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.setDoubleClickInterval
        :args:
            int
        :static:
        :description: QtWidgets/QApplication-setDoubleClickInterval-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.setEffectEnabled
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.UIEffect`
            enabled: bool = True
        :static:
        :description: QtWidgets/QApplication-setEffectEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.setFont
        :args:
            :sip:ref:`~PyQt6.QtGui.QFont`
            className: str = None
        :static:
        :description: QtWidgets/QApplication-setFont-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.setKeyboardInputInterval
        :args:
            int
        :static:
        :description: QtWidgets/QApplication-setKeyboardInputInterval-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.setPalette
        :args:
            :sip:ref:`~PyQt6.QtGui.QPalette`
            className: str = None
        :static:
        :description: QtWidgets/QApplication-setPalette-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.setStartDragDistance
        :args:
            int
        :static:
        :description: QtWidgets/QApplication-setStartDragDistance-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.setStartDragTime
        :args:
            int
        :static:
        :description: QtWidgets/QApplication-setStartDragTime-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.setStyle
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyle`
        :static:
        :description: QtWidgets/QApplication-setStyle-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.setStyle
        :args:
            str
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QStyle`
        :static:
        :description: QtWidgets/QApplication-setStyle-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.setStyleSheet
        :args:
            str
        :description: QtWidgets/QApplication-setStyleSheet-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.setWheelScrollLines
        :args:
            int
        :static:
        :description: QtWidgets/QApplication-setWheelScrollLines-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.startDragDistance
        :returns:
            int
        :static:
        :description: QtWidgets/QApplication-startDragDistance-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.startDragTime
        :returns:
            int
        :static:
        :description: QtWidgets/QApplication-startDragTime-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.style
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QStyle`
        :static:
        :description: QtWidgets/QApplication-style-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.styleSheet
        :returns:
            str
        :description: QtWidgets/QApplication-styleSheet-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.topLevelAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :static:
        :description: QtWidgets/QApplication-topLevelAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.topLevelAt
        :args:
            int
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :static:
        :description: QtWidgets/QApplication-topLevelAt-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.topLevelWidgets
        :returns:
            List[:sip:ref:`~PyQt6.QtWidgets.QWidget`]
        :static:
        :description: QtWidgets/QApplication-topLevelWidgets-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.wheelScrollLines
        :returns:
            int
        :static:
        :description: QtWidgets/QApplication-wheelScrollLines-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.widgetAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :static:
        :description: QtWidgets/QApplication-widgetAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QApplication.widgetAt
        :args:
            int
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :static:
        :description: QtWidgets/QApplication-widgetAt-f-1.rst

    .. sip:signal:: PyQt6.QtWidgets.QApplication.focusChanged
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QApplication-focusChanged-s.rst
