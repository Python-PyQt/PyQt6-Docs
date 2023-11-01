.. sip:method-description::
    :status: todo
    :pysig: a820e7612bac80c6641eb15dc78b4388
    :realsig: () const
    :digest: fdcb0be11484a20b3947114b61cf56a2

When the underlying rendering API is OpenGL, this function should return a mask where each bit represents graphics states changed by the :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render` function:

+-------------------+---------------------------------------------------------------------------------------------+
| Constant          | Description                                                                                 |
+===================+=============================================================================================+
| DepthState        | depth write mask, depth test enabled, depth comparison function                             |
+-------------------+---------------------------------------------------------------------------------------------+
| StencilState      | stencil write masks, stencil test enabled, stencil operations, stencil comparison functions |
+-------------------+---------------------------------------------------------------------------------------------+
| ScissorState      | scissor enabled, scissor test enabled                                                       |
+-------------------+---------------------------------------------------------------------------------------------+
| ColorState        | clear color, color write mask                                                               |
+-------------------+---------------------------------------------------------------------------------------------+
| BlendState        | blend enabled, blend function                                                               |
+-------------------+---------------------------------------------------------------------------------------------+
| CullState         | front face, cull face enabled                                                               |
+-------------------+---------------------------------------------------------------------------------------------+
| ViewportState     | viewport                                                                                    |
+-------------------+---------------------------------------------------------------------------------------------+
| RenderTargetState | render target                                                                               |
+-------------------+---------------------------------------------------------------------------------------------+

With APIs other than OpenGL, the only relevant values are the ones that correspond to dynamic state changes recorded on the command list/buffer. For example, RSSetViewports, RSSetScissorRects, OMSetBlendState, OMSetDepthStencilState in case of D3D11, or vkCmdSetViewport, vkCmdSetScissor, vkCmdSetBlendConstants, vkCmdSetStencilRef in case of Vulkan, and only when such commands were added to the scenegraph's command list queried via the QSGRendererInterface::CommandList resource enum. States set in pipeline state objects do not need to be reported here. Similarly, draw call related settings (pipeline states, descriptor sets, vertex or index buffer bindings, root signature, descriptor heaps, etc.) are always set again by the scenegraph so :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render` can freely change them.

**Note:** :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.StateFlag.RenderTargetState` is no longer supported with APIs like Vulkan. This is by nature. :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render` is invoked while the Qt Quick scenegraph's main command buffer is recording a renderpass, so there is no possibility of changing the target and starting another renderpass (on that command buffer at least). Therefore returning a value with :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.StateFlag.RenderTargetState` set is not sensible.

The software backend exposes its :sip:ref:`~PyQt6.QtGui.QPainter` and saves and restores before and after invoking :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render`. Therefore reporting any changed states from here is not necessary.

The function is called by the renderer so it can reset the states after rendering this node. This makes the implementation of :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render` simpler since it does not have to query and restore these states.

The default implementation returns 0, meaning no relevant state was changed in :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render`.

**Note:** This function may be called before :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render`.
