:orphan:

.. sip:class:: PyQt6.QtGui.QTextDocument
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtGui/QTextDocument-c.rst

    .. sip:enum:: PyQt6.QtGui.QTextDocument.FindFlags
        :description: QtGui/QTextDocument-FindFlags-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QTextDocument.FindFlags.FindBackward
            :description: QtGui/QTextDocument-FindFlags-FindBackward-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QTextDocument.FindFlags.FindCaseSensitively
            :description: QtGui/QTextDocument-FindFlags-FindCaseSensitively-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QTextDocument.FindFlags.FindWholeWords
            :description: QtGui/QTextDocument-FindFlags-FindWholeWords-v.rst

    .. sip:enum:: PyQt6.QtGui.QTextDocument.MarkdownFeatures
        :description: QtGui/QTextDocument-MarkdownFeatures-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QTextDocument.MarkdownFeatures.MarkdownDialectCommonMark
            :description: QtGui/QTextDocument-MarkdownFeatures-MarkdownDialectCommonMark-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QTextDocument.MarkdownFeatures.MarkdownDialectGitHub
            :description: QtGui/QTextDocument-MarkdownFeatures-MarkdownDialectGitHub-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QTextDocument.MarkdownFeatures.MarkdownNoHTML
            :description: QtGui/QTextDocument-MarkdownFeatures-MarkdownNoHTML-v.rst

    .. sip:enum:: PyQt6.QtGui.QTextDocument.MetaInformation
        :description: QtGui/QTextDocument-MetaInformation-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QTextDocument.MetaInformation.DocumentTitle
            :description: QtGui/QTextDocument-MetaInformation-DocumentTitle-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QTextDocument.MetaInformation.DocumentUrl
            :description: QtGui/QTextDocument-MetaInformation-DocumentUrl-v.rst

    .. sip:enum:: PyQt6.QtGui.QTextDocument.ResourceType
        :description: QtGui/QTextDocument-ResourceType-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QTextDocument.ResourceType.HtmlResource
            :description: QtGui/QTextDocument-ResourceType-HtmlResource-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QTextDocument.ResourceType.ImageResource
            :description: QtGui/QTextDocument-ResourceType-ImageResource-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QTextDocument.ResourceType.MarkdownResource
            :description: QtGui/QTextDocument-ResourceType-MarkdownResource-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QTextDocument.ResourceType.StyleSheetResource
            :description: QtGui/QTextDocument-ResourceType-StyleSheetResource-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QTextDocument.ResourceType.UnknownResource
            :description: QtGui/QTextDocument-ResourceType-UnknownResource-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QTextDocument.ResourceType.UserResource
            :description: QtGui/QTextDocument-ResourceType-UserResource-v.rst

    .. sip:enum:: PyQt6.QtGui.QTextDocument.Stacks
        :description: QtGui/QTextDocument-Stacks-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QTextDocument.Stacks.RedoStack
            :description: QtGui/QTextDocument-Stacks-RedoStack-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QTextDocument.Stacks.UndoAndRedoStacks
            :description: QtGui/QTextDocument-Stacks-UndoAndRedoStacks-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QTextDocument.Stacks.UndoStack
            :description: QtGui/QTextDocument-Stacks-UndoStack-v.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGui/QTextDocument-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.__init__
        :args:
            str
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGui/QTextDocument-__init__-f-1.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.addResource
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QUrl`
            Any
        :description: QtGui/QTextDocument-addResource-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.adjustSize
        :description: QtGui/QTextDocument-adjustSize-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.allFormats
        :returns:
            List[:sip:ref:`~PyQt6.QtGui.QTextFormat`]
        :description: QtGui/QTextDocument-allFormats-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.availableRedoSteps
        :returns:
            int
        :description: QtGui/QTextDocument-availableRedoSteps-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.availableUndoSteps
        :returns:
            int
        :description: QtGui/QTextDocument-availableUndoSteps-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.baselineOffset
        :returns:
            float
        :description: QtGui/QTextDocument-baselineOffset-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.baseUrl
        :returns:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtGui/QTextDocument-baseUrl-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.begin
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextBlock`
        :description: QtGui/QTextDocument-begin-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.blockCount
        :returns:
            int
        :description: QtGui/QTextDocument-blockCount-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.characterAt
        :args:
            int
        :returns:
            str
        :description: QtGui/QTextDocument-characterAt-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.characterCount
        :returns:
            int
        :description: QtGui/QTextDocument-characterCount-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.clear
        :description: QtGui/QTextDocument-clear-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.clearUndoRedoStacks
        :args:
            stacks: :sip:ref:`~PyQt6.QtGui.QTextDocument.Stacks` = :sip:ref:`~PyQt6.QtGui.QTextDocument.Stacks.UndoAndRedoStacks`
        :description: QtGui/QTextDocument-clearUndoRedoStacks-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.clone
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextDocument`
        :description: QtGui/QTextDocument-clone-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.createObject
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextFormat`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextObject`
        :description: QtGui/QTextDocument-createObject-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.defaultCursorMoveStyle
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.CursorMoveStyle`
        :description: QtGui/QTextDocument-defaultCursorMoveStyle-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.defaultFont
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtGui/QTextDocument-defaultFont-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.defaultStyleSheet
        :returns:
            str
        :description: QtGui/QTextDocument-defaultStyleSheet-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.defaultTextOption
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextOption`
        :description: QtGui/QTextDocument-defaultTextOption-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.documentLayout
        :returns:
            :sip:ref:`~PyQt6.QtGui.QAbstractTextDocumentLayout`
        :description: QtGui/QTextDocument-documentLayout-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.documentMargin
        :returns:
            float
        :description: QtGui/QTextDocument-documentMargin-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.drawContents
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            rect: :sip:ref:`~PyQt6.QtCore.QRectF` = QRectF()
        :description: QtGui/QTextDocument-drawContents-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.end
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextBlock`
        :description: QtGui/QTextDocument-end-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.find
        :args:
            :sip:ref:`~PyQt6.QtCore.QRegularExpression`
            :sip:ref:`~PyQt6.QtGui.QTextCursor`
            options: :sip:ref:`~PyQt6.QtGui.QTextDocument.FindFlags` = QTextDocument.FindFlags()
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextCursor`
        :description: QtGui/QTextDocument-find-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.find
        :args:
            :sip:ref:`~PyQt6.QtCore.QRegularExpression`
            position: int = 0
            options: :sip:ref:`~PyQt6.QtGui.QTextDocument.FindFlags` = QTextDocument.FindFlags()
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextCursor`
        :description: QtGui/QTextDocument-find-f-1.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.find
        :args:
            str
            :sip:ref:`~PyQt6.QtGui.QTextCursor`
            options: :sip:ref:`~PyQt6.QtGui.QTextDocument.FindFlags` = QTextDocument.FindFlags()
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextCursor`
        :description: QtGui/QTextDocument-find-f-2.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.find
        :args:
            str
            position: int = 0
            options: :sip:ref:`~PyQt6.QtGui.QTextDocument.FindFlags` = QTextDocument.FindFlags()
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextCursor`
        :description: QtGui/QTextDocument-find-f-3.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.findBlock
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextBlock`
        :description: QtGui/QTextDocument-findBlock-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.findBlockByLineNumber
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextBlock`
        :description: QtGui/QTextDocument-findBlockByLineNumber-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.findBlockByNumber
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextBlock`
        :description: QtGui/QTextDocument-findBlockByNumber-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.firstBlock
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextBlock`
        :description: QtGui/QTextDocument-firstBlock-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.idealWidth
        :returns:
            float
        :description: QtGui/QTextDocument-idealWidth-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.indentWidth
        :returns:
            float
        :description: QtGui/QTextDocument-indentWidth-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.isEmpty
        :returns:
            bool
        :description: QtGui/QTextDocument-isEmpty-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.isModified
        :returns:
            bool
        :description: QtGui/QTextDocument-isModified-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.isRedoAvailable
        :returns:
            bool
        :description: QtGui/QTextDocument-isRedoAvailable-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.isUndoAvailable
        :returns:
            bool
        :description: QtGui/QTextDocument-isUndoAvailable-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.isUndoRedoEnabled
        :returns:
            bool
        :description: QtGui/QTextDocument-isUndoRedoEnabled-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.lastBlock
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextBlock`
        :description: QtGui/QTextDocument-lastBlock-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.lineCount
        :returns:
            int
        :description: QtGui/QTextDocument-lineCount-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.loadResource
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :returns:
            Any
        :description: QtGui/QTextDocument-loadResource-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.markContentsDirty
        :args:
            int
            int
        :description: QtGui/QTextDocument-markContentsDirty-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.maximumBlockCount
        :returns:
            int
        :description: QtGui/QTextDocument-maximumBlockCount-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.metaInformation
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextDocument.MetaInformation`
        :returns:
            str
        :description: QtGui/QTextDocument-metaInformation-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.object
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextObject`
        :description: QtGui/QTextDocument-object-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.objectForFormat
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextFormat`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextObject`
        :description: QtGui/QTextDocument-objectForFormat-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.pageCount
        :returns:
            int
        :description: QtGui/QTextDocument-pageCount-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.pageSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSizeF`
        :description: QtGui/QTextDocument-pageSize-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.print
        :args:
            :sip:ref:`~PyQt6.QtGui.QPagedPaintDevice`
        :description: QtGui/QTextDocument-print-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.redo
        :description: QtGui/QTextDocument-redo-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.redo
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextCursor`
        :description: QtGui/QTextDocument-redo-f-1.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.resource
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :returns:
            Any
        :description: QtGui/QTextDocument-resource-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.revision
        :returns:
            int
        :description: QtGui/QTextDocument-revision-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.rootFrame
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextFrame`
        :description: QtGui/QTextDocument-rootFrame-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.setBaselineOffset
        :args:
            float
        :description: QtGui/QTextDocument-setBaselineOffset-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.setBaseUrl
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtGui/QTextDocument-setBaseUrl-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.setDefaultCursorMoveStyle
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.CursorMoveStyle`
        :description: QtGui/QTextDocument-setDefaultCursorMoveStyle-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.setDefaultFont
        :args:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtGui/QTextDocument-setDefaultFont-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.setDefaultStyleSheet
        :args:
            str
        :description: QtGui/QTextDocument-setDefaultStyleSheet-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.setDefaultTextOption
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextOption`
        :description: QtGui/QTextDocument-setDefaultTextOption-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.setDocumentLayout
        :args:
            :sip:ref:`~PyQt6.QtGui.QAbstractTextDocumentLayout`
        :description: QtGui/QTextDocument-setDocumentLayout-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.setDocumentMargin
        :args:
            float
        :description: QtGui/QTextDocument-setDocumentMargin-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.setHtml
        :args:
            str
        :description: QtGui/QTextDocument-setHtml-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.setIndentWidth
        :args:
            float
        :description: QtGui/QTextDocument-setIndentWidth-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.setMarkdown
        :args:
            str
            features: :sip:ref:`~PyQt6.QtGui.QTextDocument.MarkdownFeatures` = :sip:ref:`~PyQt6.QtGui.QTextDocument.MarkdownFeatures.MarkdownDialectGitHub`
        :description: QtGui/QTextDocument-setMarkdown-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.setMaximumBlockCount
        :args:
            int
        :description: QtGui/QTextDocument-setMaximumBlockCount-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.setMetaInformation
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextDocument.MetaInformation`
            str
        :description: QtGui/QTextDocument-setMetaInformation-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.setModified
        :args:
            on: bool = True
        :description: QtGui/QTextDocument-setModified-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.setPageSize
        :args:
            :sip:ref:`~PyQt6.QtCore.QSizeF`
        :description: QtGui/QTextDocument-setPageSize-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.setPlainText
        :args:
            str
        :description: QtGui/QTextDocument-setPlainText-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.setSubScriptBaseline
        :args:
            float
        :description: QtGui/QTextDocument-setSubScriptBaseline-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.setSuperScriptBaseline
        :args:
            float
        :description: QtGui/QTextDocument-setSuperScriptBaseline-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.setTextWidth
        :args:
            float
        :description: QtGui/QTextDocument-setTextWidth-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.setUndoRedoEnabled
        :args:
            bool
        :description: QtGui/QTextDocument-setUndoRedoEnabled-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.setUseDesignMetrics
        :args:
            bool
        :description: QtGui/QTextDocument-setUseDesignMetrics-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.size
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSizeF`
        :description: QtGui/QTextDocument-size-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.subScriptBaseline
        :returns:
            float
        :description: QtGui/QTextDocument-subScriptBaseline-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.superScriptBaseline
        :returns:
            float
        :description: QtGui/QTextDocument-superScriptBaseline-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.textWidth
        :returns:
            float
        :description: QtGui/QTextDocument-textWidth-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.toHtml
        :returns:
            str
        :description: QtGui/QTextDocument-toHtml-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.toMarkdown
        :args:
            features: :sip:ref:`~PyQt6.QtGui.QTextDocument.MarkdownFeatures` = :sip:ref:`~PyQt6.QtGui.QTextDocument.MarkdownFeatures.MarkdownDialectGitHub`
        :returns:
            str
        :description: QtGui/QTextDocument-toMarkdown-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.toPlainText
        :returns:
            str
        :description: QtGui/QTextDocument-toPlainText-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.toRawText
        :returns:
            str
        :description: QtGui/QTextDocument-toRawText-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.undo
        :description: QtGui/QTextDocument-undo-f.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.undo
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextCursor`
        :description: QtGui/QTextDocument-undo-f-1.rst

    .. sip:method:: PyQt6.QtGui.QTextDocument.useDesignMetrics
        :returns:
            bool
        :description: QtGui/QTextDocument-useDesignMetrics-f.rst

    .. sip:signal:: PyQt6.QtGui.QTextDocument.baseUrlChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QUrl`
        :description: QtGui/QTextDocument-baseUrlChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QTextDocument.blockCountChanged
        :args:
            int
        :description: QtGui/QTextDocument-blockCountChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QTextDocument.contentsChange
        :args:
            int
            int
            int
        :description: QtGui/QTextDocument-contentsChange-s.rst

    .. sip:signal:: PyQt6.QtGui.QTextDocument.contentsChanged
        :description: QtGui/QTextDocument-contentsChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QTextDocument.cursorPositionChanged
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextCursor`
        :description: QtGui/QTextDocument-cursorPositionChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QTextDocument.documentLayoutChanged
        :description: QtGui/QTextDocument-documentLayoutChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QTextDocument.modificationChanged
        :args:
            bool
        :description: QtGui/QTextDocument-modificationChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QTextDocument.redoAvailable
        :args:
            bool
        :description: QtGui/QTextDocument-redoAvailable-s.rst

    .. sip:signal:: PyQt6.QtGui.QTextDocument.undoAvailable
        :args:
            bool
        :description: QtGui/QTextDocument-undoAvailable-s.rst

    .. sip:signal:: PyQt6.QtGui.QTextDocument.undoCommandAdded
        :description: QtGui/QTextDocument-undoCommandAdded-s.rst
