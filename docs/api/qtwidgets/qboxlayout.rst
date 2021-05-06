:orphan:

.. sip:class:: PyQt6.QtWidgets.QBoxLayout
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QLayout`
    :description: QtWidgets/QBoxLayout-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QBoxLayout.Direction
        :description: QtWidgets/QBoxLayout-Direction-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QBoxLayout.Direction.BottomToTop
            :description: QtWidgets/QBoxLayout-Direction-BottomToTop-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QBoxLayout.Direction.Down
            :description: QtWidgets/QBoxLayout-Direction-Down-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QBoxLayout.Direction.LeftToRight
            :description: QtWidgets/QBoxLayout-Direction-LeftToRight-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QBoxLayout.Direction.RightToLeft
            :description: QtWidgets/QBoxLayout-Direction-RightToLeft-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QBoxLayout.Direction.TopToBottom
            :description: QtWidgets/QBoxLayout-Direction-TopToBottom-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QBoxLayout.Direction.Up
            :description: QtWidgets/QBoxLayout-Direction-Up-v.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.__init__
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.Direction`
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QBoxLayout-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.addItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QLayoutItem`
        :description: QtWidgets/QBoxLayout-addItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.addLayout
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QLayout`
            stretch: int = 0
        :description: QtWidgets/QBoxLayout-addLayout-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.addSpacerItem
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QSpacerItem`
        :description: QtWidgets/QBoxLayout-addSpacerItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.addSpacing
        :args:
            int
        :description: QtWidgets/QBoxLayout-addSpacing-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.addStretch
        :args:
            stretch: int = 0
        :description: QtWidgets/QBoxLayout-addStretch-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.addStrut
        :args:
            int
        :description: QtWidgets/QBoxLayout-addStrut-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.addWidget
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            stretch: int = 0
            alignment: :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag` = Qt.Alignment()
        :description: QtWidgets/QBoxLayout-addWidget-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.count
        :returns:
            int
        :description: QtWidgets/QBoxLayout-count-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.direction
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.Direction`
        :description: QtWidgets/QBoxLayout-direction-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.expandingDirections
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
        :description: QtWidgets/QBoxLayout-expandingDirections-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.hasHeightForWidth
        :returns:
            bool
        :description: QtWidgets/QBoxLayout-hasHeightForWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.heightForWidth
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QBoxLayout-heightForWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.insertItem
        :args:
            int
            :sip:ref:`~PyQt6.QtWidgets.QLayoutItem`
        :description: QtWidgets/QBoxLayout-insertItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.insertLayout
        :args:
            int
            :sip:ref:`~PyQt6.QtWidgets.QLayout`
            stretch: int = 0
        :description: QtWidgets/QBoxLayout-insertLayout-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.insertSpacerItem
        :args:
            int
            :sip:ref:`~PyQt6.QtWidgets.QSpacerItem`
        :description: QtWidgets/QBoxLayout-insertSpacerItem-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.insertSpacing
        :args:
            int
            int
        :description: QtWidgets/QBoxLayout-insertSpacing-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.insertStretch
        :args:
            int
            stretch: int = 0
        :description: QtWidgets/QBoxLayout-insertStretch-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.insertWidget
        :args:
            int
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            stretch: int = 0
            alignment: :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag` = Qt.Alignment()
        :description: QtWidgets/QBoxLayout-insertWidget-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.invalidate
        :description: QtWidgets/QBoxLayout-invalidate-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.itemAt
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QLayoutItem`
        :description: QtWidgets/QBoxLayout-itemAt-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.maximumSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QBoxLayout-maximumSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.minimumHeightForWidth
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QBoxLayout-minimumHeightForWidth-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.minimumSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QBoxLayout-minimumSize-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.setDirection
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.Direction`
        :description: QtWidgets/QBoxLayout-setDirection-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.setGeometry
        :args:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtWidgets/QBoxLayout-setGeometry-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.setSpacing
        :args:
            int
        :description: QtWidgets/QBoxLayout-setSpacing-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.setStretch
        :args:
            int
            int
        :description: QtWidgets/QBoxLayout-setStretch-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.setStretchFactor
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
            int
        :returns:
            bool
        :description: QtWidgets/QBoxLayout-setStretchFactor-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.setStretchFactor
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QLayout`
            int
        :returns:
            bool
        :description: QtWidgets/QBoxLayout-setStretchFactor-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.sizeHint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtWidgets/QBoxLayout-sizeHint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.spacing
        :returns:
            int
        :description: QtWidgets/QBoxLayout-spacing-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.stretch
        :args:
            int
        :returns:
            int
        :description: QtWidgets/QBoxLayout-stretch-f.rst

    .. sip:method:: PyQt6.QtWidgets.QBoxLayout.takeAt
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QLayoutItem`
        :description: QtWidgets/QBoxLayout-takeAt-f.rst
