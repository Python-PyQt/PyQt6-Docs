:orphan:

.. sip:class:: PyQt6.QtGui.QTextLayout
    :description: QtGui/QTextLayout-c.rst

    .. sip:enum:: PyQt6.QtGui.QTextLayout.CursorMode
        :description: QtGui/QTextLayout-CursorMode-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QTextLayout.CursorMode.SkipCharacters
            :description: QtGui/QTextLayout-CursorMode-SkipCharacters-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QTextLayout.CursorMode.SkipWords
            :description: QtGui/QTextLayout-CursorMode-SkipWords-v.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.__init__
        :description: QtGui/QTextLayout-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.__init__
        :args:
            str
        :description: QtGui/QTextLayout-__init__-f-1.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextBlock`
        :description: QtGui/QTextLayout-__init__-f-2.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.__init__
        :args:
            str
            :sip:ref:`~PyQt6.QtGui.QFont`
            paintdevice: :sip:ref:`~PyQt6.QtGui.QPaintDevice` = None
        :description: QtGui/QTextLayout-__init__-f-3.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.beginLayout
        :description: QtGui/QTextLayout-beginLayout-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.boundingRect
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtGui/QTextLayout-boundingRect-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.cacheEnabled
        :returns:
            bool
        :description: QtGui/QTextLayout-cacheEnabled-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.clearFormats
        :description: QtGui/QTextLayout-clearFormats-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.clearLayout
        :description: QtGui/QTextLayout-clearLayout-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.createLine
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextLine`
        :description: QtGui/QTextLayout-createLine-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.cursorMoveStyle
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.CursorMoveStyle`
        :description: QtGui/QTextLayout-cursorMoveStyle-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.draw
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtCore.QPointF`
            selections: Iterable[:sip:ref:`~PyQt6.QtGui.QTextLayout.FormatRange`] = []
            clip: :sip:ref:`~PyQt6.QtCore.QRectF` = QRectF()
        :description: QtGui/QTextLayout-draw-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.drawCursor
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtCore.QPointF`
            int
        :description: QtGui/QTextLayout-drawCursor-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.drawCursor
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtCore.QPointF`
            int
            int
        :description: QtGui/QTextLayout-drawCursor-f-1.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.endLayout
        :description: QtGui/QTextLayout-endLayout-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.font
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtGui/QTextLayout-font-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.formats
        :returns:
            List[:sip:ref:`~PyQt6.QtGui.QTextLayout.FormatRange`]
        :description: QtGui/QTextLayout-formats-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.glyphRuns
        :args:
            from: int = -1
            length: int = -1
        :returns:
            List[:sip:ref:`~PyQt6.QtGui.QGlyphRun`]
        :description: QtGui/QTextLayout-glyphRuns-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.isValidCursorPosition
        :args:
            int
        :returns:
            bool
        :description: QtGui/QTextLayout-isValidCursorPosition-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.leftCursorPosition
        :args:
            int
        :returns:
            int
        :description: QtGui/QTextLayout-leftCursorPosition-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.lineAt
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextLine`
        :description: QtGui/QTextLayout-lineAt-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.lineCount
        :returns:
            int
        :description: QtGui/QTextLayout-lineCount-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.lineForTextPosition
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextLine`
        :description: QtGui/QTextLayout-lineForTextPosition-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.maximumWidth
        :returns:
            float
        :description: QtGui/QTextLayout-maximumWidth-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.minimumWidth
        :returns:
            float
        :description: QtGui/QTextLayout-minimumWidth-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.nextCursorPosition
        :args:
            int
            mode: :sip:ref:`~PyQt6.QtGui.QTextLayout.CursorMode` = :sip:ref:`~PyQt6.QtGui.QTextLayout.CursorMode.SkipCharacters`
        :returns:
            int
        :description: QtGui/QTextLayout-nextCursorPosition-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.position
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGui/QTextLayout-position-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.preeditAreaPosition
        :returns:
            int
        :description: QtGui/QTextLayout-preeditAreaPosition-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.preeditAreaText
        :returns:
            str
        :description: QtGui/QTextLayout-preeditAreaText-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.previousCursorPosition
        :args:
            int
            mode: :sip:ref:`~PyQt6.QtGui.QTextLayout.CursorMode` = :sip:ref:`~PyQt6.QtGui.QTextLayout.CursorMode.SkipCharacters`
        :returns:
            int
        :description: QtGui/QTextLayout-previousCursorPosition-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.rightCursorPosition
        :args:
            int
        :returns:
            int
        :description: QtGui/QTextLayout-rightCursorPosition-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.setCacheEnabled
        :args:
            bool
        :description: QtGui/QTextLayout-setCacheEnabled-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.setCursorMoveStyle
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.CursorMoveStyle`
        :description: QtGui/QTextLayout-setCursorMoveStyle-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.setFont
        :args:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtGui/QTextLayout-setFont-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.setFormats
        :args:
            Iterable[:sip:ref:`~PyQt6.QtGui.QTextLayout.FormatRange`]
        :description: QtGui/QTextLayout-setFormats-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.setPosition
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGui/QTextLayout-setPosition-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.setPreeditArea
        :args:
            int
            str
        :description: QtGui/QTextLayout-setPreeditArea-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.setText
        :args:
            str
        :description: QtGui/QTextLayout-setText-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.setTextOption
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextOption`
        :description: QtGui/QTextLayout-setTextOption-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.text
        :returns:
            str
        :description: QtGui/QTextLayout-text-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLayout.textOption
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextOption`
        :description: QtGui/QTextLayout-textOption-f.rst
