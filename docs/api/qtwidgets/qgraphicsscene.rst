:orphan:

.. sip:class:: PyQt6.QtWidgets.QGraphicsScene
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtWidgets/QGraphicsScene-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QGraphicsScene.ItemIndexMethod
        :description: QtWidgets/QGraphicsScene-ItemIndexMethod-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QGraphicsScene.ItemIndexMethod.BspTreeIndex
            :description: QtWidgets/QGraphicsScene-ItemIndexMethod-BspTreeIndex-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QGraphicsScene.ItemIndexMethod.NoIndex
            :description: QtWidgets/QGraphicsScene-ItemIndexMethod-NoIndex-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QGraphicsScene.SceneLayer
        :description: QtWidgets/QGraphicsScene-SceneLayer-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QGraphicsScene.SceneLayer.AllLayers
            :description: QtWidgets/QGraphicsScene-SceneLayer-AllLayers-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QGraphicsScene.SceneLayer.BackgroundLayer
            :description: QtWidgets/QGraphicsScene-SceneLayer-BackgroundLayer-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QGraphicsScene.SceneLayer.ForegroundLayer
            :description: QtWidgets/QGraphicsScene-SceneLayer-ForegroundLayer-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QGraphicsScene.SceneLayer.ItemLayer
            :description: QtWidgets/QGraphicsScene-SceneLayer-ItemLayer-v.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtWidgets/QGraphicsScene-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QRectF`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtWidgets/QGraphicsScene-__init__-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.__init__
        :args:
            float
            float
            float
            float
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtWidgets/QGraphicsScene-__init__-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.activePanel
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`
        :description: QtWidgets/QGraphicsScene-activePanel-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.activeWindow
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget`
        :description: QtWidgets/QGraphicsScene-activeWindow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.addEllipse
        :args:
            :sip:ref:`~PyQt6.QtCore.QRectF`
            pen: Union[:sip:ref:`~PyQt6.QtGui.QPen`, Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]] = QPen()
            brush: Union[:sip:ref:`~PyQt6.QtGui.QBrush`, Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int], :sip:ref:`~PyQt6.QtGui.QGradient`] = QBrush()
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsEllipseItem`
        :description: QtWidgets/QGraphicsScene-addEllipse-f-6.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.addEllipse
        :args:
            float
            float
            float
            float
            pen: Union[:sip:ref:`~PyQt6.QtGui.QPen`, Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]] = QPen()
            brush: Union[:sip:ref:`~PyQt6.QtGui.QBrush`, Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int], :sip:ref:`~PyQt6.QtGui.QGradient`] = QBrush()
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsEllipseItem`
        :description: QtWidgets/QGraphicsScene-addEllipse-f-7.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.addItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`
        :description: QtWidgets/QGraphicsScene-addItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.addLine
        :args:
            :sip:ref:`~PyQt6.QtCore.QLineF`
            pen: Union[:sip:ref:`~PyQt6.QtGui.QPen`, Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]] = QPen()
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsLineItem`
        :description: QtWidgets/QGraphicsScene-addLine-f-6.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.addLine
        :args:
            float
            float
            float
            float
            pen: Union[:sip:ref:`~PyQt6.QtGui.QPen`, Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]] = QPen()
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsLineItem`
        :description: QtWidgets/QGraphicsScene-addLine-f-7.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.addPath
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainterPath`
            pen: Union[:sip:ref:`~PyQt6.QtGui.QPen`, Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]] = QPen()
            brush: Union[:sip:ref:`~PyQt6.QtGui.QBrush`, Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int], :sip:ref:`~PyQt6.QtGui.QGradient`] = QBrush()
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsPathItem`
        :description: QtWidgets/QGraphicsScene-addPath-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.addPixmap
        :args:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsPixmapItem`
        :description: QtWidgets/QGraphicsScene-addPixmap-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.addPolygon
        :args:
            :sip:ref:`~PyQt6.QtGui.QPolygonF`
            pen: Union[:sip:ref:`~PyQt6.QtGui.QPen`, Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]] = QPen()
            brush: Union[:sip:ref:`~PyQt6.QtGui.QBrush`, Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int], :sip:ref:`~PyQt6.QtGui.QGradient`] = QBrush()
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsPolygonItem`
        :description: QtWidgets/QGraphicsScene-addPolygon-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.addRect
        :args:
            :sip:ref:`~PyQt6.QtCore.QRectF`
            pen: Union[:sip:ref:`~PyQt6.QtGui.QPen`, Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]] = QPen()
            brush: Union[:sip:ref:`~PyQt6.QtGui.QBrush`, Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int], :sip:ref:`~PyQt6.QtGui.QGradient`] = QBrush()
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsRectItem`
        :description: QtWidgets/QGraphicsScene-addRect-f-6.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.addRect
        :args:
            float
            float
            float
            float
            pen: Union[:sip:ref:`~PyQt6.QtGui.QPen`, Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]] = QPen()
            brush: Union[:sip:ref:`~PyQt6.QtGui.QBrush`, Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int], :sip:ref:`~PyQt6.QtGui.QGradient`] = QBrush()
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsRectItem`
        :description: QtWidgets/QGraphicsScene-addRect-f-7.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.addSimpleText
        :args:
            Optional[str]
            font: :sip:ref:`~PyQt6.QtGui.QFont` = QFont()
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsSimpleTextItem`
        :description: QtWidgets/QGraphicsScene-addSimpleText-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.addText
        :args:
            Optional[str]
            font: :sip:ref:`~PyQt6.QtGui.QFont` = QFont()
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsTextItem`
        :description: QtWidgets/QGraphicsScene-addText-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.addWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            flags: :sip:ref:`~PyQt6.QtCore.Qt.WindowType` = Qt.WindowFlags()
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsProxyWidget`
        :description: QtWidgets/QGraphicsScene-addWidget-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.advance
        :description: QtWidgets/QGraphicsScene-advance-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.backgroundBrush
        :returns:
            :sip:ref:`~PyQt6.QtGui.QBrush`
        :description: QtWidgets/QGraphicsScene-backgroundBrush-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.bspTreeDepth
        :returns:
            int
        :description: QtWidgets/QGraphicsScene-bspTreeDepth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.clear
        :description: QtWidgets/QGraphicsScene-clear-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.clearFocus
        :description: QtWidgets/QGraphicsScene-clearFocus-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.clearSelection
        :description: QtWidgets/QGraphicsScene-clearSelection-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.collidingItems
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`
            mode: :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode` = :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode.IntersectsItemShape`
        :returns:
            List[:sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`]
        :description: QtWidgets/QGraphicsScene-collidingItems-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.contextMenuEvent
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneContextMenuEvent`
        :description: QtWidgets/QGraphicsScene-contextMenuEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.createItemGroup
        :args:
            Iterable[:sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`]
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsItemGroup`
        :description: QtWidgets/QGraphicsScene-createItemGroup-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.destroyItemGroup
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsItemGroup`
        :description: QtWidgets/QGraphicsScene-destroyItemGroup-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.dragEnterEvent
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneDragDropEvent`
        :description: QtWidgets/QGraphicsScene-dragEnterEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.dragLeaveEvent
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneDragDropEvent`
        :description: QtWidgets/QGraphicsScene-dragLeaveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.dragMoveEvent
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneDragDropEvent`
        :description: QtWidgets/QGraphicsScene-dragMoveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.drawBackground
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtWidgets/QGraphicsScene-drawBackground-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.drawForeground
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtWidgets/QGraphicsScene-drawForeground-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.dropEvent
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneDragDropEvent`
        :description: QtWidgets/QGraphicsScene-dropEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QGraphicsScene-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.eventFilter
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QGraphicsScene-eventFilter-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.focusInEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QFocusEvent`
        :description: QtWidgets/QGraphicsScene-focusInEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.focusItem
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`
        :description: QtWidgets/QGraphicsScene-focusItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.focusNextPrevChild
        :args:
            bool
        :returns:
            bool
        :description: QtWidgets/QGraphicsScene-focusNextPrevChild-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.focusOnTouch
        :returns:
            bool
        :description: QtWidgets/QGraphicsScene-focusOnTouch-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.focusOutEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QFocusEvent`
        :description: QtWidgets/QGraphicsScene-focusOutEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.font
        :returns:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtWidgets/QGraphicsScene-font-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.foregroundBrush
        :returns:
            :sip:ref:`~PyQt6.QtGui.QBrush`
        :description: QtWidgets/QGraphicsScene-foregroundBrush-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.hasFocus
        :returns:
            bool
        :description: QtWidgets/QGraphicsScene-hasFocus-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.height
        :returns:
            float
        :description: QtWidgets/QGraphicsScene-height-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.helpEvent
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneHelpEvent`
        :description: QtWidgets/QGraphicsScene-helpEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.inputMethodEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QInputMethodEvent`
        :description: QtWidgets/QGraphicsScene-inputMethodEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.inputMethodQuery
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.InputMethodQuery`
        :returns:
            Any
        :description: QtWidgets/QGraphicsScene-inputMethodQuery-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.invalidate
        :args:
            rect: :sip:ref:`~PyQt6.QtCore.QRectF` = QRectF()
            layers: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.SceneLayer` = :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.SceneLayer.AllLayers`
        :description: QtWidgets/QGraphicsScene-invalidate-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.invalidate
        :args:
            float
            float
            float
            float
            layers: :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.SceneLayer` = :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.SceneLayer.AllLayers`
        :description: QtWidgets/QGraphicsScene-invalidate-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.isActive
        :returns:
            bool
        :description: QtWidgets/QGraphicsScene-isActive-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.itemAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`
        :description: QtWidgets/QGraphicsScene-itemAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.itemAt
        :args:
            float
            float
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`
        :description: QtWidgets/QGraphicsScene-itemAt-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.itemIndexMethod
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.ItemIndexMethod`
        :description: QtWidgets/QGraphicsScene-itemIndexMethod-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.items
        :args:
            order: :sip:ref:`~PyQt6.QtCore.Qt.SortOrder` = :sip:ref:`~PyQt6.QtCore.Qt.SortOrder.DescendingOrder`
        :returns:
            List[:sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`]
        :description: QtWidgets/QGraphicsScene-items-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.items
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
            mode: :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode` = :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode.IntersectsItemShape`
            order: :sip:ref:`~PyQt6.QtCore.Qt.SortOrder` = :sip:ref:`~PyQt6.QtCore.Qt.SortOrder.DescendingOrder`
            deviceTransform: :sip:ref:`~PyQt6.QtGui.QTransform` = QTransform()
        :returns:
            List[:sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`]
        :description: QtWidgets/QGraphicsScene-items-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.items
        :args:
            :sip:ref:`~PyQt6.QtCore.QRectF`
            mode: :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode` = :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode.IntersectsItemShape`
            order: :sip:ref:`~PyQt6.QtCore.Qt.SortOrder` = :sip:ref:`~PyQt6.QtCore.Qt.SortOrder.DescendingOrder`
            deviceTransform: :sip:ref:`~PyQt6.QtGui.QTransform` = QTransform()
        :returns:
            List[:sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`]
        :description: QtWidgets/QGraphicsScene-items-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.items
        :args:
            :sip:ref:`~PyQt6.QtGui.QPolygonF`
            mode: :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode` = :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode.IntersectsItemShape`
            order: :sip:ref:`~PyQt6.QtCore.Qt.SortOrder` = :sip:ref:`~PyQt6.QtCore.Qt.SortOrder.DescendingOrder`
            deviceTransform: :sip:ref:`~PyQt6.QtGui.QTransform` = QTransform()
        :returns:
            List[:sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`]
        :description: QtWidgets/QGraphicsScene-items-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.items
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainterPath`
            mode: :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode` = :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode.IntersectsItemShape`
            order: :sip:ref:`~PyQt6.QtCore.Qt.SortOrder` = :sip:ref:`~PyQt6.QtCore.Qt.SortOrder.DescendingOrder`
            deviceTransform: :sip:ref:`~PyQt6.QtGui.QTransform` = QTransform()
        :returns:
            List[:sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`]
        :description: QtWidgets/QGraphicsScene-items-f-4.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.items
        :args:
            float
            float
            float
            float
            :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode`
            :sip:ref:`~PyQt6.QtCore.Qt.SortOrder`
            deviceTransform: :sip:ref:`~PyQt6.QtGui.QTransform` = QTransform()
        :returns:
            List[:sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`]
        :description: QtWidgets/QGraphicsScene-items-f-5.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.itemsBoundingRect
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtWidgets/QGraphicsScene-itemsBoundingRect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.keyPressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtWidgets/QGraphicsScene-keyPressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.keyReleaseEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtWidgets/QGraphicsScene-keyReleaseEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.minimumRenderSize
        :returns:
            float
        :description: QtWidgets/QGraphicsScene-minimumRenderSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.mouseDoubleClickEvent
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMouseEvent`
        :description: QtWidgets/QGraphicsScene-mouseDoubleClickEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.mouseGrabberItem
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`
        :description: QtWidgets/QGraphicsScene-mouseGrabberItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.mouseMoveEvent
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMouseEvent`
        :description: QtWidgets/QGraphicsScene-mouseMoveEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.mousePressEvent
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMouseEvent`
        :description: QtWidgets/QGraphicsScene-mousePressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.mouseReleaseEvent
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneMouseEvent`
        :description: QtWidgets/QGraphicsScene-mouseReleaseEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.palette
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPalette`
        :description: QtWidgets/QGraphicsScene-palette-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.removeItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`
        :description: QtWidgets/QGraphicsScene-removeItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.render
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            target: :sip:ref:`~PyQt6.QtCore.QRectF` = QRectF()
            source: :sip:ref:`~PyQt6.QtCore.QRectF` = QRectF()
            mode: :sip:ref:`~PyQt6.QtCore.Qt.AspectRatioMode` = :sip:ref:`~PyQt6.QtCore.Qt.AspectRatioMode.KeepAspectRatio`
        :description: QtWidgets/QGraphicsScene-render-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.sceneRect
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtWidgets/QGraphicsScene-sceneRect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.selectedItems
        :returns:
            List[:sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`]
        :description: QtWidgets/QGraphicsScene-selectedItems-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.selectionArea
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPainterPath`
        :description: QtWidgets/QGraphicsScene-selectionArea-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.sendEvent
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QGraphicsScene-sendEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.setActivePanel
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`
        :description: QtWidgets/QGraphicsScene-setActivePanel-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.setActiveWindow
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget`
        :description: QtWidgets/QGraphicsScene-setActiveWindow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.setBackgroundBrush
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QBrush`, Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int], :sip:ref:`~PyQt6.QtGui.QGradient`]
        :description: QtWidgets/QGraphicsScene-setBackgroundBrush-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.setBspTreeDepth
        :args:
            int
        :description: QtWidgets/QGraphicsScene-setBspTreeDepth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.setFocus
        :args:
            focusReason: :sip:ref:`~PyQt6.QtCore.Qt.FocusReason` = :sip:ref:`~PyQt6.QtCore.Qt.FocusReason.OtherFocusReason`
        :description: QtWidgets/QGraphicsScene-setFocus-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.setFocusItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`
            focusReason: :sip:ref:`~PyQt6.QtCore.Qt.FocusReason` = :sip:ref:`~PyQt6.QtCore.Qt.FocusReason.OtherFocusReason`
        :description: QtWidgets/QGraphicsScene-setFocusItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.setFocusOnTouch
        :args:
            bool
        :description: QtWidgets/QGraphicsScene-setFocusOnTouch-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.setFont
        :args:
            :sip:ref:`~PyQt6.QtGui.QFont`
        :description: QtWidgets/QGraphicsScene-setFont-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.setForegroundBrush
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QBrush`, Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int], :sip:ref:`~PyQt6.QtGui.QGradient`]
        :description: QtWidgets/QGraphicsScene-setForegroundBrush-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.setItemIndexMethod
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsScene.ItemIndexMethod`
        :description: QtWidgets/QGraphicsScene-setItemIndexMethod-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.setMinimumRenderSize
        :args:
            float
        :description: QtWidgets/QGraphicsScene-setMinimumRenderSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.setPalette
        :args:
            :sip:ref:`~PyQt6.QtGui.QPalette`
        :description: QtWidgets/QGraphicsScene-setPalette-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.setSceneRect
        :args:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtWidgets/QGraphicsScene-setSceneRect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.setSceneRect
        :args:
            float
            float
            float
            float
        :description: QtWidgets/QGraphicsScene-setSceneRect-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.setSelectionArea
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainterPath`
            :sip:ref:`~PyQt6.QtGui.QTransform`
        :description: QtWidgets/QGraphicsScene-setSelectionArea-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.setSelectionArea
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainterPath`
            selectionOperation: :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionOperation` = :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionOperation.ReplaceSelection`
            mode: :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode` = :sip:ref:`~PyQt6.QtCore.Qt.ItemSelectionMode.IntersectsItemShape`
            deviceTransform: :sip:ref:`~PyQt6.QtGui.QTransform` = QTransform()
        :description: QtWidgets/QGraphicsScene-setSelectionArea-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.setStickyFocus
        :args:
            bool
        :description: QtWidgets/QGraphicsScene-setStickyFocus-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.setStyle
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyle`
        :description: QtWidgets/QGraphicsScene-setStyle-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.stickyFocus
        :returns:
            bool
        :description: QtWidgets/QGraphicsScene-stickyFocus-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.style
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QStyle`
        :description: QtWidgets/QGraphicsScene-style-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.update
        :args:
            rect: :sip:ref:`~PyQt6.QtCore.QRectF` = QRectF()
        :description: QtWidgets/QGraphicsScene-update-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.update
        :args:
            float
            float
            float
            float
        :description: QtWidgets/QGraphicsScene-update-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.views
        :returns:
            List[:sip:ref:`~PyQt6.QtWidgets.QGraphicsView`]
        :description: QtWidgets/QGraphicsScene-views-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.wheelEvent
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsSceneWheelEvent`
        :description: QtWidgets/QGraphicsScene-wheelEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGraphicsScene.width
        :returns:
            float
        :description: QtWidgets/QGraphicsScene-width-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QGraphicsScene.changed
        :args:
            Iterable[:sip:ref:`~PyQt6.QtCore.QRectF`]
        :description: QtWidgets/QGraphicsScene-changed-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QGraphicsScene.focusItemChanged
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`
            :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`
            :sip:ref:`~PyQt6.QtCore.Qt.FocusReason`
        :description: QtWidgets/QGraphicsScene-focusItemChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QGraphicsScene.sceneRectChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtWidgets/QGraphicsScene-sceneRectChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QGraphicsScene.selectionChanged
        :description: QtWidgets/QGraphicsScene-selectionChanged-s.rst
