:orphan:

.. sip:class:: PyQt6.QtWidgets.QItemDelegate
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate`
    :description: QtWidgets/QItemDelegate-c.rst

    .. sip:method:: PyQt6.QtWidgets.QItemDelegate.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtWidgets/QItemDelegate-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QItemDelegate.createEditor
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionViewItem`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QItemDelegate-createEditor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QItemDelegate.drawBackground
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionViewItem`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QItemDelegate-drawBackground-f.rst

    .. sip:method:: PyQt6.QtWidgets.QItemDelegate.drawCheck
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionViewItem`
            :sip:ref:`~PyQt6.QtCore.QRect`
            :sip:ref:`~PyQt6.QtCore.Qt.CheckState`
        :description: QtWidgets/QItemDelegate-drawCheck-f.rst

    .. sip:method:: PyQt6.QtWidgets.QItemDelegate.drawDecoration
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionViewItem`
            :sip:ref:`~PyQt6.QtCore.QRect`
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtWidgets/QItemDelegate-drawDecoration-f.rst

    .. sip:method:: PyQt6.QtWidgets.QItemDelegate.drawDisplay
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionViewItem`
            :sip:ref:`~PyQt6.QtCore.QRect`
            Optional[str]
        :description: QtWidgets/QItemDelegate-drawDisplay-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QItemDelegate.drawFocus
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionViewItem`
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QItemDelegate-drawFocus-f.rst

    .. sip:method:: PyQt6.QtWidgets.QItemDelegate.editorEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionViewItem`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            bool
        :description: QtWidgets/QItemDelegate-editorEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QItemDelegate.eventFilter
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QItemDelegate-eventFilter-f.rst

    .. sip:method:: PyQt6.QtWidgets.QItemDelegate.hasClipping
        :returns:
            bool
        :description: QtWidgets/QItemDelegate-hasClipping-f.rst

    .. sip:method:: PyQt6.QtWidgets.QItemDelegate.itemEditorFactory
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QItemEditorFactory`
        :description: QtWidgets/QItemDelegate-itemEditorFactory-f.rst

    .. sip:method:: PyQt6.QtWidgets.QItemDelegate.paint
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionViewItem`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QItemDelegate-paint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QItemDelegate.setClipping
        :args:
            bool
        :description: QtWidgets/QItemDelegate-setClipping-f.rst

    .. sip:method:: PyQt6.QtWidgets.QItemDelegate.setEditorData
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QItemDelegate-setEditorData-f.rst

    .. sip:method:: PyQt6.QtWidgets.QItemDelegate.setItemEditorFactory
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QItemEditorFactory`
        :description: QtWidgets/QItemDelegate-setItemEditorFactory-f.rst

    .. sip:method:: PyQt6.QtWidgets.QItemDelegate.setModelData
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QItemDelegate-setModelData-f.rst

    .. sip:method:: PyQt6.QtWidgets.QItemDelegate.sizeHint
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionViewItem`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QItemDelegate-sizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QItemDelegate.updateEditorGeometry
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtWidgets.QStyleOptionViewItem`
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QItemDelegate-updateEditorGeometry-f.rst
