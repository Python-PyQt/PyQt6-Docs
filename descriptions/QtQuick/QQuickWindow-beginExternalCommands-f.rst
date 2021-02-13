.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 9a94566b492205e3ecadbc0802dfd73b

When mixing raw graphics (OpenGL, Vulkan, Metal, etc.) commands with scene graph rendering, it is necessary to call this function before recording commands to the command buffer used by the scene graph to render its main render pass. This is to avoid clobbering state.

In practice this function is often called from a slot connected to the :sip:ref:`~PyQt6.QtQuick.QQuickWindow.beforeRenderPassRecording` or :sip:ref:`~PyQt6.QtQuick.QQuickWindow.afterRenderPassRecording` signals.

The function does not need to be called when recording commands to the application's own command buffer (such as, a VkCommandBuffer or MTLCommandBuffer + MTLRenderCommandEncoder created and managed by the application, not retrieved from the scene graph). With graphics APIs where no native command buffer concept is exposed (OpenGL, Direct 3D 11),  and :sip:ref:`~PyQt6.QtQuick.QQuickWindow.endExternalCommands` together provide a replacement for the Qt 5 resetOpenGLState() function.

Calling this function and :sip:ref:`~PyQt6.QtQuick.QQuickWindow.endExternalCommands` is not necessary within the :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render` implementation of a :sip:ref:`~PyQt6.QtQuick.QSGRenderNode` because the scene graph performs the necessary steps implicitly for render nodes.

Native graphics objects (such as, graphics device, command buffer or encoder) are accessible via :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface.getResource`.

**Warning:** Watch out for the fact that :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface.Resource.CommandListResource` may return a different object between  - :sip:ref:`~PyQt6.QtQuick.QQuickWindow.endExternalCommands`. This can happen when the underlying implementation provides a dedicated secondary command buffer for recording external graphics commands within a render pass. Therefore, always query CommandListResource after calling this function. Do not attempt to reuse an object from an earlier query.

**Note:** When the scenegraph is using OpenGL, pay attention to the fact that the OpenGL state in the context can have arbitrary settings, and this function does not perform any resetting of the state back to defaults.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.endExternalCommands`, QQuickOpenGLUtils::resetOpenGLState().
