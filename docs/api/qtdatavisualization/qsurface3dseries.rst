:orphan:

.. sip:class:: PyQt6.QtDataVisualization.QSurface3DSeries
    :inherits: :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DSeries`
    :description: QtDataVisualization/QSurface3DSeries-c.rst

    .. sip:enum:: PyQt6.QtDataVisualization.QSurface3DSeries.DrawFlag
        :description: QtDataVisualization/QSurface3DSeries-DrawFlag-e.rst

        .. sip:enum-member:: PyQt6.QtDataVisualization.QSurface3DSeries.DrawFlag.DrawSurface
            :description: QtDataVisualization/QSurface3DSeries-DrawFlag-DrawSurface-v.rst

        .. sip:enum-member:: PyQt6.QtDataVisualization.QSurface3DSeries.DrawFlag.DrawSurfaceAndWireframe
            :description: QtDataVisualization/QSurface3DSeries-DrawFlag-DrawSurfaceAndWireframe-v.rst

        .. sip:enum-member:: PyQt6.QtDataVisualization.QSurface3DSeries.DrawFlag.DrawWireframe
            :description: QtDataVisualization/QSurface3DSeries-DrawFlag-DrawWireframe-v.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurface3DSeries.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtDataVisualization/QSurface3DSeries-__init__-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurface3DSeries.__init__
        :args:
            :sip:ref:`~PyQt6.QtDataVisualization.QSurfaceDataProxy`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtDataVisualization/QSurface3DSeries-__init__-f-1.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurface3DSeries.dataProxy
        :returns:
            :sip:ref:`~PyQt6.QtDataVisualization.QSurfaceDataProxy`
        :description: QtDataVisualization/QSurface3DSeries-dataProxy-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurface3DSeries.drawMode
        :returns:
            :sip:ref:`~PyQt6.QtDataVisualization.QSurface3DSeries.DrawFlag`
        :description: QtDataVisualization/QSurface3DSeries-drawMode-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurface3DSeries.invalidSelectionPosition
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :static:
        :description: QtDataVisualization/QSurface3DSeries-invalidSelectionPosition-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurface3DSeries.isFlatShadingEnabled
        :returns:
            bool
        :description: QtDataVisualization/QSurface3DSeries-isFlatShadingEnabled-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurface3DSeries.isFlatShadingSupported
        :returns:
            bool
        :description: QtDataVisualization/QSurface3DSeries-isFlatShadingSupported-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurface3DSeries.selectedPoint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtDataVisualization/QSurface3DSeries-selectedPoint-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurface3DSeries.setDataProxy
        :args:
            :sip:ref:`~PyQt6.QtDataVisualization.QSurfaceDataProxy`
        :description: QtDataVisualization/QSurface3DSeries-setDataProxy-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurface3DSeries.setDrawMode
        :args:
            :sip:ref:`~PyQt6.QtDataVisualization.QSurface3DSeries.DrawFlag`
        :description: QtDataVisualization/QSurface3DSeries-setDrawMode-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurface3DSeries.setFlatShadingEnabled
        :args:
            bool
        :description: QtDataVisualization/QSurface3DSeries-setFlatShadingEnabled-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurface3DSeries.setSelectedPoint
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtDataVisualization/QSurface3DSeries-setSelectedPoint-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurface3DSeries.setTexture
        :args:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtDataVisualization/QSurface3DSeries-setTexture-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurface3DSeries.setTextureFile
        :args:
            str
        :description: QtDataVisualization/QSurface3DSeries-setTextureFile-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurface3DSeries.setWireframeColor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtDataVisualization/QSurface3DSeries-setWireframeColor-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurface3DSeries.texture
        :returns:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtDataVisualization/QSurface3DSeries-texture-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurface3DSeries.textureFile
        :returns:
            str
        :description: QtDataVisualization/QSurface3DSeries-textureFile-f.rst

    .. sip:method:: PyQt6.QtDataVisualization.QSurface3DSeries.wireframeColor
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtDataVisualization/QSurface3DSeries-wireframeColor-f.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QSurface3DSeries.dataProxyChanged
        :args:
            :sip:ref:`~PyQt6.QtDataVisualization.QSurfaceDataProxy`
        :description: QtDataVisualization/QSurface3DSeries-dataProxyChanged-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QSurface3DSeries.drawModeChanged
        :args:
            :sip:ref:`~PyQt6.QtDataVisualization.QSurface3DSeries.DrawFlag`
        :description: QtDataVisualization/QSurface3DSeries-drawModeChanged-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QSurface3DSeries.flatShadingEnabledChanged
        :args:
            bool
        :description: QtDataVisualization/QSurface3DSeries-flatShadingEnabledChanged-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QSurface3DSeries.flatShadingSupportedChanged
        :args:
            bool
        :description: QtDataVisualization/QSurface3DSeries-flatShadingSupportedChanged-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QSurface3DSeries.selectedPointChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtDataVisualization/QSurface3DSeries-selectedPointChanged-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QSurface3DSeries.textureChanged
        :args:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtDataVisualization/QSurface3DSeries-textureChanged-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QSurface3DSeries.textureFileChanged
        :args:
            str
        :description: QtDataVisualization/QSurface3DSeries-textureFileChanged-s.rst

    .. sip:signal:: PyQt6.QtDataVisualization.QSurface3DSeries.wireframeColorChanged
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtDataVisualization/QSurface3DSeries-wireframeColorChanged-s.rst
