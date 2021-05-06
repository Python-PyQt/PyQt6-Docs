:orphan:

.. sip:class:: PyQt6.QtWidgets.QMessageBox
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QDialog`
    :description: QtWidgets/QMessageBox-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QMessageBox.ButtonRole
        :description: QtWidgets/QMessageBox-ButtonRole-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.ButtonRole.AcceptRole
            :description: QtWidgets/QMessageBox-ButtonRole-AcceptRole-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.ButtonRole.ActionRole
            :description: QtWidgets/QMessageBox-ButtonRole-ActionRole-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.ButtonRole.ApplyRole
            :description: QtWidgets/QMessageBox-ButtonRole-ApplyRole-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.ButtonRole.DestructiveRole
            :description: QtWidgets/QMessageBox-ButtonRole-DestructiveRole-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.ButtonRole.HelpRole
            :description: QtWidgets/QMessageBox-ButtonRole-HelpRole-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.ButtonRole.InvalidRole
            :description: QtWidgets/QMessageBox-ButtonRole-InvalidRole-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.ButtonRole.NoRole
            :description: QtWidgets/QMessageBox-ButtonRole-NoRole-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.ButtonRole.RejectRole
            :description: QtWidgets/QMessageBox-ButtonRole-RejectRole-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.ButtonRole.ResetRole
            :description: QtWidgets/QMessageBox-ButtonRole-ResetRole-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.ButtonRole.YesRole
            :description: QtWidgets/QMessageBox-ButtonRole-YesRole-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QMessageBox.Icon
        :description: QtWidgets/QMessageBox-Icon-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.Icon.Critical
            :description: QtWidgets/QMessageBox-Icon-Critical-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.Icon.Information
            :description: QtWidgets/QMessageBox-Icon-Information-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.Icon.NoIcon
            :description: QtWidgets/QMessageBox-Icon-NoIcon-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.Icon.Question
            :description: QtWidgets/QMessageBox-Icon-Question-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.Icon.Warning
            :description: QtWidgets/QMessageBox-Icon-Warning-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QMessageBox.StandardButton
        :description: QtWidgets/QMessageBox-StandardButton-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.Abort
            :description: QtWidgets/QMessageBox-StandardButton-Abort-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.Apply
            :description: QtWidgets/QMessageBox-StandardButton-Apply-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.ButtonMask
            :description: QtWidgets/QMessageBox-StandardButton-ButtonMask-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.Cancel
            :description: QtWidgets/QMessageBox-StandardButton-Cancel-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.Close
            :description: QtWidgets/QMessageBox-StandardButton-Close-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.Default
            :description: QtWidgets/QMessageBox-StandardButton-Default-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.Discard
            :description: QtWidgets/QMessageBox-StandardButton-Discard-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.Escape
            :description: QtWidgets/QMessageBox-StandardButton-Escape-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.FirstButton
            :description: QtWidgets/QMessageBox-StandardButton-FirstButton-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.FlagMask
            :description: QtWidgets/QMessageBox-StandardButton-FlagMask-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.Help
            :description: QtWidgets/QMessageBox-StandardButton-Help-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.Ignore
            :description: QtWidgets/QMessageBox-StandardButton-Ignore-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.LastButton
            :description: QtWidgets/QMessageBox-StandardButton-LastButton-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.No
            :description: QtWidgets/QMessageBox-StandardButton-No-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.NoAll
            :description: QtWidgets/QMessageBox-StandardButton-NoAll-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.NoButton
            :description: QtWidgets/QMessageBox-StandardButton-NoButton-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.NoToAll
            :description: QtWidgets/QMessageBox-StandardButton-NoToAll-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.Ok
            :description: QtWidgets/QMessageBox-StandardButton-Ok-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.Open
            :description: QtWidgets/QMessageBox-StandardButton-Open-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.Reset
            :description: QtWidgets/QMessageBox-StandardButton-Reset-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.RestoreDefaults
            :description: QtWidgets/QMessageBox-StandardButton-RestoreDefaults-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.Retry
            :description: QtWidgets/QMessageBox-StandardButton-Retry-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.Save
            :description: QtWidgets/QMessageBox-StandardButton-Save-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.SaveAll
            :description: QtWidgets/QMessageBox-StandardButton-SaveAll-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.Yes
            :description: QtWidgets/QMessageBox-StandardButton-Yes-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.YesAll
            :description: QtWidgets/QMessageBox-StandardButton-YesAll-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButton.YesToAll
            :description: QtWidgets/QMessageBox-StandardButton-YesToAll-v.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QMessageBox-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.__init__
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.Icon`
            str
            str
            buttons: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton` = :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton.NoButton`
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
            flags: :sip:ref:`~PyQt6.QtCore.Qt.WindowType` = Qt.Dialog|Qt.MSWindowsFixedSizeDialogHint
        :description: QtWidgets/QMessageBox-__init__-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.about
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            str
            str
        :static:
        :description: QtWidgets/QMessageBox-about-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.aboutQt
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            title: str = ''
        :static:
        :description: QtWidgets/QMessageBox-aboutQt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.addButton
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QPushButton`
        :description: QtWidgets/QMessageBox-addButton-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.addButton
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractButton`
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.ButtonRole`
        :description: QtWidgets/QMessageBox-addButton-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.addButton
        :args:
            str
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.ButtonRole`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QPushButton`
        :description: QtWidgets/QMessageBox-addButton-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.button
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractButton`
        :description: QtWidgets/QMessageBox-button-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.buttonRole
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractButton`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.ButtonRole`
        :description: QtWidgets/QMessageBox-buttonRole-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.buttons
        :returns:
            List[:sip:ref:`~PyQt6.QtWidgets.QAbstractButton`]
        :description: QtWidgets/QMessageBox-buttons-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.changeEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtWidgets/QMessageBox-changeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.checkBox
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QCheckBox`
        :description: QtWidgets/QMessageBox-checkBox-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.clickedButton
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractButton`
        :description: QtWidgets/QMessageBox-clickedButton-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.closeEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QCloseEvent`
        :description: QtWidgets/QMessageBox-closeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.critical
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            str
            str
            buttons: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton` = :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton.Ok`
            defaultButton: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton` = :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton.NoButton`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton`
        :static:
        :description: QtWidgets/QMessageBox-critical-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.defaultButton
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QPushButton`
        :description: QtWidgets/QMessageBox-defaultButton-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.detailedText
        :returns:
            str
        :description: QtWidgets/QMessageBox-detailedText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.escapeButton
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractButton`
        :description: QtWidgets/QMessageBox-escapeButton-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QMessageBox-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.icon
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.Icon`
        :description: QtWidgets/QMessageBox-icon-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.iconPixmap
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtWidgets/QMessageBox-iconPixmap-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.information
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            str
            str
            buttons: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton` = :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton.Ok`
            defaultButton: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton` = :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton.NoButton`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton`
        :static:
        :description: QtWidgets/QMessageBox-information-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.informativeText
        :returns:
            str
        :description: QtWidgets/QMessageBox-informativeText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.keyPressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtWidgets/QMessageBox-keyPressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.open
        :description: QtWidgets/QMessageBox-open-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.open
        :args:
            PYQT_SLOT
        :description: QtWidgets/QMessageBox-open-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.question
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            str
            str
            buttons: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton` = QMessageBox.StandardButtons(QMessageBox.Yes|QMessageBox.No)
            defaultButton: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton` = :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton.NoButton`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton`
        :static:
        :description: QtWidgets/QMessageBox-question-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.removeButton
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractButton`
        :description: QtWidgets/QMessageBox-removeButton-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.resizeEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QResizeEvent`
        :description: QtWidgets/QMessageBox-resizeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.setCheckBox
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QCheckBox`
        :description: QtWidgets/QMessageBox-setCheckBox-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.setDefaultButton
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QPushButton`
        :description: QtWidgets/QMessageBox-setDefaultButton-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.setDefaultButton
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton`
        :description: QtWidgets/QMessageBox-setDefaultButton-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.setDetailedText
        :args:
            str
        :description: QtWidgets/QMessageBox-setDetailedText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.setEscapeButton
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractButton`
        :description: QtWidgets/QMessageBox-setEscapeButton-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.setEscapeButton
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton`
        :description: QtWidgets/QMessageBox-setEscapeButton-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.setIcon
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.Icon`
        :description: QtWidgets/QMessageBox-setIcon-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.setIconPixmap
        :args:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtWidgets/QMessageBox-setIconPixmap-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.setInformativeText
        :args:
            str
        :description: QtWidgets/QMessageBox-setInformativeText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.setStandardButtons
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton`
        :description: QtWidgets/QMessageBox-setStandardButtons-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.setText
        :args:
            str
        :description: QtWidgets/QMessageBox-setText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.setTextFormat
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.TextFormat`
        :description: QtWidgets/QMessageBox-setTextFormat-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.setTextInteractionFlags
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.TextInteractionFlag`
        :description: QtWidgets/QMessageBox-setTextInteractionFlags-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.setWindowModality
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.WindowModality`
        :description: QtWidgets/QMessageBox-setWindowModality-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.setWindowTitle
        :args:
            str
        :description: QtWidgets/QMessageBox-setWindowTitle-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.showEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QShowEvent`
        :description: QtWidgets/QMessageBox-showEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.standardButton
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractButton`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton`
        :description: QtWidgets/QMessageBox-standardButton-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.standardButtons
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton`
        :description: QtWidgets/QMessageBox-standardButtons-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.standardIcon
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.Icon`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :static:
        :description: QtWidgets/QMessageBox-standardIcon-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.text
        :returns:
            str
        :description: QtWidgets/QMessageBox-text-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.textFormat
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.TextFormat`
        :description: QtWidgets/QMessageBox-textFormat-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.textInteractionFlags
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.TextInteractionFlag`
        :description: QtWidgets/QMessageBox-textInteractionFlags-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.warning
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            str
            str
            buttons: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton` = :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton.Ok`
            defaultButton: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton` = :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton.NoButton`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButton`
        :static:
        :description: QtWidgets/QMessageBox-warning-f-1.rst

    .. sip:signal:: PyQt6.QtWidgets.QMessageBox.buttonClicked
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractButton`
        :description: QtWidgets/QMessageBox-buttonClicked-s.rst
