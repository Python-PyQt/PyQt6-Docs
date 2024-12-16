:orphan:

.. sip:class:: PyQt6.QtCore.QItemSelectionModel
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtCore/QItemSelectionModel-c.rst

    .. sip:enum:: PyQt6.QtCore.QItemSelectionModel.SelectionFlag
        :description: QtCore/QItemSelectionModel-SelectionFlag-e.rst

        .. sip:enum-member:: PyQt6.QtCore.QItemSelectionModel.SelectionFlag.Clear
            :description: QtCore/QItemSelectionModel-SelectionFlag-Clear-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QItemSelectionModel.SelectionFlag.ClearAndSelect
            :description: QtCore/QItemSelectionModel-SelectionFlag-ClearAndSelect-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QItemSelectionModel.SelectionFlag.Columns
            :description: QtCore/QItemSelectionModel-SelectionFlag-Columns-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QItemSelectionModel.SelectionFlag.Current
            :description: QtCore/QItemSelectionModel-SelectionFlag-Current-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QItemSelectionModel.SelectionFlag.Deselect
            :description: QtCore/QItemSelectionModel-SelectionFlag-Deselect-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QItemSelectionModel.SelectionFlag.NoUpdate
            :description: QtCore/QItemSelectionModel-SelectionFlag-NoUpdate-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QItemSelectionModel.SelectionFlag.Rows
            :description: QtCore/QItemSelectionModel-SelectionFlag-Rows-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QItemSelectionModel.SelectionFlag.Select
            :description: QtCore/QItemSelectionModel-SelectionFlag-Select-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QItemSelectionModel.SelectionFlag.SelectCurrent
            :description: QtCore/QItemSelectionModel-SelectionFlag-SelectCurrent-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QItemSelectionModel.SelectionFlag.Toggle
            :description: QtCore/QItemSelectionModel-SelectionFlag-Toggle-v.rst

        .. sip:enum-member:: PyQt6.QtCore.QItemSelectionModel.SelectionFlag.ToggleCurrent
            :description: QtCore/QItemSelectionModel-SelectionFlag-ToggleCurrent-v.rst

    .. sip:method:: PyQt6.QtCore.QItemSelectionModel.__init__
        :args:
            model: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel` = None
        :description: QtCore/QItemSelectionModel-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QItemSelectionModel.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtCore/QItemSelectionModel-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QItemSelectionModel.clear
        :description: QtCore/QItemSelectionModel-clear-f.rst

    .. sip:method:: PyQt6.QtCore.QItemSelectionModel.clearCurrentIndex
        :description: QtCore/QItemSelectionModel-clearCurrentIndex-f.rst

    .. sip:method:: PyQt6.QtCore.QItemSelectionModel.clearSelection
        :description: QtCore/QItemSelectionModel-clearSelection-f.rst

    .. sip:method:: PyQt6.QtCore.QItemSelectionModel.columnIntersectsSelection
        :args:
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QItemSelectionModel-columnIntersectsSelection-f.rst

    .. sip:method:: PyQt6.QtCore.QItemSelectionModel.currentIndex
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QItemSelectionModel-currentIndex-f.rst

    .. sip:method:: PyQt6.QtCore.QItemSelectionModel.emitSelectionChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
        :description: QtCore/QItemSelectionModel-emitSelectionChanged-f.rst

    .. sip:method:: PyQt6.QtCore.QItemSelectionModel.hasSelection
        :returns:
            bool
        :description: QtCore/QItemSelectionModel-hasSelection-f.rst

    .. sip:method:: PyQt6.QtCore.QItemSelectionModel.isColumnSelected
        :args:
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QItemSelectionModel-isColumnSelected-f.rst

    .. sip:method:: PyQt6.QtCore.QItemSelectionModel.isRowSelected
        :args:
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QItemSelectionModel-isRowSelected-f.rst

    .. sip:method:: PyQt6.QtCore.QItemSelectionModel.isSelected
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtCore/QItemSelectionModel-isSelected-f.rst

    .. sip:method:: PyQt6.QtCore.QItemSelectionModel.model
        :returns:
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
        :description: QtCore/QItemSelectionModel-model-f.rst

    .. sip:method:: PyQt6.QtCore.QItemSelectionModel.reset
        :description: QtCore/QItemSelectionModel-reset-f.rst

    .. sip:method:: PyQt6.QtCore.QItemSelectionModel.rowIntersectsSelection
        :args:
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QItemSelectionModel-rowIntersectsSelection-f.rst

    .. sip:method:: PyQt6.QtCore.QItemSelectionModel.select
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlag`
        :description: QtCore/QItemSelectionModel-select-f-2.rst

    .. sip:method:: PyQt6.QtCore.QItemSelectionModel.select
        :args:
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
            :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlag`
        :description: QtCore/QItemSelectionModel-select-f-3.rst

    .. sip:method:: PyQt6.QtCore.QItemSelectionModel.selectedColumns
        :args:
            row: int = 0
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QModelIndex`]
        :description: QtCore/QItemSelectionModel-selectedColumns-f-1.rst

    .. sip:method:: PyQt6.QtCore.QItemSelectionModel.selectedIndexes
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QModelIndex`]
        :description: QtCore/QItemSelectionModel-selectedIndexes-f-1.rst

    .. sip:method:: PyQt6.QtCore.QItemSelectionModel.selectedRows
        :args:
            column: int = 0
        :returns:
            list[:sip:ref:`~PyQt6.QtCore.QModelIndex`]
        :description: QtCore/QItemSelectionModel-selectedRows-f-1.rst

    .. sip:method:: PyQt6.QtCore.QItemSelectionModel.selection
        :returns:
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
        :description: QtCore/QItemSelectionModel-selection-f.rst

    .. sip:method:: PyQt6.QtCore.QItemSelectionModel.setCurrentIndex
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            :sip:ref:`~PyQt6.QtCore.QItemSelectionModel.SelectionFlag`
        :description: QtCore/QItemSelectionModel-setCurrentIndex-f-1.rst

    .. sip:method:: PyQt6.QtCore.QItemSelectionModel.setModel
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
        :description: QtCore/QItemSelectionModel-setModel-f.rst

    .. sip:signal:: PyQt6.QtCore.QItemSelectionModel.currentChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QItemSelectionModel-currentChanged-s.rst

    .. sip:signal:: PyQt6.QtCore.QItemSelectionModel.currentColumnChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QItemSelectionModel-currentColumnChanged-s.rst

    .. sip:signal:: PyQt6.QtCore.QItemSelectionModel.currentRowChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QItemSelectionModel-currentRowChanged-s.rst

    .. sip:signal:: PyQt6.QtCore.QItemSelectionModel.modelChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
        :description: QtCore/QItemSelectionModel-modelChanged-s.rst

    .. sip:signal:: PyQt6.QtCore.QItemSelectionModel.selectionChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
            :sip:ref:`~PyQt6.QtCore.QItemSelection`
        :description: QtCore/QItemSelectionModel-selectionChanged-s.rst
