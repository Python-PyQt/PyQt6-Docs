:orphan:

.. sip:class:: PyQt6.QtGraphs.QSurface3DSeries
    :inherits: :sip:ref:`~PyQt6.QtGraphs.QAbstract3DSeries`
    :description: QtGraphs/QSurface3DSeries-c.rst

    .. sip:enum:: PyQt6.QtGraphs.QSurface3DSeries.DrawFlag
        :description: QtGraphs/QSurface3DSeries-DrawFlag-e.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QSurface3DSeries.DrawFlag.DrawFilledSurface
            :description: QtGraphs/QSurface3DSeries-DrawFlag-DrawFilledSurface-v.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QSurface3DSeries.DrawFlag.DrawSurface
            :description: QtGraphs/QSurface3DSeries-DrawFlag-DrawSurface-v.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QSurface3DSeries.DrawFlag.DrawSurfaceAndWireframe
            :description: QtGraphs/QSurface3DSeries-DrawFlag-DrawSurfaceAndWireframe-v.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QSurface3DSeries.DrawFlag.DrawWireframe
            :description: QtGraphs/QSurface3DSeries-DrawFlag-DrawWireframe-v.rst

    .. sip:enum:: PyQt6.QtGraphs.QSurface3DSeries.Shading
        :description: QtGraphs/QSurface3DSeries-Shading-e.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QSurface3DSeries.Shading.Flat
            :description: QtGraphs/QSurface3DSeries-Shading-Flat-v.rst

        .. sip:enum-member:: PyQt6.QtGraphs.QSurface3DSeries.Shading.Smooth
            :description: QtGraphs/QSurface3DSeries-Shading-Smooth-v.rst

    .. sip:method:: PyQt6.QtGraphs.QSurface3DSeries.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGraphs/QSurface3DSeries-__init__-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurface3DSeries.__init__
        :args:
            :sip:ref:`~PyQt6.QtGraphs.QSurfaceDataProxy`
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtGraphs/QSurface3DSeries-__init__-f-1.rst

    .. sip:method:: PyQt6.QtGraphs.QSurface3DSeries.clearArray
        :description: QtGraphs/QSurface3DSeries-clearArray-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurface3DSeries.clearRow
        :args:
            int
        :description: QtGraphs/QSurface3DSeries-clearRow-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurface3DSeries.dataArray
        :returns:
            list[list[:sip:ref:`~PyQt6.QtGraphs.QSurfaceDataItem`]]
        :description: QtGraphs/QSurface3DSeries-dataArray-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurface3DSeries.dataProxy
        :returns:
            :sip:ref:`~PyQt6.QtGraphs.QSurfaceDataProxy`
        :description: QtGraphs/QSurface3DSeries-dataProxy-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurface3DSeries.drawMode
        :returns:
            :sip:ref:`~PyQt6.QtGraphs.QSurface3DSeries.DrawFlag`
        :description: QtGraphs/QSurface3DSeries-drawMode-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurface3DSeries.invalidSelectionPosition
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :static:
        :description: QtGraphs/QSurface3DSeries-invalidSelectionPosition-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurface3DSeries.isFlatShadingSupported
        :returns:
            bool
        :description: QtGraphs/QSurface3DSeries-isFlatShadingSupported-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurface3DSeries.selectedPoint
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtGraphs/QSurface3DSeries-selectedPoint-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurface3DSeries.setDataArray
        :args:
            Iterable[Iterable[:sip:ref:`~PyQt6.QtGraphs.QSurfaceDataItem`]]
        :description: QtGraphs/QSurface3DSeries-setDataArray-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurface3DSeries.setDataProxy
        :args:
            :sip:ref:`~PyQt6.QtGraphs.QSurfaceDataProxy`
        :description: QtGraphs/QSurface3DSeries-setDataProxy-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurface3DSeries.setDrawMode
        :args:
            :sip:ref:`~PyQt6.QtGraphs.QSurface3DSeries.DrawFlag`
        :description: QtGraphs/QSurface3DSeries-setDrawMode-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurface3DSeries.setSelectedPoint
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtGraphs/QSurface3DSeries-setSelectedPoint-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurface3DSeries.setShading
        :args:
            :sip:ref:`~PyQt6.QtGraphs.QSurface3DSeries.Shading`
        :description: QtGraphs/QSurface3DSeries-setShading-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurface3DSeries.setTexture
        :args:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtGraphs/QSurface3DSeries-setTexture-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurface3DSeries.setTextureFile
        :args:
            Optional[str]
        :description: QtGraphs/QSurface3DSeries-setTextureFile-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurface3DSeries.setWireframeColor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtGraphs/QSurface3DSeries-setWireframeColor-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurface3DSeries.shading
        :returns:
            :sip:ref:`~PyQt6.QtGraphs.QSurface3DSeries.Shading`
        :description: QtGraphs/QSurface3DSeries-shading-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurface3DSeries.texture
        :returns:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtGraphs/QSurface3DSeries-texture-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurface3DSeries.textureFile
        :returns:
            str
        :description: QtGraphs/QSurface3DSeries-textureFile-f.rst

    .. sip:method:: PyQt6.QtGraphs.QSurface3DSeries.wireframeColor
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtGraphs/QSurface3DSeries-wireframeColor-f.rst

    .. sip:signal:: PyQt6.QtGraphs.QSurface3DSeries.dataArrayChanged
        :args:
            Iterable[Iterable[:sip:ref:`~PyQt6.QtGraphs.QSurfaceDataItem`]]
        :description: QtGraphs/QSurface3DSeries-dataArrayChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QSurface3DSeries.dataProxyChanged
        :args:
            :sip:ref:`~PyQt6.QtGraphs.QSurfaceDataProxy`
        :description: QtGraphs/QSurface3DSeries-dataProxyChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QSurface3DSeries.drawModeChanged
        :args:
            :sip:ref:`~PyQt6.QtGraphs.QSurface3DSeries.DrawFlag`
        :description: QtGraphs/QSurface3DSeries-drawModeChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QSurface3DSeries.flatShadingSupportedChanged
        :args:
            bool
        :description: QtGraphs/QSurface3DSeries-flatShadingSupportedChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QSurface3DSeries.selectedPointChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QPoint`
        :description: QtGraphs/QSurface3DSeries-selectedPointChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QSurface3DSeries.shadingChanged
        :args:
            :sip:ref:`~PyQt6.QtGraphs.QSurface3DSeries.Shading`
        :description: QtGraphs/QSurface3DSeries-shadingChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QSurface3DSeries.textureChanged
        :args:
            :sip:ref:`~PyQt6.QtGui.QImage`
        :description: QtGraphs/QSurface3DSeries-textureChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QSurface3DSeries.textureFileChanged
        :args:
            Optional[str]
        :description: QtGraphs/QSurface3DSeries-textureFileChanged-s.rst

    .. sip:signal:: PyQt6.QtGraphs.QSurface3DSeries.wireframeColorChanged
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtGraphs/QSurface3DSeries-wireframeColorChanged-s.rst
