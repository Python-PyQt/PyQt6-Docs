:orphan:

.. sip:class:: PyQt6.QtCore.QAbstractListModel
    :inherits: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
    :description: QtCore/QAbstractListModel-c.rst

    .. sip:method:: PyQt6.QtCore.QAbstractListModel.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QAbstractListModel-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractListModel.dropMimeData
        :args:
            :sip:ref:`~PyQt6.QtCore.QMimeData`
            :sip:ref:`~PyQt6.QtCore.Qt.DropActions`
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtCore/QAbstractListModel-dropMimeData-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractListModel.flags
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.ItemFlags`
        :description: QtCore/QAbstractListModel-flags-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractListModel.index
        :args:
            int
            column: int = 0
            parent: :sip:ref:`~PyQt6.QtCore.QModelIndex` = QModelIndex()
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QAbstractListModel-index-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractListModel.parent
        :returns:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :description: QtCore/QAbstractListModel-parent-f.rst

    .. sip:method:: PyQt6.QtCore.QAbstractListModel.sibling
        :args:
            int
            int
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtCore/QAbstractListModel-sibling-f.rst
