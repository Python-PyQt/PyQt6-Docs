.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 952f55d3d3e31e880a4792feedc303a0

Enables the graphics API implementation's debug or validation layers, if available.

In practice this is supported with Vulkan and Direct 3D 11, assuming the necessary support (validation layers, Windows SDK) is installed and available at runtime. When *enable* is true, Qt will attempt to enable the standard validation layer on the VkInstance, or set ``D3D11_CREATE_DEVICE_DEBUG`` on the graphics device.

For Metal on macOS, set the environment variable ``METAL_DEVICE_WRAPPER_TYPE=1`` instead before launching the application.

Calling this function with *enable* set to true is equivalent to setting the environment variable ``QSG_RHI_DEBUG_LAYER`` to a non-zero value.

The default value is false.

**Note:** Enabling debug or validation layers may have a non-insignificant performance impact. Shipping applications to production with the flag enabled is strongly discouraged.

**Note:** Be aware that due to differences in the design of the underlying graphics APIs, this setting cannot always be a per-\ :sip:ref:`~PyQt6.QtQuick.QQuickWindow` setting, even though each :sip:ref:`~PyQt6.QtQuick.QQuickWindow` has their own :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration`. With Vulkan in particular, the instance object (VkInstance) is only created once and then used by all windows in the application. Therefore, enabling the validation layer is something that affects all windows. This also means that attempting to enable validation via a window that only gets shown after some other windows have already started rendering has no effect with Vulkan. Other APIs, such as D3D11, expose the debug layer concept as a per-device (ID3D11Device) setting, and so it is controlled on a true per-window basis (assuming the scenegraph render loop uses a dedicated graphics device/context for each :sip:ref:`~PyQt6.QtQuick.QQuickWindow`).

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration.isDebugLayerEnabled`.
