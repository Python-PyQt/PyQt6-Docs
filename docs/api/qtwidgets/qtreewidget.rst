:orphan:

.. sip:class:: PyQt6.QtWidgets.QTreeWidget
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QTreeView`
    :description: QtWidgets/QTreeWidget-c.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QTreeWidget-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.addTopLevelItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
        :description: QtWidgets/QTreeWidget-addTopLevelItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.addTopLevelItems
        :args:
            Iterable[:sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`]
        :description: QtWidgets/QTreeWidget-addTopLevelItems-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.clear
        :description: QtWidgets/QTreeWidget-clear-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.closePersistentEditor
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
            column: int = 0
        :description: QtWidgets/QTreeWidget-closePersistentEditor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.collapseItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
        :description: QtWidgets/QTreeWidget-collapseItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.columnCount
        :returns:
            int
        :description: QtWidgets/QTreeWidget-columnCount-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.currentColumn
        :returns:
            int
        :description: QtWidgets/QTreeWidget-currentColumn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.currentItem
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
        :description: QtWidgets/QTreeWidget-currentItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.dropEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDropEvent`
        :description: QtWidgets/QTreeWidget-dropEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.dropMimeData
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
            int
            :sip:ref:`~PyQt6.QtCore.QMimeData`
            :sip:ref:`~PyQt6.QtCore.Qt.DropAction`
        :returns:
            bool
        :description: QtWidgets/QTreeWidget-dropMimeData-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.editItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
            column: int = 0
        :description: QtWidgets/QTreeWidget-editItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QTreeWidget-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.expandItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
        :description: QtWidgets/QTreeWidget-expandItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.findItems
        :args:
            Optional[str]
            :sip:ref:`~PyQt6.QtCore.Qt.MatchFlag`
            column: int = 0
        :returns:
            list[:sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`]
        :description: QtWidgets/QTreeWidget-findItems-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.headerItem
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
        :description: QtWidgets/QTreeWidget-headerItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.indexFromItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
            column: int = 0
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QTreeWidget-indexFromItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.indexOfTopLevelItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
        :returns:
            int
        :description: QtWidgets/QTreeWidget-indexOfTopLevelItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.insertTopLevelItem
        :args:
            int
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
        :description: QtWidgets/QTreeWidget-insertTopLevelItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.insertTopLevelItems
        :args:
            int
            Iterable[:sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`]
        :description: QtWidgets/QTreeWidget-insertTopLevelItems-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.invisibleRootItem
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
        :description: QtWidgets/QTreeWidget-invisibleRootItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.isPersistentEditorOpen
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
            column: int = 0
        :returns:
            bool
        :description: QtWidgets/QTreeWidget-isPersistentEditorOpen-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.itemAbove
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
        :description: QtWidgets/QTreeWidget-itemAbove-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.itemAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
        :description: QtWidgets/QTreeWidget-itemAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.itemAt
        :args:
            int
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
        :description: QtWidgets/QTreeWidget-itemAt-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.itemBelow
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
        :description: QtWidgets/QTreeWidget-itemBelow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.itemFromIndex
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
        :description: QtWidgets/QTreeWidget-itemFromIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.itemWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QTreeWidget-itemWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.mimeData
        :args:
            Iterable[:sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
        :description: QtWidgets/QTreeWidget-mimeData-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.mimeTypes
        :returns:
            list[str]
        :description: QtWidgets/QTreeWidget-mimeTypes-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.openPersistentEditor
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
            column: int = 0
        :description: QtWidgets/QTreeWidget-openPersistentEditor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.removeItemWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
            int
        :description: QtWidgets/QTreeWidget-removeItemWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.scrollToItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
            hint: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.ScrollHint` = :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.ScrollHint.EnsureVisible`
        :description: QtWidgets/QTreeWidget-scrollToItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.selectedItems
        :returns:
            list[:sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`]
        :description: QtWidgets/QTreeWidget-selectedItems-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.setColumnCount
        :args:
            int
        :description: QtWidgets/QTreeWidget-setColumnCount-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.setCurrentItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
        :description: QtWidgets/QTreeWidget-setCurrentItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.setCurrentItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
            int
        :description: QtWidgets/QTreeWidget-setCurrentItem-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.setCurrentItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
            int
            :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlag`
        :description: QtWidgets/QTreeWidget-setCurrentItem-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.setHeaderItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
        :description: QtWidgets/QTreeWidget-setHeaderItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.setHeaderLabel
        :args:
            Optional[str]
        :description: QtWidgets/QTreeWidget-setHeaderLabel-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.setHeaderLabels
        :args:
            Iterable[Optional[str]]
        :description: QtWidgets/QTreeWidget-setHeaderLabels-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.setItemWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
            int
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QTreeWidget-setItemWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.setSelectionModel
        :args:
            :sip:ref:`~PyQt6.QtCore.QItemSelectionModel`
        :description: QtWidgets/QTreeWidget-setSelectionModel-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.sortColumn
        :returns:
            int
        :description: QtWidgets/QTreeWidget-sortColumn-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.sortItems
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.Qt.SortOrder`
        :description: QtWidgets/QTreeWidget-sortItems-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.supportedDropActions
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.DropAction`
        :description: QtWidgets/QTreeWidget-supportedDropActions-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.takeTopLevelItem
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
        :description: QtWidgets/QTreeWidget-takeTopLevelItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.topLevelItem
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
        :description: QtWidgets/QTreeWidget-topLevelItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.topLevelItemCount
        :returns:
            int
        :description: QtWidgets/QTreeWidget-topLevelItemCount-f.rst

    .. sip:method:: PyQt6.QtWidgets.QTreeWidget.visualItemRect
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QTreeWidget-visualItemRect-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QTreeWidget.currentItemChanged
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
        :description: QtWidgets/QTreeWidget-currentItemChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTreeWidget.itemActivated
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
            int
        :description: QtWidgets/QTreeWidget-itemActivated-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTreeWidget.itemChanged
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
            int
        :description: QtWidgets/QTreeWidget-itemChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTreeWidget.itemClicked
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
            int
        :description: QtWidgets/QTreeWidget-itemClicked-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTreeWidget.itemCollapsed
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
        :description: QtWidgets/QTreeWidget-itemCollapsed-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTreeWidget.itemDoubleClicked
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
            int
        :description: QtWidgets/QTreeWidget-itemDoubleClicked-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTreeWidget.itemEntered
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
            int
        :description: QtWidgets/QTreeWidget-itemEntered-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTreeWidget.itemExpanded
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
        :description: QtWidgets/QTreeWidget-itemExpanded-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTreeWidget.itemPressed
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem`
            int
        :description: QtWidgets/QTreeWidget-itemPressed-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QTreeWidget.itemSelectionChanged
        :description: QtWidgets/QTreeWidget-itemSelectionChanged-s.rst
