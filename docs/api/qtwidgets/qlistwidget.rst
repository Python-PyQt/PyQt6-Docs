:orphan:

.. sip:class:: PyQt6.QtWidgets.QListWidget
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QListView`
    :description: QtWidgets/QListWidget-c.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QListWidget-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.addItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :description: QtWidgets/QListWidget-addItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.addItem
        :args:
            Optional[str]
        :description: QtWidgets/QListWidget-addItem-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.addItems
        :args:
            Iterable[Optional[str]]
        :description: QtWidgets/QListWidget-addItems-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.clear
        :description: QtWidgets/QListWidget-clear-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.closePersistentEditor
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :description: QtWidgets/QListWidget-closePersistentEditor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.count
        :returns:
            int
        :description: QtWidgets/QListWidget-count-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.currentItem
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :description: QtWidgets/QListWidget-currentItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.currentRow
        :returns:
            int
        :description: QtWidgets/QListWidget-currentRow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.dropEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QDropEvent`
        :description: QtWidgets/QListWidget-dropEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.dropMimeData
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QMimeData`
            :sip:ref:`~PyQt6.QtCore.Qt.DropAction`
        :returns:
            bool
        :description: QtWidgets/QListWidget-dropMimeData-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.editItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :description: QtWidgets/QListWidget-editItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QListWidget-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.findItems
        :args:
            Optional[str]
            :sip:ref:`~PyQt6.QtCore.Qt.MatchFlag`
        :returns:
            list[:sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`]
        :description: QtWidgets/QListWidget-findItems-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.indexFromItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QListWidget-indexFromItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.insertItem
        :args:
            int
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :description: QtWidgets/QListWidget-insertItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.insertItem
        :args:
            int
            Optional[str]
        :description: QtWidgets/QListWidget-insertItem-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.insertItems
        :args:
            int
            Iterable[Optional[str]]
        :description: QtWidgets/QListWidget-insertItems-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.isPersistentEditorOpen
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :returns:
            bool
        :description: QtWidgets/QListWidget-isPersistentEditorOpen-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.isSortingEnabled
        :returns:
            bool
        :description: QtWidgets/QListWidget-isSortingEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.item
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :description: QtWidgets/QListWidget-item-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.itemAt
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :description: QtWidgets/QListWidget-itemAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.itemAt
        :args:
            int
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :description: QtWidgets/QListWidget-itemAt-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.itemFromIndex
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :description: QtWidgets/QListWidget-itemFromIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.items
        :args:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
        :returns:
            list[:sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`]
        :description: QtWidgets/QListWidget-items-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.itemWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QListWidget-itemWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.__len__
        :returns:
            int
        :description: QtWidgets/QListWidget-__len__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.mimeData
        :args:
            Iterable[:sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`]
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
        :description: QtWidgets/QListWidget-mimeData-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.mimeTypes
        :returns:
            list[str]
        :description: QtWidgets/QListWidget-mimeTypes-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.openPersistentEditor
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :description: QtWidgets/QListWidget-openPersistentEditor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.removeItemWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :description: QtWidgets/QListWidget-removeItemWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.row
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :returns:
            int
        :description: QtWidgets/QListWidget-row-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.scrollToItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
            hint: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.ScrollHint` = :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.ScrollHint.EnsureVisible`
        :description: QtWidgets/QListWidget-scrollToItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.selectedItems
        :returns:
            list[:sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`]
        :description: QtWidgets/QListWidget-selectedItems-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.setCurrentItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :description: QtWidgets/QListWidget-setCurrentItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.setCurrentItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
            :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlag`
        :description: QtWidgets/QListWidget-setCurrentItem-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.setCurrentRow
        :args:
            int
        :description: QtWidgets/QListWidget-setCurrentRow-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.setCurrentRow
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlag`
        :description: QtWidgets/QListWidget-setCurrentRow-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.setItemWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QListWidget-setItemWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.setSelectionModel
        :args:
            :sip:ref:`~PyQt6.QtCore.QItemSelectionModel`
        :description: QtWidgets/QListWidget-setSelectionModel-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.setSortingEnabled
        :args:
            bool
        :description: QtWidgets/QListWidget-setSortingEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.setSupportedDragActions
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.DropAction`
        :description: QtWidgets/QListWidget-setSupportedDragActions-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.sortItems
        :args:
            order: :sip:ref:`~PyQt6.QtCore.Qt.SortOrder` = :sip:ref:`~PyQt6.QtCore.Qt.SortOrder.AscendingOrder`
        :description: QtWidgets/QListWidget-sortItems-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.supportedDragActions
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.DropAction`
        :description: QtWidgets/QListWidget-supportedDragActions-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.supportedDropActions
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.DropAction`
        :description: QtWidgets/QListWidget-supportedDropActions-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.takeItem
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :description: QtWidgets/QListWidget-takeItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QListWidget.visualItemRect
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QListWidget-visualItemRect-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QListWidget.currentItemChanged
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :description: QtWidgets/QListWidget-currentItemChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QListWidget.currentRowChanged
        :args:
            int
        :description: QtWidgets/QListWidget-currentRowChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QListWidget.currentTextChanged
        :args:
            Optional[str]
        :description: QtWidgets/QListWidget-currentTextChanged-s-1.rst

    .. sip:signal:: PyQt6.QtWidgets.QListWidget.itemActivated
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :description: QtWidgets/QListWidget-itemActivated-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QListWidget.itemChanged
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :description: QtWidgets/QListWidget-itemChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QListWidget.itemClicked
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :description: QtWidgets/QListWidget-itemClicked-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QListWidget.itemDoubleClicked
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :description: QtWidgets/QListWidget-itemDoubleClicked-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QListWidget.itemEntered
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :description: QtWidgets/QListWidget-itemEntered-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QListWidget.itemPressed
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem`
        :description: QtWidgets/QListWidget-itemPressed-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QListWidget.itemSelectionChanged
        :description: QtWidgets/QListWidget-itemSelectionChanged-s.rst
