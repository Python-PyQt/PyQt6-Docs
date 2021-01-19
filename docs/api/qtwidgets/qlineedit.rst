:orphan:

.. sip:class:: PyQt6.QtWidgets.QLineEdit
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QWidget`
    :description: QtWidgets/QLineEdit-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QLineEdit.ActionPosition
        :description: QtWidgets/QLineEdit-ActionPosition-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QLineEdit.ActionPosition.LeadingPosition
            :description: QtWidgets/QLineEdit-ActionPosition-LeadingPosition-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QLineEdit.ActionPosition.TrailingPosition
            :description: QtWidgets/QLineEdit-ActionPosition-TrailingPosition-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QLineEdit.EchoMode
        :description: QtWidgets/QLineEdit-EchoMode-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QLineEdit.EchoMode.NoEcho
            :description: QtWidgets/QLineEdit-EchoMode-NoEcho-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QLineEdit.EchoMode.Normal
            :description: QtWidgets/QLineEdit-EchoMode-Normal-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QLineEdit.EchoMode.Password
            :description: QtWidgets/QLineEdit-EchoMode-Password-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit
            :description: QtWidgets/QLineEdit-EchoMode-PasswordEchoOnEdit-v.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QLineEdit-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.__init__
        :args:
            str
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QLineEdit-__init__-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.addAction
        :args:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtWidgets/QLineEdit-addAction-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.addAction
        :args:
            :sip:ref:`~PyQt6.QtGui.QAction`
            :sip:ref:`~PyQt6.QtWidgets.QLineEdit.ActionPosition`
        :description: QtWidgets/QLineEdit-addAction-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.addAction
        :args:
            :sip:ref:`~PyQt6.QtGui.QIcon`
            :sip:ref:`~PyQt6.QtWidgets.QLineEdit.ActionPosition`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAction`
        :description: QtWidgets/QLineEdit-addAction-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.alignment
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.Alignment`
        :description: QtWidgets/QLineEdit-alignment-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.backspace
        :description: QtWidgets/QLineEdit-backspace-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.changeEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtWidgets/QLineEdit-changeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.clear
        :description: QtWidgets/QLineEdit-clear-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.completer
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QCompleter`
        :description: QtWidgets/QLineEdit-completer-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.contextMenuEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QContextMenuEvent`
        :description: QtWidgets/QLineEdit-contextMenuEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.copy
        :description: QtWidgets/QLineEdit-copy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.createStandardContextMenu
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QMenu`
        :description: QtWidgets/QLineEdit-createStandardContextMenu-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.cursorBackward
        :args:
            bool
            steps: int = 1
        :description: QtWidgets/QLineEdit-cursorBackward-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.cursorForward
        :args:
            bool
            steps: int = 1
        :description: QtWidgets/QLineEdit-cursorForward-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.cursorMoveStyle
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.CursorMoveStyle`
        :description: QtWidgets/QLineEdit-cursorMoveStyle-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.cursorPosition
        :returns:
            int
        :description: QtWidgets/QLineEdit-cursorPosition-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.cursorPositionAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            int
        :description: QtWidgets/QLineEdit-cursorPositionAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.cursorRect
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QLineEdit-cursorRect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.cursorWordBackward
        :args:
            bool
        :description: QtWidgets/QLineEdit-cursorWordBackward-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.cursorWordForward
        :args:
            bool
        :description: QtWidgets/QLineEdit-cursorWordForward-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.cut
        :description: QtWidgets/QLineEdit-cut-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.del_
        :description: QtWidgets/QLineEdit-del_-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.deselect
        :description: QtWidgets/QLineEdit-deselect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.displayText
        :returns:
            str
        :description: QtWidgets/QLineEdit-displayText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.dragEnabled
        :returns:
            bool
        :description: QtWidgets/QLineEdit-dragEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.dragEnterEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDragEnterEvent`
        :description: QtWidgets/QLineEdit-dragEnterEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.dragLeaveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDragLeaveEvent`
        :description: QtWidgets/QLineEdit-dragLeaveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.dragMoveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDragMoveEvent`
        :description: QtWidgets/QLineEdit-dragMoveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.dropEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDropEvent`
        :description: QtWidgets/QLineEdit-dropEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.echoMode
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QLineEdit.EchoMode`
        :description: QtWidgets/QLineEdit-echoMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.end
        :args:
            bool
        :description: QtWidgets/QLineEdit-end-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QLineEdit-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.focusInEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QFocusEvent`
        :description: QtWidgets/QLineEdit-focusInEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.focusOutEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QFocusEvent`
        :description: QtWidgets/QLineEdit-focusOutEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.hasAcceptableInput
        :returns:
            bool
        :description: QtWidgets/QLineEdit-hasAcceptableInput-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.hasFrame
        :returns:
            bool
        :description: QtWidgets/QLineEdit-hasFrame-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.hasSelectedText
        :returns:
            bool
        :description: QtWidgets/QLineEdit-hasSelectedText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.home
        :args:
            bool
        :description: QtWidgets/QLineEdit-home-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.initStyleOption
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionFrame`
        :description: QtWidgets/QLineEdit-initStyleOption-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.inputMask
        :returns:
            str
        :description: QtWidgets/QLineEdit-inputMask-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.inputMethodEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QInputMethodEvent`
        :description: QtWidgets/QLineEdit-inputMethodEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.inputMethodQuery
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.InputMethodQueries`
        :returns:
            Any
        :description: QtWidgets/QLineEdit-inputMethodQuery-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.inputMethodQuery
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.InputMethodQueries`
            Any
        :returns:
            Any
        :description: QtWidgets/QLineEdit-inputMethodQuery-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.insert
        :args:
            str
        :description: QtWidgets/QLineEdit-insert-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.isClearButtonEnabled
        :returns:
            bool
        :description: QtWidgets/QLineEdit-isClearButtonEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.isModified
        :returns:
            bool
        :description: QtWidgets/QLineEdit-isModified-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.isReadOnly
        :returns:
            bool
        :description: QtWidgets/QLineEdit-isReadOnly-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.isRedoAvailable
        :returns:
            bool
        :description: QtWidgets/QLineEdit-isRedoAvailable-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.isUndoAvailable
        :returns:
            bool
        :description: QtWidgets/QLineEdit-isUndoAvailable-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.keyPressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtWidgets/QLineEdit-keyPressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.keyReleaseEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtWidgets/QLineEdit-keyReleaseEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.maxLength
        :returns:
            int
        :description: QtWidgets/QLineEdit-maxLength-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.minimumSizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QLineEdit-minimumSizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.mouseDoubleClickEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QLineEdit-mouseDoubleClickEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.mouseMoveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QLineEdit-mouseMoveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.mousePressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QLineEdit-mousePressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.mouseReleaseEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QLineEdit-mouseReleaseEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.paintEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QPaintEvent`
        :description: QtWidgets/QLineEdit-paintEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.paste
        :description: QtWidgets/QLineEdit-paste-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.placeholderText
        :returns:
            str
        :description: QtWidgets/QLineEdit-placeholderText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.redo
        :description: QtWidgets/QLineEdit-redo-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.selectAll
        :description: QtWidgets/QLineEdit-selectAll-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.selectedText
        :returns:
            str
        :description: QtWidgets/QLineEdit-selectedText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.selectionEnd
        :returns:
            int
        :description: QtWidgets/QLineEdit-selectionEnd-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.selectionLength
        :returns:
            int
        :description: QtWidgets/QLineEdit-selectionLength-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.selectionStart
        :returns:
            int
        :description: QtWidgets/QLineEdit-selectionStart-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.setAlignment
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.Alignment`
        :description: QtWidgets/QLineEdit-setAlignment-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.setClearButtonEnabled
        :args:
            bool
        :description: QtWidgets/QLineEdit-setClearButtonEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.setCompleter
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QCompleter`
        :description: QtWidgets/QLineEdit-setCompleter-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.setCursorMoveStyle
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.CursorMoveStyle`
        :description: QtWidgets/QLineEdit-setCursorMoveStyle-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.setCursorPosition
        :args:
            int
        :description: QtWidgets/QLineEdit-setCursorPosition-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.setDragEnabled
        :args:
            bool
        :description: QtWidgets/QLineEdit-setDragEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.setEchoMode
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QLineEdit.EchoMode`
        :description: QtWidgets/QLineEdit-setEchoMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.setFrame
        :args:
            bool
        :description: QtWidgets/QLineEdit-setFrame-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.setInputMask
        :args:
            str
        :description: QtWidgets/QLineEdit-setInputMask-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.setMaxLength
        :args:
            int
        :description: QtWidgets/QLineEdit-setMaxLength-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.setModified
        :args:
            bool
        :description: QtWidgets/QLineEdit-setModified-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.setPlaceholderText
        :args:
            str
        :description: QtWidgets/QLineEdit-setPlaceholderText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.setReadOnly
        :args:
            bool
        :description: QtWidgets/QLineEdit-setReadOnly-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.setSelection
        :args:
            int
            int
        :description: QtWidgets/QLineEdit-setSelection-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.setText
        :args:
            str
        :description: QtWidgets/QLineEdit-setText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.setTextMargins
        :args:
            :sip:ref:`~PyQt6.QtCore.QMargins`
        :description: QtWidgets/QLineEdit-setTextMargins-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.setTextMargins
        :args:
            int
            int
            int
            int
        :description: QtWidgets/QLineEdit-setTextMargins-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.setValidator
        :args:
            :sip:ref:`~PyQt6.QtGui.QValidator`
        :description: QtWidgets/QLineEdit-setValidator-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.sizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QLineEdit-sizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.text
        :returns:
            str
        :description: QtWidgets/QLineEdit-text-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.textMargins
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMargins`
        :description: QtWidgets/QLineEdit-textMargins-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.timerEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimerEvent`
        :description: QtWidgets/QLineEdit-timerEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.undo
        :description: QtWidgets/QLineEdit-undo-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLineEdit.validator
        :returns:
            :sip:ref:`~PyQt6.QtGui.QValidator`
        :description: QtWidgets/QLineEdit-validator-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QLineEdit.cursorPositionChanged
        :args:
            int
            int
        :description: QtWidgets/QLineEdit-cursorPositionChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QLineEdit.editingFinished
        :description: QtWidgets/QLineEdit-editingFinished-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QLineEdit.inputRejected
        :description: QtWidgets/QLineEdit-inputRejected-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QLineEdit.returnPressed
        :description: QtWidgets/QLineEdit-returnPressed-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QLineEdit.selectionChanged
        :description: QtWidgets/QLineEdit-selectionChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QLineEdit.textChanged
        :args:
            str
        :description: QtWidgets/QLineEdit-textChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QLineEdit.textEdited
        :args:
            str
        :description: QtWidgets/QLineEdit-textEdited-s.rst
