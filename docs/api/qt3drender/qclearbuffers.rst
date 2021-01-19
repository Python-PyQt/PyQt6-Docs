:orphan:

.. sip:class:: PyQt6.Qt3DRender.QClearBuffers
    :inherits: :sip:ref:`~PyQt6.Qt3DRender.QFrameGraphNode`
    :description: Qt3DRender/QClearBuffers-c.rst

    .. sip:enum:: PyQt6.Qt3DRender.QClearBuffers.BufferType
        :description: Qt3DRender/QClearBuffers-BufferType-e.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QClearBuffers.BufferType.AllBuffers
            :description: Qt3DRender/QClearBuffers-BufferType-AllBuffers-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QClearBuffers.BufferType.ColorBuffer
            :description: Qt3DRender/QClearBuffers-BufferType-ColorBuffer-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QClearBuffers.BufferType.ColorDepthBuffer
            :description: Qt3DRender/QClearBuffers-BufferType-ColorDepthBuffer-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QClearBuffers.BufferType.ColorDepthStencilBuffer
            :description: Qt3DRender/QClearBuffers-BufferType-ColorDepthStencilBuffer-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QClearBuffers.BufferType.DepthBuffer
            :description: Qt3DRender/QClearBuffers-BufferType-DepthBuffer-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QClearBuffers.BufferType.DepthStencilBuffer
            :description: Qt3DRender/QClearBuffers-BufferType-DepthStencilBuffer-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QClearBuffers.BufferType.None_
            :description: Qt3DRender/QClearBuffers-BufferType-None_-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QClearBuffers.BufferType.StencilBuffer
            :description: Qt3DRender/QClearBuffers-BufferType-StencilBuffer-v.rst

    .. sip:method:: PyQt6.Qt3DRender.QClearBuffers.__init__
        :args:
            parent: :sip:ref:`~PyQt6.Qt3DCore.QNode` = None
        :description: Qt3DRender/QClearBuffers-__init__-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QClearBuffers.buffers
        :returns:
            :sip:ref:`~PyQt6.Qt3DRender.QClearBuffers.BufferType`
        :description: Qt3DRender/QClearBuffers-buffers-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QClearBuffers.clearColor
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: Qt3DRender/QClearBuffers-clearColor-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QClearBuffers.clearDepthValue
        :returns:
            float
        :description: Qt3DRender/QClearBuffers-clearDepthValue-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QClearBuffers.clearStencilValue
        :returns:
            int
        :description: Qt3DRender/QClearBuffers-clearStencilValue-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QClearBuffers.colorBuffer
        :returns:
            :sip:ref:`~PyQt6.Qt3DRender.QRenderTargetOutput`
        :description: Qt3DRender/QClearBuffers-colorBuffer-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QClearBuffers.setBuffers
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QClearBuffers.BufferType`
        :description: Qt3DRender/QClearBuffers-setBuffers-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QClearBuffers.setClearColor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`]
        :description: Qt3DRender/QClearBuffers-setClearColor-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QClearBuffers.setClearDepthValue
        :args:
            float
        :description: Qt3DRender/QClearBuffers-setClearDepthValue-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QClearBuffers.setClearStencilValue
        :args:
            int
        :description: Qt3DRender/QClearBuffers-setClearStencilValue-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QClearBuffers.setColorBuffer
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QRenderTargetOutput`
        :description: Qt3DRender/QClearBuffers-setColorBuffer-f.rst

    .. sip:signal:: PyQt6.Qt3DRender.QClearBuffers.buffersChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QClearBuffers.BufferType`
        :description: Qt3DRender/QClearBuffers-buffersChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QClearBuffers.clearColorChanged
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`]
        :description: Qt3DRender/QClearBuffers-clearColorChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QClearBuffers.clearDepthValueChanged
        :args:
            float
        :description: Qt3DRender/QClearBuffers-clearDepthValueChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QClearBuffers.clearStencilValueChanged
        :args:
            int
        :description: Qt3DRender/QClearBuffers-clearStencilValueChanged-s.rst

    .. sip:signal:: PyQt6.Qt3DRender.QClearBuffers.colorBufferChanged
        :args:
            :sip:ref:`~PyQt6.Qt3DRender.QRenderTargetOutput`
        :description: Qt3DRender/QClearBuffers-colorBufferChanged-s.rst
