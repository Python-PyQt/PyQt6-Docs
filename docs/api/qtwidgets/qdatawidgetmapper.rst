:orphan:

.. sip:class:: PyQt6.QtWidgets.QDataWidgetMapper
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: QtWidgets/QDataWidgetMapper-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QDataWidgetMapper.SubmitPolicy
        :description: QtWidgets/QDataWidgetMapper-SubmitPolicy-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QDataWidgetMapper.SubmitPolicy.AutoSubmit
            :description: QtWidgets/QDataWidgetMapper-SubmitPolicy-AutoSubmit-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QDataWidgetMapper.SubmitPolicy.ManualSubmit
            :description: QtWidgets/QDataWidgetMapper-SubmitPolicy-ManualSubmit-v.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtWidgets/QDataWidgetMapper-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.addMapping
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            int
        :description: QtWidgets/QDataWidgetMapper-addMapping-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.addMapping
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            int
            Union[:sip:ref:`~PyQt6.QtCore.QByteArray`, bytes, bytearray, memoryview]
        :description: QtWidgets/QDataWidgetMapper-addMapping-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.clearMapping
        :description: QtWidgets/QDataWidgetMapper-clearMapping-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.currentIndex
        :returns:
            int
        :description: QtWidgets/QDataWidgetMapper-currentIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.itemDelegate
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate`
        :description: QtWidgets/QDataWidgetMapper-itemDelegate-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.mappedPropertyName
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QByteArray`
        :description: QtWidgets/QDataWidgetMapper-mappedPropertyName-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.mappedSection
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :returns:
            int
        :description: QtWidgets/QDataWidgetMapper-mappedSection-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.mappedWidgetAt
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QDataWidgetMapper-mappedWidgetAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.model
        :returns:
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
        :description: QtWidgets/QDataWidgetMapper-model-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.orientation
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
        :description: QtWidgets/QDataWidgetMapper-orientation-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.removeMapping
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QDataWidgetMapper-removeMapping-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.revert
        :description: QtWidgets/QDataWidgetMapper-revert-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.rootIndex
        :returns:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QDataWidgetMapper-rootIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.setCurrentIndex
        :args:
            int
        :description: QtWidgets/QDataWidgetMapper-setCurrentIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.setCurrentModelIndex
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QDataWidgetMapper-setCurrentModelIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.setItemDelegate
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractItemDelegate`
        :description: QtWidgets/QDataWidgetMapper-setItemDelegate-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.setModel
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`
        :description: QtWidgets/QDataWidgetMapper-setModel-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.setOrientation
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
        :description: QtWidgets/QDataWidgetMapper-setOrientation-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.setRootIndex
        :args:
            :sip:ref:`~PyQt6.QtCore.QModelIndex`
        :description: QtWidgets/QDataWidgetMapper-setRootIndex-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.setSubmitPolicy
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.SubmitPolicy`
        :description: QtWidgets/QDataWidgetMapper-setSubmitPolicy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.submit
        :returns:
            bool
        :description: QtWidgets/QDataWidgetMapper-submit-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.submitPolicy
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.SubmitPolicy`
        :description: QtWidgets/QDataWidgetMapper-submitPolicy-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.toFirst
        :description: QtWidgets/QDataWidgetMapper-toFirst-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.toLast
        :description: QtWidgets/QDataWidgetMapper-toLast-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.toNext
        :description: QtWidgets/QDataWidgetMapper-toNext-f.rst

    .. sip:method:: PyQt6.QtWidgets.QDataWidgetMapper.toPrevious
        :description: QtWidgets/QDataWidgetMapper-toPrevious-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QDataWidgetMapper.currentIndexChanged
        :args:
            int
        :description: QtWidgets/QDataWidgetMapper-currentIndexChanged-s.rst
