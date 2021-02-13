.. sip:enum-member-description::
    :status: todo
    :value: 0
    :digest: 5e0d9571396cc67404105e3f3711986c

The resource is a pointer to the graphics device, when applicable. For example, a ``VkDevice \*``, ``MTLDevice \*`` or ``ID3D11Device \*``. Note that with Vulkan the returned value is a pointer to the VkDevice, not the handle itself. This is because Vulkan handles may not be pointers, and may use a different size from the architecture's pointer size so merely casting to/from ``void \*`` is wrong.
