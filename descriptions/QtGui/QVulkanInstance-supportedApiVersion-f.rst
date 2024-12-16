.. sip:method-description::
    :status: todo
    :pysig: e067a21998652d1aaf9dc7a94f484b86
    :realsig: () const
    :digest: 044face160f131300e85c5d54329de4a

Returns the version of instance-level functionality supported by the Vulkan implementation.

In practice this is either the value returned from vkEnumerateInstanceVersion, if that function is available (with Vulkan 1.1 and newer), or 1.0.

Applications that want to branch in their Vulkan feature and API usage based on what Vulkan version is available at run time, can use this function to determine what version to pass in to :sip:ref:`~PyQt6.QtGui.QVulkanInstance.setApiVersion` before calling :sip:ref:`~PyQt6.QtGui.QVulkanInstance.create`.

**Note:** This function can be called before :sip:ref:`~PyQt6.QtGui.QVulkanInstance.create`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QVulkanInstance.setApiVersion`.
