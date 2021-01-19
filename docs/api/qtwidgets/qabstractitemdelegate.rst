:orphan:

.. sip:class:: PyQt6.QtWidgets.QAbstractItemDelegate
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtWidgets/QAbstractItemDelegate-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QAbstractItemDelegate.EndEditHint
        :description: QtWidgets/QAbstractItemDelegate-EndEditHint-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QAbstractItemDelegate.EndEditHint.EditNextItem
            :description: QtWidgets/QAbstractItemDelegate-EndEditHint-EditNextItem-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QAbstractItemDelegate.EndEditHint.EditPreviousItem
            :description: QtWidgets/QAbstractItemDelegate-EndEditHint-EditPreviousItem-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QAbstractItemDelegate.EndEditHint.NoHint
            :description: QtWidgets/QAbstractItemDelegate-EndEditHint-NoHint-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QAbstractItemDelegate.EndEditHint.RevertModelCache
            :description: QtWidgets/QAbstractItemDelegate-EndEditHint-RevertModelCache-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QAbstractItemDelegate.EndEditHint.SubmitModelCache
            :description: QtWidgets/QAbstractItemDelegate-EndEditHint-SubmitModelCache-v.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractItemDelegate.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtWidgets/QAbstractItemDelegate-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractItemDelegate.createEditor
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionViewItem`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QAbstractItemDelegate-createEditor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractItemDelegate.destroyEditor
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QAbstractItemDelegate-destroyEditor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractItemDelegate.editorEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionViewItem`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtWidgets/QAbstractItemDelegate-editorEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractItemDelegate.helpEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QHelpEvent`
            :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionViewItem`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtWidgets/QAbstractItemDelegate-helpEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractItemDelegate.paint
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionViewItem`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QAbstractItemDelegate-paint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractItemDelegate.setEditorData
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QAbstractItemDelegate-setEditorData-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractItemDelegate.setModelData
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QAbstractItemDelegate-setModelData-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractItemDelegate.sizeHint
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionViewItem`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QAbstractItemDelegate-sizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractItemDelegate.updateEditorGeometry
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionViewItem`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QAbstractItemDelegate-updateEditorGeometry-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QAbstractItemDelegate.closeEditor
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            hint: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.EndEditHint` = :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate.EndEditHint.NoHint`
        :description: QtWidgets/QAbstractItemDelegate-closeEditor-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QAbstractItemDelegate.commitData
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QAbstractItemDelegate-commitData-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QAbstractItemDelegate.sizeHintChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QAbstractItemDelegate-sizeHintChanged-s.rst
