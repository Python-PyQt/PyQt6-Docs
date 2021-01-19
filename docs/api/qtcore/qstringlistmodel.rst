:orphan:

.. sip:class:: PyQt6.QtCore.QStringListModel
    :inherits: :sip:ref:`~PyQt6.QtCore.QAbstractListModel`
    :description: QtCore/QStringListModel-c.rst

    .. sip:method:: PyQt6.QtCore.QStringListModel.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QStringListModel-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QStringListModel.__init__
        :args:
            Iterable[str]
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QStringListModel-__init__-f-1.rst

    .. sip:method:: PyQt6.QtCore.QStringListModel.clearItemData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtCore/QStringListModel-clearItemData-f.rst

    .. sip:method:: PyQt6.QtCore.QStringListModel.data
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.DisplayRole`
        :returns:
            Any
        :description: QtCore/QStringListModel-data-f.rst

    .. sip:method:: PyQt6.QtCore.QStringListModel.flags
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.ItemFlags`
        :description: QtCore/QStringListModel-flags-f.rst

    .. sip:method:: PyQt6.QtCore.QStringListModel.insertRows
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QStringListModel-insertRows-f.rst

    .. sip:method:: PyQt6.QtCore.QStringListModel.itemData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            Dict[int, Any]
        :description: QtCore/QStringListModel-itemData-f.rst

    .. sip:method:: PyQt6.QtCore.QStringListModel.moveRows
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            int
        :returns:
            bool
        :description: QtCore/QStringListModel-moveRows-f.rst

    .. sip:method:: PyQt6.QtCore.QStringListModel.removeRows
        :args:
            int
            int
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            bool
        :description: QtCore/QStringListModel-removeRows-f.rst

    .. sip:method:: PyQt6.QtCore.QStringListModel.rowCount
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            int
        :description: QtCore/QStringListModel-rowCount-f.rst

    .. sip:method:: PyQt6.QtCore.QStringListModel.setData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            Any
            role: int = :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole.EditRole`
        :returns:
            bool
        :description: QtCore/QStringListModel-setData-f.rst

    .. sip:method:: PyQt6.QtCore.QStringListModel.setItemData
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
            Dict[int, Any]
        :returns:
            bool
        :description: QtCore/QStringListModel-setItemData-f.rst

    .. sip:method:: PyQt6.QtCore.QStringListModel.setStringList
        :args:
            Iterable[str]
        :description: QtCore/QStringListModel-setStringList-f.rst

    .. sip:method:: PyQt6.QtCore.QStringListModel.sibling
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QStringListModel-sibling-f.rst

    .. sip:method:: PyQt6.QtCore.QStringListModel.sort
        :args:
            int
            order: :sip:ref:`~PyQt6.QtCore.Qt.SortOrder` = :sip:ref:`~PyQt6.QtCore.Qt.SortOrder.AscendingOrder`
        :description: QtCore/QStringListModel-sort-f.rst

    .. sip:method:: PyQt6.QtCore.QStringListModel.stringList
        :returns:
            List[str]
        :description: QtCore/QStringListModel-stringList-f.rst

    .. sip:method:: PyQt6.QtCore.QStringListModel.supportedDropActions
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.DropActions`
        :description: QtCore/QStringListModel-supportedDropActions-f.rst
