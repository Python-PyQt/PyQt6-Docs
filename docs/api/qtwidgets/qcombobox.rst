:orphan:

.. sip:class:: PyQt6.QtWidgets.QComboBox
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QWidget`
    :description: QtWidgets/QComboBox-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QComboBox.InsertPolicy
        :description: QtWidgets/QComboBox-InsertPolicy-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QComboBox.InsertPolicy.InsertAfterCurrent
            :description: QtWidgets/QComboBox-InsertPolicy-InsertAfterCurrent-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QComboBox.InsertPolicy.InsertAlphabetically
            :description: QtWidgets/QComboBox-InsertPolicy-InsertAlphabetically-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QComboBox.InsertPolicy.InsertAtBottom
            :description: QtWidgets/QComboBox-InsertPolicy-InsertAtBottom-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QComboBox.InsertPolicy.InsertAtCurrent
            :description: QtWidgets/QComboBox-InsertPolicy-InsertAtCurrent-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QComboBox.InsertPolicy.InsertAtTop
            :description: QtWidgets/QComboBox-InsertPolicy-InsertAtTop-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QComboBox.InsertPolicy.InsertBeforeCurrent
            :description: QtWidgets/QComboBox-InsertPolicy-InsertBeforeCurrent-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QComboBox.InsertPolicy.NoInsert
            :description: QtWidgets/QComboBox-InsertPolicy-NoInsert-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QComboBox.SizeAdjustPolicy
        :description: QtWidgets/QComboBox-SizeAdjustPolicy-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents
            :description: QtWidgets/QComboBox-SizeAdjustPolicy-AdjustToContents-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow
            :description: QtWidgets/QComboBox-SizeAdjustPolicy-AdjustToContentsOnFirstShow-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon
            :description: QtWidgets/QComboBox-SizeAdjustPolicy-AdjustToMinimumContentsLengthWithIcon-v.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QComboBox-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.addItem
        :args:
            str
            userData: Any = None
        :description: QtWidgets/QComboBox-addItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.addItem
        :args:
            :sip:ref:`~PyQt6.QtGui.QIcon`
            str
            userData: Any = None
        :description: QtWidgets/QComboBox-addItem-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.addItems
        :args:
            Iterable[str]
        :description: QtWidgets/QComboBox-addItems-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.changeEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtWidgets/QComboBox-changeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.clear
        :description: QtWidgets/QComboBox-clear-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.clearEditText
        :description: QtWidgets/QComboBox-clearEditText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.completer
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QCompleter`
        :description: QtWidgets/QComboBox-completer-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.contextMenuEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QContextMenuEvent`
        :description: QtWidgets/QComboBox-contextMenuEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.count
        :returns:
            int
        :description: QtWidgets/QComboBox-count-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.currentData
        :args:
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.UserRole`
        :returns:
            Any
        :description: QtWidgets/QComboBox-currentData-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.currentIndex
        :returns:
            int
        :description: QtWidgets/QComboBox-currentIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.currentText
        :returns:
            str
        :description: QtWidgets/QComboBox-currentText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.duplicatesEnabled
        :returns:
            bool
        :description: QtWidgets/QComboBox-duplicatesEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QComboBox-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.findData
        :args:
            Any
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.UserRole`
            flags: :sip:ref:`~PyQt6.QtCore.Qt.MatchFlag` = unknown-type(Qt.MatchExactly|Qt.MatchCaseSensitive)
        :returns:
            int
        :description: QtWidgets/QComboBox-findData-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.findText
        :args:
            str
            flags: :sip:ref:`~PyQt6.QtCore.Qt.MatchFlag` = unknown-type(Qt.MatchExactly|Qt.MatchCaseSensitive)
        :returns:
            int
        :description: QtWidgets/QComboBox-findText-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.focusInEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QFocusEvent`
        :description: QtWidgets/QComboBox-focusInEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.focusOutEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QFocusEvent`
        :description: QtWidgets/QComboBox-focusOutEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.hasFrame
        :returns:
            bool
        :description: QtWidgets/QComboBox-hasFrame-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.hideEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QHideEvent`
        :description: QtWidgets/QComboBox-hideEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.hidePopup
        :description: QtWidgets/QComboBox-hidePopup-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.iconSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QComboBox-iconSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.initStyleOption
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionComboBox`
        :description: QtWidgets/QComboBox-initStyleOption-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.inputMethodEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QInputMethodEvent`
        :description: QtWidgets/QComboBox-inputMethodEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.inputMethodQuery
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.InputMethodQuery`
        :returns:
            Any
        :description: QtWidgets/QComboBox-inputMethodQuery-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.inputMethodQuery
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.InputMethodQuery`
            Any
        :returns:
            Any
        :description: QtWidgets/QComboBox-inputMethodQuery-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.insertItem
        :args:
            int
            str
            userData: Any = None
        :description: QtWidgets/QComboBox-insertItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.insertItem
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QIcon`
            str
            userData: Any = None
        :description: QtWidgets/QComboBox-insertItem-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.insertItems
        :args:
            int
            Iterable[str]
        :description: QtWidgets/QComboBox-insertItems-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.insertPolicy
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QComboBox.InsertPolicy`
        :description: QtWidgets/QComboBox-insertPolicy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.insertSeparator
        :args:
            int
        :description: QtWidgets/QComboBox-insertSeparator-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.isEditable
        :returns:
            bool
        :description: QtWidgets/QComboBox-isEditable-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.itemData
        :args:
            int
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.UserRole`
        :returns:
            Any
        :description: QtWidgets/QComboBox-itemData-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.itemDelegate
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate`
        :description: QtWidgets/QComboBox-itemDelegate-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.itemIcon
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QIcon`
        :description: QtWidgets/QComboBox-itemIcon-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.itemText
        :args:
            int
        :returns:
            str
        :description: QtWidgets/QComboBox-itemText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.keyPressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtWidgets/QComboBox-keyPressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.keyReleaseEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtWidgets/QComboBox-keyReleaseEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.__len__
        :returns:
            int
        :description: QtWidgets/QComboBox-__len__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.lineEdit
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QLineEdit`
        :description: QtWidgets/QComboBox-lineEdit-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.maxCount
        :returns:
            int
        :description: QtWidgets/QComboBox-maxCount-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.maxVisibleItems
        :returns:
            int
        :description: QtWidgets/QComboBox-maxVisibleItems-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.minimumContentsLength
        :returns:
            int
        :description: QtWidgets/QComboBox-minimumContentsLength-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.minimumSizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QComboBox-minimumSizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.model
        :returns:
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
        :description: QtWidgets/QComboBox-model-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.modelColumn
        :returns:
            int
        :description: QtWidgets/QComboBox-modelColumn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.mousePressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QComboBox-mousePressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.mouseReleaseEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QComboBox-mouseReleaseEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.paintEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QPaintEvent`
        :description: QtWidgets/QComboBox-paintEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.placeholderText
        :returns:
            str
        :description: QtWidgets/QComboBox-placeholderText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.removeItem
        :args:
            int
        :description: QtWidgets/QComboBox-removeItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.resizeEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QResizeEvent`
        :description: QtWidgets/QComboBox-resizeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.rootModelIndex
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QComboBox-rootModelIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.setCompleter
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QCompleter`
        :description: QtWidgets/QComboBox-setCompleter-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.setCurrentIndex
        :args:
            int
        :description: QtWidgets/QComboBox-setCurrentIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.setCurrentText
        :args:
            str
        :description: QtWidgets/QComboBox-setCurrentText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.setDuplicatesEnabled
        :args:
            bool
        :description: QtWidgets/QComboBox-setDuplicatesEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.setEditable
        :args:
            bool
        :description: QtWidgets/QComboBox-setEditable-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.setEditText
        :args:
            str
        :description: QtWidgets/QComboBox-setEditText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.setFrame
        :args:
            bool
        :description: QtWidgets/QComboBox-setFrame-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.setIconSize
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QComboBox-setIconSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.setInsertPolicy
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QComboBox.InsertPolicy`
        :description: QtWidgets/QComboBox-setInsertPolicy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.setItemData
        :args:
            int
            Any
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.UserRole`
        :description: QtWidgets/QComboBox-setItemData-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.setItemDelegate
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate`
        :description: QtWidgets/QComboBox-setItemDelegate-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.setItemIcon
        :args:
            int
            :sip:ref:`~PyQt6.QtGui.QIcon`
        :description: QtWidgets/QComboBox-setItemIcon-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.setItemText
        :args:
            int
            str
        :description: QtWidgets/QComboBox-setItemText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.setLineEdit
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QLineEdit`
        :description: QtWidgets/QComboBox-setLineEdit-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.setMaxCount
        :args:
            int
        :description: QtWidgets/QComboBox-setMaxCount-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.setMaxVisibleItems
        :args:
            int
        :description: QtWidgets/QComboBox-setMaxVisibleItems-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.setMinimumContentsLength
        :args:
            int
        :description: QtWidgets/QComboBox-setMinimumContentsLength-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.setModel
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
        :description: QtWidgets/QComboBox-setModel-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.setModelColumn
        :args:
            int
        :description: QtWidgets/QComboBox-setModelColumn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.setPlaceholderText
        :args:
            str
        :description: QtWidgets/QComboBox-setPlaceholderText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.setRootModelIndex
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QComboBox-setRootModelIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.setSizeAdjustPolicy
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QComboBox.SizeAdjustPolicy`
        :description: QtWidgets/QComboBox-setSizeAdjustPolicy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.setValidator
        :args:
            :sip:ref:`~PyQt6.QtGui.QValidator`
        :description: QtWidgets/QComboBox-setValidator-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.setView
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView`
        :description: QtWidgets/QComboBox-setView-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.showEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QShowEvent`
        :description: QtWidgets/QComboBox-showEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.showPopup
        :description: QtWidgets/QComboBox-showPopup-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.sizeAdjustPolicy
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QComboBox.SizeAdjustPolicy`
        :description: QtWidgets/QComboBox-sizeAdjustPolicy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.sizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QComboBox-sizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.validator
        :returns:
            :sip:ref:`~PyQt6.QtGui.QValidator`
        :description: QtWidgets/QComboBox-validator-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.view
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView`
        :description: QtWidgets/QComboBox-view-f.rst

    .. sip:method:: PyQt6.QtWidgets.QComboBox.wheelEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QWheelEvent`
        :description: QtWidgets/QComboBox-wheelEvent-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QComboBox.activated
        :args:
            int
        :description: QtWidgets/QComboBox-activated-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QComboBox.currentIndexChanged
        :args:
            int
        :description: QtWidgets/QComboBox-currentIndexChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QComboBox.currentTextChanged
        :args:
            str
        :description: QtWidgets/QComboBox-currentTextChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QComboBox.editTextChanged
        :args:
            str
        :description: QtWidgets/QComboBox-editTextChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QComboBox.highlighted
        :args:
            int
        :description: QtWidgets/QComboBox-highlighted-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QComboBox.textActivated
        :args:
            str
        :description: QtWidgets/QComboBox-textActivated-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QComboBox.textHighlighted
        :args:
            str
        :description: QtWidgets/QComboBox-textHighlighted-s.rst
