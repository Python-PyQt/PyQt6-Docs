:orphan:

.. sip:class:: PyQt6.QtGui.QTextLine
    :description: QtGui/QTextLine-c.rst

    .. sip:enum:: PyQt6.QtGui.QTextLine.CursorPosition
        :description: QtGui/QTextLine-CursorPosition-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QTextLine.CursorPosition.CursorBetweenCharacters
            :description: QtGui/QTextLine-CursorPosition-CursorBetweenCharacters-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QTextLine.CursorPosition.CursorOnCharacter
            :description: QtGui/QTextLine-CursorPosition-CursorOnCharacter-v.rst

    .. sip:enum:: PyQt6.QtGui.QTextLine.Edge
        :description: QtGui/QTextLine-Edge-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QTextLine.Edge.Leading
            :description: QtGui/QTextLine-Edge-Leading-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QTextLine.Edge.Trailing
            :description: QtGui/QTextLine-Edge-Trailing-v.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.__init__
        :description: QtGui/QTextLine-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextLine`
        :description: QtGui/QTextLine-__init__-f-1.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.ascent
        :returns:
            float
        :description: QtGui/QTextLine-ascent-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.cursorToX
        :args:
            int
            edge: :sip:ref:`~PyQt6.QtGui.QTextLine.Edge` = :sip:ref:`~PyQt6.QtGui.QTextLine.Edge.Leading`
        :returns:
            float
            int
        :description: QtGui/QTextLine-cursorToX-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.descent
        :returns:
            float
        :description: QtGui/QTextLine-descent-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.draw
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGui/QTextLine-draw-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.glyphRuns
        :args:
            from: int = -1
            length: int = -1
        :returns:
            list[:sip:ref:`~PyQt6.QtGui.QGlyphRun`]
        :description: QtGui/QTextLine-glyphRuns-f-2.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.glyphRuns
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtGui.QTextLayout.GlyphRunRetrievalFlag`
        :returns:
            list[:sip:ref:`~PyQt6.QtGui.QGlyphRun`]
        :description: QtGui/QTextLine-glyphRuns-f-3.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.height
        :returns:
            float
        :description: QtGui/QTextLine-height-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.horizontalAdvance
        :returns:
            float
        :description: QtGui/QTextLine-horizontalAdvance-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.isValid
        :returns:
            bool
        :description: QtGui/QTextLine-isValid-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.leading
        :returns:
            float
        :description: QtGui/QTextLine-leading-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.leadingIncluded
        :returns:
            bool
        :description: QtGui/QTextLine-leadingIncluded-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.lineNumber
        :returns:
            int
        :description: QtGui/QTextLine-lineNumber-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.naturalTextRect
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtGui/QTextLine-naturalTextRect-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.naturalTextWidth
        :returns:
            float
        :description: QtGui/QTextLine-naturalTextWidth-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.position
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGui/QTextLine-position-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.rect
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtGui/QTextLine-rect-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.setLeadingIncluded
        :args:
            bool
        :description: QtGui/QTextLine-setLeadingIncluded-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.setLineWidth
        :args:
            float
        :description: QtGui/QTextLine-setLineWidth-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.setNumColumns
        :args:
            int
        :description: QtGui/QTextLine-setNumColumns-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.setNumColumns
        :args:
            int
            float
        :description: QtGui/QTextLine-setNumColumns-f-1.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.setPosition
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: QtGui/QTextLine-setPosition-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.textLength
        :returns:
            int
        :description: QtGui/QTextLine-textLength-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.textStart
        :returns:
            int
        :description: QtGui/QTextLine-textStart-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.width
        :returns:
            float
        :description: QtGui/QTextLine-width-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.x
        :returns:
            float
        :description: QtGui/QTextLine-x-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.xToCursor
        :args:
            float
            edge: :sip:ref:`~PyQt6.QtGui.QTextLine.CursorPosition` = :sip:ref:`~PyQt6.QtGui.QTextLine.CursorPosition.CursorBetweenCharacters`
        :returns:
            int
        :description: QtGui/QTextLine-xToCursor-f.rst

    .. sip:method:: PyQt6.QtGui.QTextLine.y
        :returns:
            float
        :description: QtGui/QTextLine-y-f.rst
