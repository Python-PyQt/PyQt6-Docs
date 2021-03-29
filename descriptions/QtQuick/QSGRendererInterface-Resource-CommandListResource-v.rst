.. sip:enum-member-description::
    :status: todo
    :value: 2
    :digest: 58dc053d4102e720c382823780536ca1

The resource is a pointer to the command list or buffer used by the scenegraph, when applicable. For example, a ``VkCommandBuffer \*`` or ``MTLCommandBuffer \*``. This object has limited validity, and is only valid while the scene graph is preparing the next frame. Note that with Vulkan the returned value is a pointer to the VkCommandBuffer, not the handle itself.
