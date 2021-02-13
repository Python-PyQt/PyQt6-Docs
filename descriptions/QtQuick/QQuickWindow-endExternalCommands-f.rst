.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 6d8ffeb8385fda7ec4683b9d8fb1cb12

When mixing raw graphics (OpenGL, Vulkan, Metal, etc.) commands with scene graph rendering, it is necessary to call this function after recording commands to the command buffer used by the scene graph to render its main render pass. This is to avoid clobbering state.

In practice this function is often called from a slot connected to the :sip:ref:`~PyQt6.QtQuick.QQuickWindow.beforeRenderPassRecording` or :sip:ref:`~PyQt6.QtQuick.QQuickWindow.afterRenderPassRecording` signals.

The function does not need to be called when recording commands to the application's own command buffer (such as, a VkCommandBuffer or MTLCommandBuffer + MTLRenderCommandEncoder created and managed by the application, not retrieved from the scene graph). With graphics APIs where no native command buffer concept is exposed (OpenGL, Direct 3D 11), :sip:ref:`~PyQt6.QtQuick.QQuickWindow.beginExternalCommands` and  together provide a replacement for the Qt 5 resetOpenGLState() function.

Calling this function and :sip:ref:`~PyQt6.QtQuick.QQuickWindow.beginExternalCommands` is not necessary within the :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render` implementation of a :sip:ref:`~PyQt6.QtQuick.QSGRenderNode` because the scene graph performs the necessary steps implicitly for render nodes.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.beginExternalCommands`, QQuickOpenGLUtils::resetOpenGLState().
