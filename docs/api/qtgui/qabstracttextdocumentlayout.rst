:orphan:

.. sip:class:: PyQt6.QtGui.QAbstractTextDocumentLayout
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtGui/QAbstractTextDocumentLayout-c.rst

    .. sip:method:: PyQt6.QtGui.QAbstractTextDocumentLayout.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextDocument`
        :description: QtGui/QAbstractTextDocumentLayout-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QAbstractTextDocumentLayout.anchorAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :returns:
            str
        :description: QtGui/QAbstractTextDocumentLayout-anchorAt-f.rst

    .. sip:method:: PyQt6.QtGui.QAbstractTextDocumentLayout.blockBoundingRect
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextBlock`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtGui/QAbstractTextDocumentLayout-blockBoundingRect-f.rst

    .. sip:method:: PyQt6.QtGui.QAbstractTextDocumentLayout.blockWithMarkerAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextBlock`
        :description: QtGui/QAbstractTextDocumentLayout-blockWithMarkerAt-f.rst

    .. sip:method:: PyQt6.QtGui.QAbstractTextDocumentLayout.document
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextDocument`
        :description: QtGui/QAbstractTextDocumentLayout-document-f.rst

    .. sip:method:: PyQt6.QtGui.QAbstractTextDocumentLayout.documentChanged
        :args:
            int
            int
            int
        :description: QtGui/QAbstractTextDocumentLayout-documentChanged-f.rst

    .. sip:method:: PyQt6.QtGui.QAbstractTextDocumentLayout.documentSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSizeF`
        :description: QtGui/QAbstractTextDocumentLayout-documentSize-f.rst

    .. sip:method:: PyQt6.QtGui.QAbstractTextDocumentLayout.draw
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtGui.QAbstractTextDocumentLayout.PaintContext`
        :description: QtGui/QAbstractTextDocumentLayout-draw-f.rst

    .. sip:method:: PyQt6.QtGui.QAbstractTextDocumentLayout.drawInlineObject
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtCore.QRectF`
            :sip:ref:`~PyQt6.QtGui.QTextInlineObject`
            int
            :sip:ref:`~PyQt6.QtGui.QTextFormat`
        :description: QtGui/QAbstractTextDocumentLayout-drawInlineObject-f.rst

    .. sip:method:: PyQt6.QtGui.QAbstractTextDocumentLayout.format
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextCharFormat`
        :description: QtGui/QAbstractTextDocumentLayout-format-f.rst

    .. sip:method:: PyQt6.QtGui.QAbstractTextDocumentLayout.formatAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextFormat`
        :description: QtGui/QAbstractTextDocumentLayout-formatAt-f.rst

    .. sip:method:: PyQt6.QtGui.QAbstractTextDocumentLayout.frameBoundingRect
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextFrame`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtGui/QAbstractTextDocumentLayout-frameBoundingRect-f.rst

    .. sip:method:: PyQt6.QtGui.QAbstractTextDocumentLayout.handlerForObject
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtGui.QTextObjectInterface`
        :description: QtGui/QAbstractTextDocumentLayout-handlerForObject-f.rst

    .. sip:method:: PyQt6.QtGui.QAbstractTextDocumentLayout.hitTest
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
            :sip:ref:`~PyQt6.QtCore.Qt.HitTestAccuracy`
        :returns:
            int
        :description: QtGui/QAbstractTextDocumentLayout-hitTest-f.rst

    .. sip:method:: PyQt6.QtGui.QAbstractTextDocumentLayout.imageAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :returns:
            str
        :description: QtGui/QAbstractTextDocumentLayout-imageAt-f.rst

    .. sip:method:: PyQt6.QtGui.QAbstractTextDocumentLayout.pageCount
        :returns:
            int
        :description: QtGui/QAbstractTextDocumentLayout-pageCount-f.rst

    .. sip:method:: PyQt6.QtGui.QAbstractTextDocumentLayout.paintDevice
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPaintDevice`
        :description: QtGui/QAbstractTextDocumentLayout-paintDevice-f.rst

    .. sip:method:: PyQt6.QtGui.QAbstractTextDocumentLayout.positionInlineObject
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextInlineObject`
            int
            :sip:ref:`~PyQt6.QtGui.QTextFormat`
        :description: QtGui/QAbstractTextDocumentLayout-positionInlineObject-f.rst

    .. sip:method:: PyQt6.QtGui.QAbstractTextDocumentLayout.registerHandler
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtGui/QAbstractTextDocumentLayout-registerHandler-f.rst

    .. sip:method:: PyQt6.QtGui.QAbstractTextDocumentLayout.resizeInlineObject
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextInlineObject`
            int
            :sip:ref:`~PyQt6.QtGui.QTextFormat`
        :description: QtGui/QAbstractTextDocumentLayout-resizeInlineObject-f.rst

    .. sip:method:: PyQt6.QtGui.QAbstractTextDocumentLayout.setPaintDevice
        :args:
            :sip:ref:`~PyQt6.QtGui.QPaintDevice`
        :description: QtGui/QAbstractTextDocumentLayout-setPaintDevice-f.rst

    .. sip:method:: PyQt6.QtGui.QAbstractTextDocumentLayout.unregisterHandler
        :args:
            int
            component: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGui/QAbstractTextDocumentLayout-unregisterHandler-f.rst

    .. sip:signal:: PyQt6.QtGui.QAbstractTextDocumentLayout.documentSizeChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QSizeF`
        :description: QtGui/QAbstractTextDocumentLayout-documentSizeChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QAbstractTextDocumentLayout.pageCountChanged
        :args:
            int
        :description: QtGui/QAbstractTextDocumentLayout-pageCountChanged-s.rst

    .. sip:signal:: PyQt6.QtGui.QAbstractTextDocumentLayout.update
        :args:
            rect: :sip:ref:`~PyQt6.QtCore.QRectF` = QRectF(0,0,1000000000.0,1000000000.0)
        :description: QtGui/QAbstractTextDocumentLayout-update-s-1.rst

    .. sip:signal:: PyQt6.QtGui.QAbstractTextDocumentLayout.updateBlock
        :args:
            :sip:ref:`~PyQt6.QtGui.QTextBlock`
        :description: QtGui/QAbstractTextDocumentLayout-updateBlock-s.rst
