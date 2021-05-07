.. sip:method-description::
    :status: todo
    :pysig: a9de941641bfc9e1529fe64f342cdb3e
    :realsig: ()
    :digest: 6e530bb2cea152a4d0966616a6c3fe53

Returns the list of Vulkan instance extensions Qt Quick prefers to have enabled on the VkInstance.

In most cases Qt Quick is responsible for creating a QVulkanInstance. This function is not relevant then. On the other hand, when using :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl` in combination with Vulkan-based rendering, it is the application's responsibility to create a QVulkanInstance and associate it with the (offscreen) :sip:ref:`~PyQt6.QtQuick.QQuickWindow`. In this case, it is expected that the application queries the list of instance extensions to enable, and passes them to QVulkanInstance::setExtensions() before calling QVulkanInstance::create().
