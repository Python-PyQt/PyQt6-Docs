.. sip:method-description::
    :status: todo
    :pysig: 81e0924ce8a94a47a0a87c7ffcda73a8
    :realsig: (const QQuickRenderTarget&)
    :digest: 12d1a04c1ceb3dd6cb99d5b2254ae230

Sets the render target for this window to be *target*.

A :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget` serves as an opaque handle for a renderable native object, most commonly a 2D texture, and associated metadata, such as the size in pixels.

A default constructed :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget` means no redirection. A valid *target*, created via one of the static :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget` factory functions, on the other hand, enables redirection of the rendering of the Qt Quick scene: it will no longer target the color buffers for the surface associated with the window, but rather the textures or other graphics objects specified in *target*.

For example, assuming the scenegraph is using Vulkan to render, one can redirect its output into a ``VkImage``. For graphics APIs like Vulkan, the image layout must be provided as well. :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget` instances are implicitly shared and are copyable and can be passed by value. They do not own the associated native objects (such as, the VkImage in the example), however.

::

    QQuickRenderTarget rt = QQuickRenderTarget::fromVulkanImage(vulkanImage, VK_IMAGE_LAYOUT_PREINITIALIZED, pixelSize);
    quickWindow->setRenderTarget(rt);

This function is very often used in combination with :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl` and an invisible :sip:ref:`~PyQt6.QtQuick.QQuickWindow`, in order to render Qt Quick content into a texture, without creating an on-screen native window for this :sip:ref:`~PyQt6.QtQuick.QQuickWindow`.

When the desired target, or associated data, such as the size, changes, call this function with a new :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget`. Constructing :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget` instances and calling this function is cheap, but be aware that setting a new *target* with a different native object or other data may lead to potentially expensive initialization steps when the scenegraph is about to render the next frame. Therefore change the target only when necessary.

**Note:** This function should not be used when using the ``software`` backend. Instead, use :sip:ref:`~PyQt6.QtQuick.QQuickWindow.grabWindow` to render the content into a :sip:ref:`~PyQt6.QtGui.QImage`.

**Note:** The window does not take ownership of any native objects referenced in *target*.

**Note:** It is the caller's responsibility to ensure the native objects referred to in *target* are valid for the scenegraph renderer too. For instance, with Vulkan, Metal, and Direct3D this implies that the texture or image is created on the same graphics device that is used by the scenegraph internally. Therefore, when texture objects created on an already existing device or context are involved, this function is often used in combination with :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setGraphicsDevice`.

**Note:** With graphics APIs where relevant, the application must pay attention to image layout transitions performed by the scenegraph. For example, once a VkImage is associated with the scenegraph by calling this function, its layout will transition to ``VK_IMAGE_LAYOUT_COLOR_ATTACHMENT_OPTIMAL`` when rendering a frame.

**Warning:** This function can only be called from the thread doing the rendering.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.renderTarget`, :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setGraphicsDevice`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setGraphicsApi`.
