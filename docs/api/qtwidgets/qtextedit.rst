:orphan:

.. sip:class:: PyQt6.QtWidgets.QTextEdit
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea`
    :description: QtWidgets/QTextEdit-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QTextEdit.AutoFormattingFlag
        :description: QtWidgets/QTextEdit-AutoFormattingFlag-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTextEdit.AutoFormattingFlag.AutoAll
            :description: QtWidgets/QTextEdit-AutoFormattingFlag-AutoAll-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTextEdit.AutoFormattingFlag.AutoBulletList
            :description: QtWidgets/QTextEdit-AutoFormattingFlag-AutoBulletList-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTextEdit.AutoFormattingFlag.AutoNone
            :description: QtWidgets/QTextEdit-AutoFormattingFlag-AutoNone-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QTextEdit.LineWrapMode
        :description: QtWidgets/QTextEdit-LineWrapMode-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTextEdit.LineWrapMode.FixedColumnWidth
            :description: QtWidgets/QTextEdit-LineWrapMode-FixedColumnWidth-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTextEdit.LineWrapMode.FixedPixelWidth
            :description: QtWidgets/QTextEdit-LineWrapMode-FixedPixelWidth-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTextEdit.LineWrapMode.NoWrap
            :description: QtWidgets/QTextEdit-LineWrapMode-NoWrap-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QTextEdit.LineWrapMode.WidgetWidth
            :description: QtWidgets/QTextEdit-LineWrapMode-WidgetWidth-v.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QTextEdit-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.__init__
        :args:
            str
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QTextEdit-__init__-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.acceptRichText
        :returns:
            bool
        :description: QtWidgets/QTextEdit-acceptRichText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.alignment
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag`
        :description: QtWidgets/QTextEdit-alignment-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.anchorAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            str
        :description: QtWidgets/QTextEdit-anchorAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.append
        :args:
            str
        :description: QtWidgets/QTextEdit-append-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.autoFormatting
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTextEdit.AutoFormattingFlag`
        :description: QtWidgets/QTextEdit-autoFormatting-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.canInsertFromMimeData
        :args:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
        :returns:
            bool
        :description: QtWidgets/QTextEdit-canInsertFromMimeData-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.canPaste
        :returns:
            bool
        :description: QtWidgets/QTextEdit-canPaste-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.changeEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtWidgets/QTextEdit-changeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.clear
        :description: QtWidgets/QTextEdit-clear-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.contextMenuEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QContextMenuEvent`
        :description: QtWidgets/QTextEdit-contextMenuEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.copy
        :description: QtWidgets/QTextEdit-copy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.createMimeDataFromSelection
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
        :description: QtWidgets/QTextEdit-createMimeDataFromSelection-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.createStandardContextMenu
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QMenu`
        :description: QtWidgets/QTextEdit-createStandardContextMenu-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.createStandardContextMenu
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QMenu`
        :description: QtWidgets/QTextEdit-createStandardContextMenu-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.currentCharFormat
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextCharFormat`
        :description: QtWidgets/QTextEdit-currentCharFormat-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.currentFont
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtWidgets/QTextEdit-currentFont-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.cursorForPosition
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextCursor`
        :description: QtWidgets/QTextEdit-cursorForPosition-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.cursorRect
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QTextEdit-cursorRect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.cursorRect
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextCursor`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QTextEdit-cursorRect-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.cursorWidth
        :returns:
            int
        :description: QtWidgets/QTextEdit-cursorWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.cut
        :description: QtWidgets/QTextEdit-cut-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.document
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextDocument`
        :description: QtWidgets/QTextEdit-document-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.documentTitle
        :returns:
            str
        :description: QtWidgets/QTextEdit-documentTitle-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.dragEnterEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDragEnterEvent`
        :description: QtWidgets/QTextEdit-dragEnterEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.dragLeaveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDragLeaveEvent`
        :description: QtWidgets/QTextEdit-dragLeaveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.dragMoveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDragMoveEvent`
        :description: QtWidgets/QTextEdit-dragMoveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.dropEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDropEvent`
        :description: QtWidgets/QTextEdit-dropEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.ensureCursorVisible
        :description: QtWidgets/QTextEdit-ensureCursorVisible-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QTextEdit-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.extraSelections
        :returns:
            List[:sip:ref:`~PyQt6.QtWidgets.QTextEdit.ExtraSelection`]
        :description: QtWidgets/QTextEdit-extraSelections-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.find
        :args:
            str
            options: :sip:ref:`~PyQt6.QtGui.QTextDocument.FindFlag` = QTextDocument.FindFlags()
        :returns:
            bool
        :description: QtWidgets/QTextEdit-find-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.find
        :args:
            :sip:ref:`~PyQt6.QtCore.QRegularExpression`
            options: :sip:ref:`~PyQt6.QtGui.QTextDocument.FindFlag` = QTextDocument.FindFlags()
        :returns:
            bool
        :description: QtWidgets/QTextEdit-find-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.focusInEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QFocusEvent`
        :description: QtWidgets/QTextEdit-focusInEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.focusNextPrevChild
        :args:
            bool
        :returns:
            bool
        :description: QtWidgets/QTextEdit-focusNextPrevChild-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.focusOutEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QFocusEvent`
        :description: QtWidgets/QTextEdit-focusOutEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.fontFamily
        :returns:
            str
        :description: QtWidgets/QTextEdit-fontFamily-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.fontItalic
        :returns:
            bool
        :description: QtWidgets/QTextEdit-fontItalic-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.fontPointSize
        :returns:
            float
        :description: QtWidgets/QTextEdit-fontPointSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.fontUnderline
        :returns:
            bool
        :description: QtWidgets/QTextEdit-fontUnderline-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.fontWeight
        :returns:
            int
        :description: QtWidgets/QTextEdit-fontWeight-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.inputMethodEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QInputMethodEvent`
        :description: QtWidgets/QTextEdit-inputMethodEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.inputMethodQuery
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.InputMethodQuery`
        :returns:
            Any
        :description: QtWidgets/QTextEdit-inputMethodQuery-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.inputMethodQuery
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.InputMethodQuery`
            Any
        :returns:
            Any
        :description: QtWidgets/QTextEdit-inputMethodQuery-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.insertFromMimeData
        :args:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
        :description: QtWidgets/QTextEdit-insertFromMimeData-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.insertHtml
        :args:
            str
        :description: QtWidgets/QTextEdit-insertHtml-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.insertPlainText
        :args:
            str
        :description: QtWidgets/QTextEdit-insertPlainText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.isReadOnly
        :returns:
            bool
        :description: QtWidgets/QTextEdit-isReadOnly-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.isUndoRedoEnabled
        :returns:
            bool
        :description: QtWidgets/QTextEdit-isUndoRedoEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.keyPressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtWidgets/QTextEdit-keyPressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.keyReleaseEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtWidgets/QTextEdit-keyReleaseEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.lineWrapColumnOrWidth
        :returns:
            int
        :description: QtWidgets/QTextEdit-lineWrapColumnOrWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.lineWrapMode
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTextEdit.LineWrapMode`
        :description: QtWidgets/QTextEdit-lineWrapMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.loadResource
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :returns:
            Any
        :description: QtWidgets/QTextEdit-loadResource-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.mergeCurrentCharFormat
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextCharFormat`
        :description: QtWidgets/QTextEdit-mergeCurrentCharFormat-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.mouseDoubleClickEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QTextEdit-mouseDoubleClickEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.mouseMoveEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QTextEdit-mouseMoveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.mousePressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QTextEdit-mousePressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.mouseReleaseEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QTextEdit-mouseReleaseEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.moveCursor
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextCursor.MoveOperation`
            mode: :sip:ref:`~PyQt6.QtGui.QTextCursor.MoveMode` = :sip:ref:`~PyQt6.QtGui.QTextCursor.MoveMode.MoveAnchor`
        :description: QtWidgets/QTextEdit-moveCursor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.overwriteMode
        :returns:
            bool
        :description: QtWidgets/QTextEdit-overwriteMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.paintEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QPaintEvent`
        :description: QtWidgets/QTextEdit-paintEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.paste
        :description: QtWidgets/QTextEdit-paste-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.placeholderText
        :returns:
            str
        :description: QtWidgets/QTextEdit-placeholderText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.print
        :args:
            :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice`
        :description: QtWidgets/QTextEdit-print-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.redo
        :description: QtWidgets/QTextEdit-redo-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.resizeEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QResizeEvent`
        :description: QtWidgets/QTextEdit-resizeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.scrollContentsBy
        :args:
            int
            int
        :description: QtWidgets/QTextEdit-scrollContentsBy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.scrollToAnchor
        :args:
            str
        :description: QtWidgets/QTextEdit-scrollToAnchor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.selectAll
        :description: QtWidgets/QTextEdit-selectAll-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setAcceptRichText
        :args:
            bool
        :description: QtWidgets/QTextEdit-setAcceptRichText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setAlignment
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag`
        :description: QtWidgets/QTextEdit-setAlignment-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setAutoFormatting
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTextEdit.AutoFormattingFlag`
        :description: QtWidgets/QTextEdit-setAutoFormatting-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setCurrentCharFormat
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextCharFormat`
        :description: QtWidgets/QTextEdit-setCurrentCharFormat-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setCurrentFont
        :args:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtWidgets/QTextEdit-setCurrentFont-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setCursorWidth
        :args:
            int
        :description: QtWidgets/QTextEdit-setCursorWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setDocument
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextDocument`
        :description: QtWidgets/QTextEdit-setDocument-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setDocumentTitle
        :args:
            str
        :description: QtWidgets/QTextEdit-setDocumentTitle-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setExtraSelections
        :args:
            Iterable[:sip:ref:`~PyQt6.QtWidgets.QTextEdit.ExtraSelection`]
        :description: QtWidgets/QTextEdit-setExtraSelections-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setFontFamily
        :args:
            str
        :description: QtWidgets/QTextEdit-setFontFamily-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setFontItalic
        :args:
            bool
        :description: QtWidgets/QTextEdit-setFontItalic-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setFontPointSize
        :args:
            float
        :description: QtWidgets/QTextEdit-setFontPointSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setFontUnderline
        :args:
            bool
        :description: QtWidgets/QTextEdit-setFontUnderline-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setFontWeight
        :args:
            int
        :description: QtWidgets/QTextEdit-setFontWeight-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setHtml
        :args:
            str
        :description: QtWidgets/QTextEdit-setHtml-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setLineWrapColumnOrWidth
        :args:
            int
        :description: QtWidgets/QTextEdit-setLineWrapColumnOrWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setLineWrapMode
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTextEdit.LineWrapMode`
        :description: QtWidgets/QTextEdit-setLineWrapMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setMarkdown
        :args:
            str
        :description: QtWidgets/QTextEdit-setMarkdown-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setOverwriteMode
        :args:
            bool
        :description: QtWidgets/QTextEdit-setOverwriteMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setPlaceholderText
        :args:
            str
        :description: QtWidgets/QTextEdit-setPlaceholderText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setPlainText
        :args:
            str
        :description: QtWidgets/QTextEdit-setPlainText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setReadOnly
        :args:
            bool
        :description: QtWidgets/QTextEdit-setReadOnly-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setTabChangesFocus
        :args:
            bool
        :description: QtWidgets/QTextEdit-setTabChangesFocus-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setTabStopDistance
        :args:
            float
        :description: QtWidgets/QTextEdit-setTabStopDistance-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setText
        :args:
            str
        :description: QtWidgets/QTextEdit-setText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setTextBackgroundColor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int, :sip:ref:`~PyQt6.QtGui.QGradient`]
        :description: QtWidgets/QTextEdit-setTextBackgroundColor-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setTextColor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int, :sip:ref:`~PyQt6.QtGui.QGradient`]
        :description: QtWidgets/QTextEdit-setTextColor-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setTextCursor
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextCursor`
        :description: QtWidgets/QTextEdit-setTextCursor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setTextInteractionFlags
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.TextInteractionFlag`
        :description: QtWidgets/QTextEdit-setTextInteractionFlags-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setUndoRedoEnabled
        :args:
            bool
        :description: QtWidgets/QTextEdit-setUndoRedoEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.setWordWrapMode
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextOption.WrapMode`
        :description: QtWidgets/QTextEdit-setWordWrapMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.showEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QShowEvent`
        :description: QtWidgets/QTextEdit-showEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.tabChangesFocus
        :returns:
            bool
        :description: QtWidgets/QTextEdit-tabChangesFocus-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.tabStopDistance
        :returns:
            float
        :description: QtWidgets/QTextEdit-tabStopDistance-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.textBackgroundColor
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtWidgets/QTextEdit-textBackgroundColor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.textColor
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtWidgets/QTextEdit-textColor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.textCursor
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextCursor`
        :description: QtWidgets/QTextEdit-textCursor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.textInteractionFlags
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.TextInteractionFlag`
        :description: QtWidgets/QTextEdit-textInteractionFlags-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.timerEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimerEvent`
        :description: QtWidgets/QTextEdit-timerEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.toHtml
        :returns:
            str
        :description: QtWidgets/QTextEdit-toHtml-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.toMarkdown
        :args:
            features: :sip:ref:`~PyQt6.QtGui.QTextDocument.MarkdownFeature` = :sip:ref:`~PyQt6.QtGui.QTextDocument.MarkdownFeature.MarkdownDialectGitHub`
        :returns:
            str
        :description: QtWidgets/QTextEdit-toMarkdown-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.toPlainText
        :returns:
            str
        :description: QtWidgets/QTextEdit-toPlainText-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.undo
        :description: QtWidgets/QTextEdit-undo-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.wheelEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QWheelEvent`
        :description: QtWidgets/QTextEdit-wheelEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.wordWrapMode
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextOption.WrapMode`
        :description: QtWidgets/QTextEdit-wordWrapMode-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.zoomIn
        :args:
            range: int = 1
        :description: QtWidgets/QTextEdit-zoomIn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTextEdit.zoomOut
        :args:
            range: int = 1
        :description: QtWidgets/QTextEdit-zoomOut-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QTextEdit.copyAvailable
        :args:
            bool
        :description: QtWidgets/QTextEdit-copyAvailable-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTextEdit.currentCharFormatChanged
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextCharFormat`
        :description: QtWidgets/QTextEdit-currentCharFormatChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTextEdit.cursorPositionChanged
        :description: QtWidgets/QTextEdit-cursorPositionChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTextEdit.redoAvailable
        :args:
            bool
        :description: QtWidgets/QTextEdit-redoAvailable-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTextEdit.selectionChanged
        :description: QtWidgets/QTextEdit-selectionChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTextEdit.textChanged
        :description: QtWidgets/QTextEdit-textChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTextEdit.undoAvailable
        :args:
            bool
        :description: QtWidgets/QTextEdit-undoAvailable-s.rst
