:orphan:

.. sip:class:: PyQt6.QtWidgets.QPlainTextEdit
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea`
    :description: QtWidgets/QPlainTextEdit-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QPlainTextEdit.LineWrapMode
        :description: QtWidgets/QPlainTextEdit-LineWrapMode-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QPlainTextEdit.LineWrapMode.NoWrap
            :description: QtWidgets/QPlainTextEdit-LineWrapMode-NoWrap-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QPlainTextEdit.LineWrapMode.WidgetWidth
            :description: QtWidgets/QPlainTextEdit-LineWrapMode-WidgetWidth-v.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QPlainTextEdit-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.__init__
        :args:
            Optional[str]
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QPlainTextEdit-__init__-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.anchorAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            str
        :description: QtWidgets/QPlainTextEdit-anchorAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.appendHtml
        :args:
            Optional[str]
        :description: QtWidgets/QPlainTextEdit-appendHtml-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.appendPlainText
        :args:
            Optional[str]
        :description: QtWidgets/QPlainTextEdit-appendPlainText-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.backgroundVisible
        :returns:
            bool
        :description: QtWidgets/QPlainTextEdit-backgroundVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.blockBoundingGeometry
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextBlock`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtWidgets/QPlainTextEdit-blockBoundingGeometry-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.blockBoundingRect
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextBlock`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtWidgets/QPlainTextEdit-blockBoundingRect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.blockCount
        :returns:
            int
        :description: QtWidgets/QPlainTextEdit-blockCount-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.canInsertFromMimeData
        :args:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
        :returns:
            bool
        :description: QtWidgets/QPlainTextEdit-canInsertFromMimeData-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.canPaste
        :returns:
            bool
        :description: QtWidgets/QPlainTextEdit-canPaste-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.centerCursor
        :description: QtWidgets/QPlainTextEdit-centerCursor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.centerOnScroll
        :returns:
            bool
        :description: QtWidgets/QPlainTextEdit-centerOnScroll-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.changeEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtWidgets/QPlainTextEdit-changeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.clear
        :description: QtWidgets/QPlainTextEdit-clear-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.contentOffset
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtWidgets/QPlainTextEdit-contentOffset-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.contextMenuEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QContextMenuEvent`
        :description: QtWidgets/QPlainTextEdit-contextMenuEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.copy
        :description: QtWidgets/QPlainTextEdit-copy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.createMimeDataFromSelection
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
        :description: QtWidgets/QPlainTextEdit-createMimeDataFromSelection-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.createStandardContextMenu
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QMenu`
        :description: QtWidgets/QPlainTextEdit-createStandardContextMenu-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.createStandardContextMenu
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QMenu`
        :description: QtWidgets/QPlainTextEdit-createStandardContextMenu-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.currentCharFormat
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextCharFormat`
        :description: QtWidgets/QPlainTextEdit-currentCharFormat-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.cursorForPosition
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextCursor`
        :description: QtWidgets/QPlainTextEdit-cursorForPosition-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.cursorRect
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QPlainTextEdit-cursorRect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.cursorRect
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextCursor`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QPlainTextEdit-cursorRect-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.cursorWidth
        :returns:
            int
        :description: QtWidgets/QPlainTextEdit-cursorWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.cut
        :description: QtWidgets/QPlainTextEdit-cut-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.document
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextDocument`
        :description: QtWidgets/QPlainTextEdit-document-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.documentTitle
        :returns:
            str
        :description: QtWidgets/QPlainTextEdit-documentTitle-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.dragEnterEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDragEnterEvent`
        :description: QtWidgets/QPlainTextEdit-dragEnterEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.dragLeaveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDragLeaveEvent`
        :description: QtWidgets/QPlainTextEdit-dragLeaveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.dragMoveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDragMoveEvent`
        :description: QtWidgets/QPlainTextEdit-dragMoveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.dropEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDropEvent`
        :description: QtWidgets/QPlainTextEdit-dropEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.ensureCursorVisible
        :description: QtWidgets/QPlainTextEdit-ensureCursorVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QPlainTextEdit-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.extraSelections
        :returns:
            list[:sip:ref:`~PyQt6.QtWidgets.QTextEdit.ExtraSelection`]
        :description: QtWidgets/QPlainTextEdit-extraSelections-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.find
        :args:
            Optional[str]
            options: :sip:ref:`~PyQt6.QtGui.QTextDocument.FindFlag` = QTextDocument.FindFlags()
        :returns:
            bool
        :description: QtWidgets/QPlainTextEdit-find-f-4.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.find
        :args:
            :sip:ref:`~PyQt6.QtCore.QRegularExpression`
            options: :sip:ref:`~PyQt6.QtGui.QTextDocument.FindFlag` = QTextDocument.FindFlags()
        :returns:
            bool
        :description: QtWidgets/QPlainTextEdit-find-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.firstVisibleBlock
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextBlock`
        :description: QtWidgets/QPlainTextEdit-firstVisibleBlock-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.focusInEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QFocusEvent`
        :description: QtWidgets/QPlainTextEdit-focusInEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.focusNextPrevChild
        :args:
            bool
        :returns:
            bool
        :description: QtWidgets/QPlainTextEdit-focusNextPrevChild-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.focusOutEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QFocusEvent`
        :description: QtWidgets/QPlainTextEdit-focusOutEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.getPaintContext
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAbstractTextDocumentLayout.PaintContext`
        :description: QtWidgets/QPlainTextEdit-getPaintContext-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.inputMethodEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QInputMethodEvent`
        :description: QtWidgets/QPlainTextEdit-inputMethodEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.inputMethodQuery
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.InputMethodQuery`
        :returns:
            Any
        :description: QtWidgets/QPlainTextEdit-inputMethodQuery-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.inputMethodQuery
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.InputMethodQuery`
            Any
        :returns:
            Any
        :description: QtWidgets/QPlainTextEdit-inputMethodQuery-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.insertFromMimeData
        :args:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
        :description: QtWidgets/QPlainTextEdit-insertFromMimeData-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.insertPlainText
        :args:
            Optional[str]
        :description: QtWidgets/QPlainTextEdit-insertPlainText-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.isReadOnly
        :returns:
            bool
        :description: QtWidgets/QPlainTextEdit-isReadOnly-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.isUndoRedoEnabled
        :returns:
            bool
        :description: QtWidgets/QPlainTextEdit-isUndoRedoEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.keyPressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtWidgets/QPlainTextEdit-keyPressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.keyReleaseEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtWidgets/QPlainTextEdit-keyReleaseEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.lineWrapMode
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.LineWrapMode`
        :description: QtWidgets/QPlainTextEdit-lineWrapMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.loadResource
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :returns:
            Any
        :description: QtWidgets/QPlainTextEdit-loadResource-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.maximumBlockCount
        :returns:
            int
        :description: QtWidgets/QPlainTextEdit-maximumBlockCount-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.mergeCurrentCharFormat
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextCharFormat`
        :description: QtWidgets/QPlainTextEdit-mergeCurrentCharFormat-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.mouseDoubleClickEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QPlainTextEdit-mouseDoubleClickEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.mouseMoveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QPlainTextEdit-mouseMoveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.mousePressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QPlainTextEdit-mousePressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.mouseReleaseEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QPlainTextEdit-mouseReleaseEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.moveCursor
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextCursor.MoveOperation`
            mode: :sip:ref:`~PyQt6.QtGui.QTextCursor.MoveMode` = :sip:ref:`~PyQt6.QtGui.QTextCursor.MoveMode.MoveAnchor`
        :description: QtWidgets/QPlainTextEdit-moveCursor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.overwriteMode
        :returns:
            bool
        :description: QtWidgets/QPlainTextEdit-overwriteMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.paintEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QPaintEvent`
        :description: QtWidgets/QPlainTextEdit-paintEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.paste
        :description: QtWidgets/QPlainTextEdit-paste-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.placeholderText
        :returns:
            str
        :description: QtWidgets/QPlainTextEdit-placeholderText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.print
        :args:
            :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice`
        :description: QtWidgets/QPlainTextEdit-print-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.redo
        :description: QtWidgets/QPlainTextEdit-redo-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.resizeEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QResizeEvent`
        :description: QtWidgets/QPlainTextEdit-resizeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.scrollContentsBy
        :args:
            int
            int
        :description: QtWidgets/QPlainTextEdit-scrollContentsBy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.selectAll
        :description: QtWidgets/QPlainTextEdit-selectAll-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.setBackgroundVisible
        :args:
            bool
        :description: QtWidgets/QPlainTextEdit-setBackgroundVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.setCenterOnScroll
        :args:
            bool
        :description: QtWidgets/QPlainTextEdit-setCenterOnScroll-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.setCurrentCharFormat
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextCharFormat`
        :description: QtWidgets/QPlainTextEdit-setCurrentCharFormat-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.setCursorWidth
        :args:
            int
        :description: QtWidgets/QPlainTextEdit-setCursorWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.setDocument
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextDocument`
        :description: QtWidgets/QPlainTextEdit-setDocument-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.setDocumentTitle
        :args:
            Optional[str]
        :description: QtWidgets/QPlainTextEdit-setDocumentTitle-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.setExtraSelections
        :args:
            Iterable[:sip:ref:`~PyQt6.QtWidgets.QTextEdit.ExtraSelection`]
        :description: QtWidgets/QPlainTextEdit-setExtraSelections-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.setLineWrapMode
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QPlainTextEdit.LineWrapMode`
        :description: QtWidgets/QPlainTextEdit-setLineWrapMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.setMaximumBlockCount
        :args:
            int
        :description: QtWidgets/QPlainTextEdit-setMaximumBlockCount-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.setOverwriteMode
        :args:
            bool
        :description: QtWidgets/QPlainTextEdit-setOverwriteMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.setPlaceholderText
        :args:
            Optional[str]
        :description: QtWidgets/QPlainTextEdit-setPlaceholderText-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.setPlainText
        :args:
            Optional[str]
        :description: QtWidgets/QPlainTextEdit-setPlainText-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.setReadOnly
        :args:
            bool
        :description: QtWidgets/QPlainTextEdit-setReadOnly-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.setTabChangesFocus
        :args:
            bool
        :description: QtWidgets/QPlainTextEdit-setTabChangesFocus-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.setTabStopDistance
        :args:
            float
        :description: QtWidgets/QPlainTextEdit-setTabStopDistance-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.setTextCursor
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextCursor`
        :description: QtWidgets/QPlainTextEdit-setTextCursor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.setTextInteractionFlags
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.TextInteractionFlag`
        :description: QtWidgets/QPlainTextEdit-setTextInteractionFlags-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.setUndoRedoEnabled
        :args:
            bool
        :description: QtWidgets/QPlainTextEdit-setUndoRedoEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.setWordWrapMode
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextOption.WrapMode`
        :description: QtWidgets/QPlainTextEdit-setWordWrapMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.showEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QShowEvent`
        :description: QtWidgets/QPlainTextEdit-showEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.tabChangesFocus
        :returns:
            bool
        :description: QtWidgets/QPlainTextEdit-tabChangesFocus-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.tabStopDistance
        :returns:
            float
        :description: QtWidgets/QPlainTextEdit-tabStopDistance-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.textCursor
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextCursor`
        :description: QtWidgets/QPlainTextEdit-textCursor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.textInteractionFlags
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.TextInteractionFlag`
        :description: QtWidgets/QPlainTextEdit-textInteractionFlags-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.timerEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimerEvent`
        :description: QtWidgets/QPlainTextEdit-timerEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.toPlainText
        :returns:
            str
        :description: QtWidgets/QPlainTextEdit-toPlainText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.undo
        :description: QtWidgets/QPlainTextEdit-undo-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.wheelEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QWheelEvent`
        :description: QtWidgets/QPlainTextEdit-wheelEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.wordWrapMode
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextOption.WrapMode`
        :description: QtWidgets/QPlainTextEdit-wordWrapMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.zoomIn
        :args:
            range: int = 1
        :description: QtWidgets/QPlainTextEdit-zoomIn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QPlainTextEdit.zoomOut
        :args:
            range: int = 1
        :description: QtWidgets/QPlainTextEdit-zoomOut-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QPlainTextEdit.blockCountChanged
        :args:
            int
        :description: QtWidgets/QPlainTextEdit-blockCountChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QPlainTextEdit.copyAvailable
        :args:
            bool
        :description: QtWidgets/QPlainTextEdit-copyAvailable-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QPlainTextEdit.cursorPositionChanged
        :description: QtWidgets/QPlainTextEdit-cursorPositionChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QPlainTextEdit.modificationChanged
        :args:
            bool
        :description: QtWidgets/QPlainTextEdit-modificationChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QPlainTextEdit.redoAvailable
        :args:
            bool
        :description: QtWidgets/QPlainTextEdit-redoAvailable-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QPlainTextEdit.selectionChanged
        :description: QtWidgets/QPlainTextEdit-selectionChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QPlainTextEdit.textChanged
        :description: QtWidgets/QPlainTextEdit-textChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QPlainTextEdit.undoAvailable
        :args:
            bool
        :description: QtWidgets/QPlainTextEdit-undoAvailable-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QPlainTextEdit.updateRequest
        :args:
            :sip:ref:`~PyQt6.QtCore.QRect`
            int
        :description: QtWidgets/QPlainTextEdit-updateRequest-s.rst
