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

    .. sip:enum:: PyQt6.QtWidgets.QMessageBox.StandardButtons
        :description: QtWidgets/QMessageBox-StandardButtons-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.Abort
            :description: QtWidgets/QMessageBox-StandardButtons-Abort-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.Apply
            :description: QtWidgets/QMessageBox-StandardButtons-Apply-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.ButtonMask
            :description: QtWidgets/QMessageBox-StandardButtons-ButtonMask-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.Cancel
            :description: QtWidgets/QMessageBox-StandardButtons-Cancel-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.Close
            :description: QtWidgets/QMessageBox-StandardButtons-Close-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.Default
            :description: QtWidgets/QMessageBox-StandardButtons-Default-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.Discard
            :description: QtWidgets/QMessageBox-StandardButtons-Discard-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.Escape
            :description: QtWidgets/QMessageBox-StandardButtons-Escape-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.FirstButton
            :description: QtWidgets/QMessageBox-StandardButtons-FirstButton-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.FlagMask
            :description: QtWidgets/QMessageBox-StandardButtons-FlagMask-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.Help
            :description: QtWidgets/QMessageBox-StandardButtons-Help-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.Ignore
            :description: QtWidgets/QMessageBox-StandardButtons-Ignore-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.LastButton
            :description: QtWidgets/QMessageBox-StandardButtons-LastButton-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.No
            :description: QtWidgets/QMessageBox-StandardButtons-No-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.NoAll
            :description: QtWidgets/QMessageBox-StandardButtons-NoAll-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.NoButton
            :description: QtWidgets/QMessageBox-StandardButtons-NoButton-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.NoToAll
            :description: QtWidgets/QMessageBox-StandardButtons-NoToAll-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.Ok
            :description: QtWidgets/QMessageBox-StandardButtons-Ok-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.Open
            :description: QtWidgets/QMessageBox-StandardButtons-Open-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.Reset
            :description: QtWidgets/QMessageBox-StandardButtons-Reset-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.RestoreDefaults
            :description: QtWidgets/QMessageBox-StandardButtons-RestoreDefaults-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.Retry
            :description: QtWidgets/QMessageBox-StandardButtons-Retry-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.Save
            :description: QtWidgets/QMessageBox-StandardButtons-Save-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.SaveAll
            :description: QtWidgets/QMessageBox-StandardButtons-SaveAll-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.Yes
            :description: QtWidgets/QMessageBox-StandardButtons-Yes-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.YesAll
            :description: QtWidgets/QMessageBox-StandardButtons-YesAll-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QMessageBox.StandardButtons.YesToAll
            :description: QtWidgets/QMessageBox-StandardButtons-YesToAll-v.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QMessageBox-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.__init__
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.Icon`
            str
            str
            buttons: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons` = :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons.NoButton`
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
            flags: :sip:ref:`~PyQt6.QtCore.Qt.WindowFlags` = Qt.Dialog|Qt.MSWindowsFixedSizeDialogHint
        :description: QtWidgets/QMessageBox-__init__-f-1.rst

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
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QPushButton`
        :description: QtWidgets/QMessageBox-addButton-f.rst

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
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractButton`
        :description: QtWidgets/QMessageBox-button-f.rst

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
            buttons: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons` = :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons.Ok`
            defaultButton: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons` = :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons.NoButton`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons`
        :static:
        :description: QtWidgets/QMessageBox-critical-f.rst

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
            buttons: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons` = :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons.Ok`
            defaultButton: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons` = :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons.NoButton`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons`
        :static:
        :description: QtWidgets/QMessageBox-information-f.rst

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
            buttons: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons` = QMessageBox.StandardButtons(QMessageBox.Yes|QMessageBox.No)
            defaultButton: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons` = :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons.NoButton`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons`
        :static:
        :description: QtWidgets/QMessageBox-question-f.rst

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
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons`
        :description: QtWidgets/QMessageBox-setDefaultButton-f-1.rst

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
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons`
        :description: QtWidgets/QMessageBox-setEscapeButton-f-1.rst

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
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons`
        :description: QtWidgets/QMessageBox-setStandardButtons-f.rst

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
            :sip:ref:`~PyQt6.QtCore.Qt.TextInteractionFlags`
        :description: QtWidgets/QMessageBox-setTextInteractionFlags-f.rst

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
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons`
        :description: QtWidgets/QMessageBox-standardButton-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.standardButtons
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons`
        :description: QtWidgets/QMessageBox-standardButtons-f.rst

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
            :sip:ref:`~PyQt6.QtCore.Qt.TextInteractionFlags`
        :description: QtWidgets/QMessageBox-textInteractionFlags-f.rst

    .. sip:method:: PyQt6.QtWidgets.QMessageBox.warning
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            str
            str
            buttons: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons` = :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons.Ok`
            defaultButton: :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons` = :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons.NoButton`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QMessageBox.StandardButtons`
        :static:
        :description: QtWidgets/QMessageBox-warning-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QMessageBox.buttonClicked
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractButton`
        :description: QtWidgets/QMessageBox-buttonClicked-s.rst
