.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: d4262608cfdd4c6c7beca6d680a160ac

Requests choosing an adapter or physical device that uses software-based rasterization. Applicable only when the underlying API has support for enumerating adapters (for example, Direct 3D or Vulkan), and is ignored otherwise.

If the graphics API implementation has no such graphics adapter or physical device available, the request is ignored. With Direct 3D it can be expected that a `WARP <https://docs.microsoft.com/en-us/windows/win32/direct3darticles/directx-warp>`_-based rasterizer is always available. With Vulkan, the flag only has an effect if Mesa's ``lavapipe``, or some other physical device reporting ``VK_PHYSICAL_DEVICE_TYPE_CPU`` is available.

Calling this function with *enable* set to true is equivalent to setting the environment variable ``QSG_RHI_PREFER_SOFTWARE_RENDERER`` to a non-zero value.

The default value is false.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration.prefersSoftwareDevice`.
