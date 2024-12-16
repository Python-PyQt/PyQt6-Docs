.. sip:method-description::
    :status: todo
    :pysig: e067a21998652d1aaf9dc7a94f484b86
    :realsig: (const QVersionNumber&)
    :digest: d08ac178faebb524aa9799fa21afefa8

Specifies the highest Vulkan API version the application is designed to use.

By default *vulkanVersion* is 0, which maps to Vulkan 1.0.

**Note:** This function can only be called before :sip:ref:`~PyQt6.QtGui.QVulkanInstance.create` and has no effect if called afterwards.

**Note:** Be aware that Vulkan 1.1 changes the behavior with regards to the Vulkan API version field. In Vulkan 1.0 specifying an unsupported *vulkanVersion* led to failing :sip:ref:`~PyQt6.QtGui.QVulkanInstance.create` with ``VK_ERROR_INCOMPATIBLE_DRIVER``, as was mandated by the specification. Starting with Vulkan 1.1, the specification disallows this, the driver must accept any version without failing the instance creation.

Application developers are advised to familiarize themselves with the ``apiVersion`` notes in `the Vulkan specification <https://www.khronos.org/registry/vulkan/specs/1.2-extensions/man/html/VkApplicationInfo.html>`_.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QVulkanInstance.apiVersion`, :sip:ref:`~PyQt6.QtGui.QVulkanInstance.supportedApiVersion`.
