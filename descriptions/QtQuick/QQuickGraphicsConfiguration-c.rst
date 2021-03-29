.. sip:class-description::
    :status: todo
    :brief: Container for low-level graphics settings that can affect how the underlying graphics API, such as Vulkan, is initialized by the Qt Quick scene graph. It can also control certain aspects of the scene graph renderer
    :digest: 2333c2f3e25a5dcbd356f6a78ba40768

The :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration` class is a container for low-level graphics settings that can affect how the underlying graphics API, such as Vulkan, is initialized by the Qt Quick scene graph. It can also control certain aspects of the scene graph renderer.

When constructing and showing a :sip:ref:`~PyQt6.QtQuick.QQuickWindow` that uses Vulkan to render, a Vulkan instance (``VkInstance``), a physical device (``VkPhysicalDevice``), a device (``VkDevice``) and associated objects (queues, pools) are initialized through the Vulkan API. The same is mostly true when using :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl` to redirect the rendering into a custom render target, such as a texture. While QVulkanInstance construction is under the application's control then, the initialization of other graphics objects happen the same way in :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.initialize` as with an on-screen :sip:ref:`~PyQt6.QtQuick.QQuickWindow`.

For the majority of applications no additional configuration is needed because Qt Quick provides reasonable defaults for many low-level graphics settings, for example which device extensions to enable.

This will not alway be sufficient, however. In advanced use cases, when integrating direct Vulkan or other graphics API content, or when integrating with an external 3D or VR engine, such as, OpenXR, the application will want to specify its own set of settings when it comes to details, such as which device extensions to enable.

That is what this class enables. It allows specifying, for example, a list of device extensions that is then picked up by the scene graph when using Vulkan, or graphics APIs where the concept is applicable. Where some concepts are not applicable, the related settings are simply ignored.

Another class of settings are related to the scene graph's renderer. In some cases applications may want to control certain behavior,such as using the depth buffer when rendering 2D content. In Qt 5 such settings were either not controllable at all, or were managed through environment variables. In Qt 6, :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration` provides a new home for these settings, while keeping support for the legacy environment variables, where applicable.

**Note:** Setting a :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration` on a :sip:ref:`~PyQt6.QtQuick.QQuickWindow` must happen early enough, before the scene graph is initialized for the first time for that window. With on-screen windows this means the call must be done before invoking show() on the :sip:ref:`~PyQt6.QtQuick.QQuickWindow` or :sip:ref:`~PyQt6.QtQuick.QQuickView`. With :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl` the configuration must be finalized before calling :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.initialize`.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setGraphicsConfiguration`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow`, :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl`.
