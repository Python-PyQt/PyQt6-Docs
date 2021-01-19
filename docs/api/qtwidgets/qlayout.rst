:orphan:

.. sip:class:: PyQt6.QtWidgets.QLayout
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject` :sip:ref:`~PyQt6.QtWidgets.QLayoutItem`
    :description: QtWidgets/QLayout-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QLayout.SizeConstraint
        :description: QtWidgets/QLayout-SizeConstraint-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
            :description: QtWidgets/QLayout-SizeConstraint-SetDefaultConstraint-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QLayout.SizeConstraint.SetFixedSize
            :description: QtWidgets/QLayout-SizeConstraint-SetFixedSize-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QLayout.SizeConstraint.SetMaximumSize
            :description: QtWidgets/QLayout-SizeConstraint-SetMaximumSize-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QLayout.SizeConstraint.SetMinAndMaxSize
            :description: QtWidgets/QLayout-SizeConstraint-SetMinAndMaxSize-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QLayout.SizeConstraint.SetMinimumSize
            :description: QtWidgets/QLayout-SizeConstraint-SetMinimumSize-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QLayout.SizeConstraint.SetNoConstraint
            :description: QtWidgets/QLayout-SizeConstraint-SetNoConstraint-v.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QLayout-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.activate
        :returns:
            bool
        :description: QtWidgets/QLayout-activate-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.addChildLayout
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QLayout`
        :description: QtWidgets/QLayout-addChildLayout-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.addChildWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QLayout-addChildWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.addItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QLayoutItem`
        :description: QtWidgets/QLayout-addItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.addWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QLayout-addWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.alignmentRect
        :args:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QLayout-alignmentRect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.childEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QChildEvent`
        :description: QtWidgets/QLayout-childEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.closestAcceptableSize
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtCore.QSize`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :static:
        :description: QtWidgets/QLayout-closestAcceptableSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.contentsMargins
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMargins`
        :description: QtWidgets/QLayout-contentsMargins-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.contentsRect
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QLayout-contentsRect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.controlTypes
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.ControlTypes`
        :description: QtWidgets/QLayout-controlTypes-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.count
        :returns:
            int
        :description: QtWidgets/QLayout-count-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.expandingDirections
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.Orientations`
        :description: QtWidgets/QLayout-expandingDirections-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.geometry
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QLayout-geometry-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.getContentsMargins
        :returns:
            int
            int
            int
            int
        :description: QtWidgets/QLayout-getContentsMargins-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.indexOf
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :returns:
            int
        :description: QtWidgets/QLayout-indexOf-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.indexOf
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QLayoutItem`
        :returns:
            int
        :description: QtWidgets/QLayout-indexOf-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.invalidate
        :description: QtWidgets/QLayout-invalidate-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.isEmpty
        :returns:
            bool
        :description: QtWidgets/QLayout-isEmpty-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.isEnabled
        :returns:
            bool
        :description: QtWidgets/QLayout-isEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.itemAt
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QLayoutItem`
        :description: QtWidgets/QLayout-itemAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.layout
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QLayout`
        :description: QtWidgets/QLayout-layout-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.__len__
        :returns:
            int
        :description: QtWidgets/QLayout-__len__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.maximumSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QLayout-maximumSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.menuBar
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QLayout-menuBar-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.minimumSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QLayout-minimumSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.parentWidget
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QLayout-parentWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.removeItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QLayoutItem`
        :description: QtWidgets/QLayout-removeItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.removeWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QLayout-removeWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.replaceWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            options: :sip:ref:`~PyQt6.QtCore.Qt.FindChildOptions` = :sip:ref:`~PyQt6.QtCore.Qt.FindChildOptions.FindChildrenRecursively`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QLayoutItem`
        :description: QtWidgets/QLayout-replaceWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.setAlignment
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            :sip:ref:`~PyQt6.QtCore.Qt.Alignment`
        :returns:
            bool
        :description: QtWidgets/QLayout-setAlignment-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.setAlignment
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QLayout`
            :sip:ref:`~PyQt6.QtCore.Qt.Alignment`
        :returns:
            bool
        :description: QtWidgets/QLayout-setAlignment-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.setContentsMargins
        :args:
            :sip:ref:`~PyQt6.QtCore.QMargins`
        :description: QtWidgets/QLayout-setContentsMargins-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.setContentsMargins
        :args:
            int
            int
            int
            int
        :description: QtWidgets/QLayout-setContentsMargins-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.setEnabled
        :args:
            bool
        :description: QtWidgets/QLayout-setEnabled-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.setGeometry
        :args:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QLayout-setGeometry-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.setMenuBar
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QLayout-setMenuBar-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.setSizeConstraint
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QLayout.SizeConstraint`
        :description: QtWidgets/QLayout-setSizeConstraint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.setSpacing
        :args:
            int
        :description: QtWidgets/QLayout-setSpacing-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.sizeConstraint
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QLayout.SizeConstraint`
        :description: QtWidgets/QLayout-sizeConstraint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.spacing
        :returns:
            int
        :description: QtWidgets/QLayout-spacing-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.takeAt
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QLayoutItem`
        :description: QtWidgets/QLayout-takeAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.totalHeightForWidth
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QLayout-totalHeightForWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.totalMaximumSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QLayout-totalMaximumSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.totalMinimumSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QLayout-totalMinimumSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.totalSizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QLayout-totalSizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.update
        :description: QtWidgets/QLayout-update-f.rst

    .. sip:method:: PyQt6.QtWidgets.QLayout.widgetEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtWidgets/QLayout-widgetEvent-f.rst
