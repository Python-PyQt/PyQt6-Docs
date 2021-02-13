.. sip:method-description::
    :status: todo
    :pysig: f73749e1be44c336279cb675c2ba815b
    :realsig: (const QQuickGraphicsConfiguration&)
    :digest: 7103fd1c3f62140e9b0a78c7083ed81c

Sets the graphics configuration for this window. *config* contains various settings that may be taken into account by the scene graph when initializing the underlying graphics devices and contexts.

Such additional configuration, specifying for example what device extensions to enable for Vulkan, becomes relevant and essential when integrating native graphics rendering code that relies on certain extensions. The same is true when integrating with an external 3D or VR engines, such as OpenXR.

**Note:** The configuration is ignored when adopting existing graphics devices via :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setGraphicsDevice` since the scene graph is then not in control of the actual construction of those objects.

:sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration` instances are implicitly shared, copyable, and can be passed by value.

**Warning:** Setting a :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration` on a :sip:ref:`~PyQt6.QtQuick.QQuickWindow` must happen early enough, before the scene graph is initialized for the first time for that window. With on-screen windows this means the call must be done before invoking show() on the :sip:ref:`~PyQt6.QtQuick.QQuickWindow` or :sip:ref:`~PyQt6.QtQuick.QQuickView`. With :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl` the configuration must be finalized before calling :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.initialize`.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.graphicsConfiguration`.
