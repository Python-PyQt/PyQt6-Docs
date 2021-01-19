:orphan:

.. sip:class:: PyQt6.QtWidgets.QGridLayout
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QLayout`
    :description: QtWidgets/QGridLayout-c.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QGridLayout-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.addItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QLayoutItem`
        :description: QtWidgets/QGridLayout-addItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.addItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QLayoutItem`
            int
            int
            rowSpan: int = 1
            columnSpan: int = 1
            alignment: :sip:ref:`~PyQt6.QtCore.Qt.Alignment` = Qt.Alignment()
        :description: QtWidgets/QGridLayout-addItem-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.addLayout
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QLayout`
            int
            int
            alignment: :sip:ref:`~PyQt6.QtCore.Qt.Alignment` = Qt.Alignment()
        :description: QtWidgets/QGridLayout-addLayout-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.addLayout
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QLayout`
            int
            int
            int
            int
            alignment: :sip:ref:`~PyQt6.QtCore.Qt.Alignment` = Qt.Alignment()
        :description: QtWidgets/QGridLayout-addLayout-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.addWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QGridLayout-addWidget-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.addWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            int
            int
            alignment: :sip:ref:`~PyQt6.QtCore.Qt.Alignment` = Qt.Alignment()
        :description: QtWidgets/QGridLayout-addWidget-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.addWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            int
            int
            int
            int
            alignment: :sip:ref:`~PyQt6.QtCore.Qt.Alignment` = Qt.Alignment()
        :description: QtWidgets/QGridLayout-addWidget-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.cellRect
        :args:
            int
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QGridLayout-cellRect-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.columnCount
        :returns:
            int
        :description: QtWidgets/QGridLayout-columnCount-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.columnMinimumWidth
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QGridLayout-columnMinimumWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.columnStretch
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QGridLayout-columnStretch-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.count
        :returns:
            int
        :description: QtWidgets/QGridLayout-count-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.expandingDirections
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.Orientations`
        :description: QtWidgets/QGridLayout-expandingDirections-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.getItemPosition
        :args:
            int
        :returns:
            int
            int
            int
            int
        :description: QtWidgets/QGridLayout-getItemPosition-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.hasHeightForWidth
        :returns:
            bool
        :description: QtWidgets/QGridLayout-hasHeightForWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.heightForWidth
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QGridLayout-heightForWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.horizontalSpacing
        :returns:
            int
        :description: QtWidgets/QGridLayout-horizontalSpacing-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.invalidate
        :description: QtWidgets/QGridLayout-invalidate-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.itemAt
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QLayoutItem`
        :description: QtWidgets/QGridLayout-itemAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.itemAtPosition
        :args:
            int
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QLayoutItem`
        :description: QtWidgets/QGridLayout-itemAtPosition-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.maximumSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QGridLayout-maximumSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.minimumHeightForWidth
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QGridLayout-minimumHeightForWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.minimumSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QGridLayout-minimumSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.originCorner
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.Corner`
        :description: QtWidgets/QGridLayout-originCorner-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.rowCount
        :returns:
            int
        :description: QtWidgets/QGridLayout-rowCount-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.rowMinimumHeight
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QGridLayout-rowMinimumHeight-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.rowStretch
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QGridLayout-rowStretch-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.setColumnMinimumWidth
        :args:
            int
            int
        :description: QtWidgets/QGridLayout-setColumnMinimumWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.setColumnStretch
        :args:
            int
            int
        :description: QtWidgets/QGridLayout-setColumnStretch-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.setDefaultPositioning
        :args:
            int
            :sip:ref:`~PyQt6.QtCore.Qt.Orientations`
        :description: QtWidgets/QGridLayout-setDefaultPositioning-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.setGeometry
        :args:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QGridLayout-setGeometry-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.setHorizontalSpacing
        :args:
            int
        :description: QtWidgets/QGridLayout-setHorizontalSpacing-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.setOriginCorner
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.Corner`
        :description: QtWidgets/QGridLayout-setOriginCorner-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.setRowMinimumHeight
        :args:
            int
            int
        :description: QtWidgets/QGridLayout-setRowMinimumHeight-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.setRowStretch
        :args:
            int
            int
        :description: QtWidgets/QGridLayout-setRowStretch-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.setSpacing
        :args:
            int
        :description: QtWidgets/QGridLayout-setSpacing-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.setVerticalSpacing
        :args:
            int
        :description: QtWidgets/QGridLayout-setVerticalSpacing-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.sizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QGridLayout-sizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.spacing
        :returns:
            int
        :description: QtWidgets/QGridLayout-spacing-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.takeAt
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QLayoutItem`
        :description: QtWidgets/QGridLayout-takeAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGridLayout.verticalSpacing
        :returns:
            int
        :description: QtWidgets/QGridLayout-verticalSpacing-f.rst
