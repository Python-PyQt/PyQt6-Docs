:orphan:

.. sip:class:: PyQt6.QtGui.QPageLayout
    :description: QtGui/QPageLayout-c.rst

    .. sip:enum:: PyQt6.QtGui.QPageLayout.Mode
        :description: QtGui/QPageLayout-Mode-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QPageLayout.Mode.FullPageMode
            :description: QtGui/QPageLayout-Mode-FullPageMode-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QPageLayout.Mode.StandardMode
            :description: QtGui/QPageLayout-Mode-StandardMode-v.rst

    .. sip:enum:: PyQt6.QtGui.QPageLayout.Orientation
        :description: QtGui/QPageLayout-Orientation-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QPageLayout.Orientation.Landscape
            :description: QtGui/QPageLayout-Orientation-Landscape-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QPageLayout.Orientation.Portrait
            :description: QtGui/QPageLayout-Orientation-Portrait-v.rst

    .. sip:enum:: PyQt6.QtGui.QPageLayout.Unit
        :description: QtGui/QPageLayout-Unit-e.rst

        .. sip:enum-member:: PyQt6.QtGui.QPageLayout.Unit.Cicero
            :description: QtGui/QPageLayout-Unit-Cicero-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QPageLayout.Unit.Didot
            :description: QtGui/QPageLayout-Unit-Didot-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QPageLayout.Unit.Inch
            :description: QtGui/QPageLayout-Unit-Inch-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QPageLayout.Unit.Millimeter
            :description: QtGui/QPageLayout-Unit-Millimeter-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QPageLayout.Unit.Pica
            :description: QtGui/QPageLayout-Unit-Pica-v.rst

        .. sip:enum-member:: PyQt6.QtGui.QPageLayout.Unit.Point
            :description: QtGui/QPageLayout-Unit-Point-v.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.__init__
        :description: QtGui/QPageLayout-__init__-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QPageLayout`
        :description: QtGui/QPageLayout-__init__-f-1.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QPageSize`
            :sip:ref:`~PyQt6.QtGui.QPageLayout.Orientation`
            :sip:ref:`~PyQt6.QtCore.QMarginsF`
            units: :sip:ref:`~PyQt6.QtGui.QPageLayout.Unit` = :sip:ref:`~PyQt6.QtGui.QPageLayout.Unit.Point`
            minMargins: :sip:ref:`~PyQt6.QtCore.QMarginsF` = QMarginsF(0,0,0,0)
        :description: QtGui/QPageLayout-__init__-f-2.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.__eq__
        :args:
            :sip:ref:`~PyQt6.QtGui.QPageLayout`
        :returns:
            bool
        :description: QtGui/QPageLayout-__eq__-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.fullRect
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtGui/QPageLayout-fullRect-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.fullRect
        :args:
            :sip:ref:`~PyQt6.QtGui.QPageLayout.Unit`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtGui/QPageLayout-fullRect-f-1.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.fullRectPixels
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtGui/QPageLayout-fullRectPixels-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.fullRectPoints
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtGui/QPageLayout-fullRectPoints-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.isEquivalentTo
        :args:
            :sip:ref:`~PyQt6.QtGui.QPageLayout`
        :returns:
            bool
        :description: QtGui/QPageLayout-isEquivalentTo-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.isValid
        :returns:
            bool
        :description: QtGui/QPageLayout-isValid-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.margins
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMarginsF`
        :description: QtGui/QPageLayout-margins-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.margins
        :args:
            :sip:ref:`~PyQt6.QtGui.QPageLayout.Unit`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMarginsF`
        :description: QtGui/QPageLayout-margins-f-1.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.marginsPixels
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMargins`
        :description: QtGui/QPageLayout-marginsPixels-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.marginsPoints
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMargins`
        :description: QtGui/QPageLayout-marginsPoints-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.maximumMargins
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMarginsF`
        :description: QtGui/QPageLayout-maximumMargins-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.minimumMargins
        :returns:
            :sip:ref:`~PyQt6.QtCore.QMarginsF`
        :description: QtGui/QPageLayout-minimumMargins-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.mode
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPageLayout.Mode`
        :description: QtGui/QPageLayout-mode-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.__ne__
        :args:
            :sip:ref:`~PyQt6.QtGui.QPageLayout`
        :returns:
            bool
        :description: QtGui/QPageLayout-__ne__-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.orientation
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPageLayout.Orientation`
        :description: QtGui/QPageLayout-orientation-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.pageSize
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPageSize`
        :description: QtGui/QPageLayout-pageSize-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.paintRect
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtGui/QPageLayout-paintRect-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.paintRect
        :args:
            :sip:ref:`~PyQt6.QtGui.QPageLayout.Unit`
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtGui/QPageLayout-paintRect-f-1.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.paintRectPixels
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtGui/QPageLayout-paintRectPixels-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.paintRectPoints
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRect`
        :description: QtGui/QPageLayout-paintRectPoints-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.setBottomMargin
        :args:
            float
        :returns:
            bool
        :description: QtGui/QPageLayout-setBottomMargin-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.setLeftMargin
        :args:
            float
        :returns:
            bool
        :description: QtGui/QPageLayout-setLeftMargin-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.setMargins
        :args:
            :sip:ref:`~PyQt6.QtCore.QMarginsF`
        :returns:
            bool
        :description: QtGui/QPageLayout-setMargins-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.setMinimumMargins
        :args:
            :sip:ref:`~PyQt6.QtCore.QMarginsF`
        :description: QtGui/QPageLayout-setMinimumMargins-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.setMode
        :args:
            :sip:ref:`~PyQt6.QtGui.QPageLayout.Mode`
        :description: QtGui/QPageLayout-setMode-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.setOrientation
        :args:
            :sip:ref:`~PyQt6.QtGui.QPageLayout.Orientation`
        :description: QtGui/QPageLayout-setOrientation-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.setPageSize
        :args:
            :sip:ref:`~PyQt6.QtGui.QPageSize`
            minMargins: :sip:ref:`~PyQt6.QtCore.QMarginsF` = QMarginsF(0,0,0,0)
        :description: QtGui/QPageLayout-setPageSize-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.setRightMargin
        :args:
            float
        :returns:
            bool
        :description: QtGui/QPageLayout-setRightMargin-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.setTopMargin
        :args:
            float
        :returns:
            bool
        :description: QtGui/QPageLayout-setTopMargin-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.setUnits
        :args:
            :sip:ref:`~PyQt6.QtGui.QPageLayout.Unit`
        :description: QtGui/QPageLayout-setUnits-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.swap
        :args:
            :sip:ref:`~PyQt6.QtGui.QPageLayout`
        :description: QtGui/QPageLayout-swap-f.rst

    .. sip:method:: PyQt6.QtGui.QPageLayout.units
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPageLayout.Unit`
        :description: QtGui/QPageLayout-units-f.rst
