:orphan:

.. sip:class:: PyQt6.QtQuick.QSGRenderNode
    :inherits: :sip:ref:`~PyQt6.QtQuick.QSGNode`
    :description: QtQuick/QSGRenderNode-c.rst

    .. sip:enum:: PyQt6.QtQuick.QSGRenderNode.RenderingFlag
        :description: QtQuick/QSGRenderNode-RenderingFlag-e.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGRenderNode.RenderingFlag.BoundedRectRendering
            :description: QtQuick/QSGRenderNode-RenderingFlag-BoundedRectRendering-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGRenderNode.RenderingFlag.DepthAwareRendering
            :description: QtQuick/QSGRenderNode-RenderingFlag-DepthAwareRendering-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGRenderNode.RenderingFlag.OpaqueRendering
            :description: QtQuick/QSGRenderNode-RenderingFlag-OpaqueRendering-v.rst

    .. sip:enum:: PyQt6.QtQuick.QSGRenderNode.StateFlag
        :description: QtQuick/QSGRenderNode-StateFlag-e.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGRenderNode.StateFlag.BlendState
            :description: QtQuick/QSGRenderNode-StateFlag-BlendState-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGRenderNode.StateFlag.ColorState
            :description: QtQuick/QSGRenderNode-StateFlag-ColorState-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGRenderNode.StateFlag.CullState
            :description: QtQuick/QSGRenderNode-StateFlag-CullState-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGRenderNode.StateFlag.DepthState
            :description: QtQuick/QSGRenderNode-StateFlag-DepthState-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGRenderNode.StateFlag.RenderTargetState
            :description: QtQuick/QSGRenderNode-StateFlag-RenderTargetState-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGRenderNode.StateFlag.ScissorState
            :description: QtQuick/QSGRenderNode-StateFlag-ScissorState-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGRenderNode.StateFlag.StencilState
            :description: QtQuick/QSGRenderNode-StateFlag-StencilState-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGRenderNode.StateFlag.ViewportState
            :description: QtQuick/QSGRenderNode-StateFlag-ViewportState-v.rst

    .. sip:method:: PyQt6.QtQuick.QSGRenderNode.__init__
        :description: QtQuick/QSGRenderNode-__init__-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGRenderNode.changedStates
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.StateFlag`
        :description: QtQuick/QSGRenderNode-changedStates-f-1.rst

    .. sip:method:: PyQt6.QtQuick.QSGRenderNode.clipList
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGClipNode`
        :description: QtQuick/QSGRenderNode-clipList-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGRenderNode.flags
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.RenderingFlag`
        :description: QtQuick/QSGRenderNode-flags-f-1.rst

    .. sip:method:: PyQt6.QtQuick.QSGRenderNode.inheritedOpacity
        :returns:
            float
        :description: QtQuick/QSGRenderNode-inheritedOpacity-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGRenderNode.matrix
        :returns:
            :sip:ref:`~PyQt6.QtGui.QMatrix4x4`
        :description: QtQuick/QSGRenderNode-matrix-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGRenderNode.prepare
        :description: QtQuick/QSGRenderNode-prepare-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGRenderNode.projectionMatrix
        :returns:
            :sip:ref:`~PyQt6.QtGui.QMatrix4x4`
        :description: QtQuick/QSGRenderNode-projectionMatrix-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGRenderNode.rect
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtQuick/QSGRenderNode-rect-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGRenderNode.releaseResources
        :description: QtQuick/QSGRenderNode-releaseResources-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGRenderNode.render
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.RenderState`
        :description: QtQuick/QSGRenderNode-render-f.rst
