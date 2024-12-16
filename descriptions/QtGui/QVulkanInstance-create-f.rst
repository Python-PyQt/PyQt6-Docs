.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 3bf9ff379f5848f519d8391838fb1310

Initializes the Vulkan library and creates a new or adopts and existing Vulkan instance.

Returns true if successful, false on error or when Vulkan is not supported.

When successful, the pointer to this :sip:ref:`~PyQt6.QtGui.QVulkanInstance` is retrievable via vkInstance().

The Vulkan instance and library is available as long as this :sip:ref:`~PyQt6.QtGui.QVulkanInstance` exists, or until :sip:ref:`~PyQt6.QtGui.QVulkanInstance.destroy` is called.

By default the VkInstance is created with the flag `VK_INSTANCE_CREATE_ENUMERATE_PORTABILITY_BIT_KHR <https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VkInstanceCreateFlagBits.html>`_ set. This means that Vulkan Portability physical devices get enumerated as well. If this is not desired, set the NoPortabilityDrivers flag.
