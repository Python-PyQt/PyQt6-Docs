:orphan:

.. sip:class:: PyQt6.QtQuick.QQuickPaintedItem
    :inherits: :sip:ref:`~PyQt6.QtQuick.QQuickItem`
    :description: QtQuick/QQuickPaintedItem-c.rst

    .. sip:enum:: PyQt6.QtQuick.QQuickPaintedItem.PerformanceHints
        :description: QtQuick/QQuickPaintedItem-PerformanceHints-e.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickPaintedItem.PerformanceHints.FastFBOResizing
            :description: QtQuick/QQuickPaintedItem-PerformanceHints-FastFBOResizing-v.rst

    .. sip:enum:: PyQt6.QtQuick.QQuickPaintedItem.RenderTarget
        :description: QtQuick/QQuickPaintedItem-RenderTarget-e.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickPaintedItem.RenderTarget.FramebufferObject
            :description: QtQuick/QQuickPaintedItem-RenderTarget-FramebufferObject-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickPaintedItem.RenderTarget.Image
            :description: QtQuick/QQuickPaintedItem-RenderTarget-Image-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QQuickPaintedItem.RenderTarget.InvertedYFramebufferObject
            :description: QtQuick/QQuickPaintedItem-RenderTarget-InvertedYFramebufferObject-v.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtQuick.QQuickItem` = None
        :description: QtQuick/QQuickPaintedItem-__init__-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.antialiasing
        :returns:
            bool
        :description: QtQuick/QQuickPaintedItem-antialiasing-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.contentsBoundingRect
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtQuick/QQuickPaintedItem-contentsBoundingRect-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.contentsScale
        :returns:
            float
        :description: QtQuick/QQuickPaintedItem-contentsScale-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.contentsSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtQuick/QQuickPaintedItem-contentsSize-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.fillColor
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtQuick/QQuickPaintedItem-fillColor-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.isTextureProvider
        :returns:
            bool
        :description: QtQuick/QQuickPaintedItem-isTextureProvider-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.itemChange
        :args:
            :sip:ref:`~PyQt6.QtQuick.QQuickItem.ItemChange`
            :sip:ref:`~PyQt6.QtQuick.QQuickItem.ItemChangeData`
        :description: QtQuick/QQuickPaintedItem-itemChange-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.mipmap
        :returns:
            bool
        :description: QtQuick/QQuickPaintedItem-mipmap-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.opaquePainting
        :returns:
            bool
        :description: QtQuick/QQuickPaintedItem-opaquePainting-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.paint
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
        :description: QtQuick/QQuickPaintedItem-paint-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.performanceHints
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QQuickPaintedItem.PerformanceHints`
        :description: QtQuick/QQuickPaintedItem-performanceHints-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.releaseResources
        :description: QtQuick/QQuickPaintedItem-releaseResources-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.renderTarget
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QQuickPaintedItem.RenderTarget`
        :description: QtQuick/QQuickPaintedItem-renderTarget-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.resetContentsSize
        :description: QtQuick/QQuickPaintedItem-resetContentsSize-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.setAntialiasing
        :args:
            bool
        :description: QtQuick/QQuickPaintedItem-setAntialiasing-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.setContentsScale
        :args:
            float
        :description: QtQuick/QQuickPaintedItem-setContentsScale-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.setContentsSize
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtQuick/QQuickPaintedItem-setContentsSize-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.setFillColor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`]
        :description: QtQuick/QQuickPaintedItem-setFillColor-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.setMipmap
        :args:
            bool
        :description: QtQuick/QQuickPaintedItem-setMipmap-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.setOpaquePainting
        :args:
            bool
        :description: QtQuick/QQuickPaintedItem-setOpaquePainting-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.setPerformanceHint
        :args:
            :sip:ref:`~PyQt6.QtQuick.QQuickPaintedItem.PerformanceHints`
            enabled: bool = True
        :description: QtQuick/QQuickPaintedItem-setPerformanceHint-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.setPerformanceHints
        :args:
            :sip:ref:`~PyQt6.QtQuick.QQuickPaintedItem.PerformanceHints`
        :description: QtQuick/QQuickPaintedItem-setPerformanceHints-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.setRenderTarget
        :args:
            :sip:ref:`~PyQt6.QtQuick.QQuickPaintedItem.RenderTarget`
        :description: QtQuick/QQuickPaintedItem-setRenderTarget-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.setTextureSize
        :args:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtQuick/QQuickPaintedItem-setTextureSize-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.textureProvider
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGTextureProvider`
        :description: QtQuick/QQuickPaintedItem-textureProvider-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.textureSize
        :returns:
            :sip:ref:`~PyQt6.QtCore.QSize`
        :description: QtQuick/QQuickPaintedItem-textureSize-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.update
        :args:
            rect: :sip:ref:`~PyQt6.QtCore.QRect` = QRect()
        :description: QtQuick/QQuickPaintedItem-update-f.rst

    .. sip:method:: PyQt6.QtQuick.QQuickPaintedItem.updatePaintNode
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGNode`
            :sip:ref:`~PyQt6.QtQuick.QQuickItem.UpdatePaintNodeData`
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGNode`
        :description: QtQuick/QQuickPaintedItem-updatePaintNode-f.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickPaintedItem.contentsScaleChanged
        :description: QtQuick/QQuickPaintedItem-contentsScaleChanged-s.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickPaintedItem.contentsSizeChanged
        :description: QtQuick/QQuickPaintedItem-contentsSizeChanged-s.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickPaintedItem.fillColorChanged
        :description: QtQuick/QQuickPaintedItem-fillColorChanged-s.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickPaintedItem.renderTargetChanged
        :description: QtQuick/QQuickPaintedItem-renderTargetChanged-s.rst

    .. sip:signal:: PyQt6.QtQuick.QQuickPaintedItem.textureSizeChanged
        :description: QtQuick/QQuickPaintedItem-textureSizeChanged-s.rst
