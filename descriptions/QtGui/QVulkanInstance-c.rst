.. sip:class-description::
    :status: todo
    :brief: Represents a native Vulkan instance, enabling Vulkan rendering onto a QSurface
    :digest: d005f77347c994d110f1e7b02005690c

The :sip:ref:`~PyQt6.QtGui.QVulkanInstance` class represents a native Vulkan instance, enabling Vulkan rendering onto a :sip:ref:`~PyQt6.QtGui.QSurface`.

`Vulkan <https://www.khronos.org/vulkan/>`_ is a cross-platform, explicit graphics and compute API. This class provides support for loading a Vulkan library and creating an ``instance`` in a cross-platform manner. For an introduction on Vulkan instances, refer `to section 3.2 of the specification <https://www.khronos.org/registry/vulkan/specs/1.0/html/vkspec.html#initialization-instances>`_.

**Note:** Platform-specific support for Vulkan instances and windows with Vulkan-capable surfaces is provided by the various platform plugins. Not all of them will support Vulkan, however. When running on such a platform, :sip:ref:`~PyQt6.QtGui.QVulkanInstance.create` will fail and always return ``false``.

**Note:** Vulkan support may get automatically disabled for a given Qt build due to not having the necessary Vulkan headers available at build time. When this is the case, and the output of ``configure`` indicates Vulkan support is disabled, the QVulkan\* classes will be unavailable.

**Note:** Some functions changed their signature between the various Vulkan header revisions. When building Qt and only headers with the old, conflicting signatures are present in a system, Vulkan support will get disabled. It is recommended to use headers from Vulkan 1.0.39 or newer.

.. _qvulkaninstance-initialization:

Initialization
--------------

Similarly to :sip:ref:`~PyQt6.QtGui.QOpenGLContext`, any actual Vulkan instance creation happens only when calling :sip:ref:`~PyQt6.QtGui.QVulkanInstance.create`. This allows using :sip:ref:`~PyQt6.QtGui.QVulkanInstance` as a plain member variable while retaining control over when to perform initialization.

Querying the supported instance-level layers and extensions is possible by calling :sip:ref:`~PyQt6.QtGui.QVulkanInstance.supportedLayers` and :sip:ref:`~PyQt6.QtGui.QVulkanInstance.supportedExtensions`. These ensure the Vulkan library is loaded, and can therefore be called safely before :sip:ref:`~PyQt6.QtGui.QVulkanInstance.create` as well.

Instances store per-application Vulkan state and creating a ``VkInstance`` object initializes the Vulkan library. In practice there will typically be a single instance constructed early on in main(). The object then stays alive until exiting the application.

Every Vulkan-based :sip:ref:`~PyQt6.QtGui.QWindow` must be associated with a :sip:ref:`~PyQt6.QtGui.QVulkanInstance` by calling :sip:ref:`~PyQt6.QtGui.QWindow.setVulkanInstance`. Thus a typical application pattern is the following:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_vulkan_qvulkaninstance.py
    :lines: 21-34

.. _qvulkaninstance-configuration:

Configuration
-------------

:sip:ref:`~PyQt6.QtGui.QVulkanInstance` automatically enables the minimum set of extensions it needs on the newly created instance. In practice this means the ``VK_KHR_\*_surface`` family of extensions.

By default Vulkan debug output, for example messages from the validation layers, is routed to :sip:ref:`~PyQt6.QtCore.qDebug`. This can be disabled by passing the flag ``NoDebugOutputRedirect`` to setFlags() *before* invoking :sip:ref:`~PyQt6.QtGui.QVulkanInstance.create`.

To enable additional layers and extensions, provide the list via setLayers() and setExtensions() *before* invoking :sip:ref:`~PyQt6.QtGui.QVulkanInstance.create`. When a given layer or extension is not reported as available from the instance, the request is ignored. After a successful call to :sip:ref:`~PyQt6.QtGui.QVulkanInstance.create`, the values returned from functions like layers() and extensions() reflect the actual enabled layers and extensions. When necessary, for example to avoid requesting extensions that conflict and thus would fail the Vulkan instance creation, the list of actually supported layers and extensions can be examined via :sip:ref:`~PyQt6.QtGui.QVulkanInstance.supportedLayers` and :sip:ref:`~PyQt6.QtGui.QVulkanInstance.supportedExtensions` before calling :sip:ref:`~PyQt6.QtGui.QVulkanInstance.create`.

For example, to enable the standard validation layers, one could do the following:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_vulkan_qvulkaninstance.py
    :lines: 40-52

Or, alternatively, to make decisions before attempting to create a Vulkan instance:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_vulkan_qvulkaninstance.py
    :lines: 59-65

.. _qvulkaninstance-adopting-an-existing-instance:

Adopting an Existing Instance
-----------------------------

By default :sip:ref:`~PyQt6.QtGui.QVulkanInstance` creates a new Vulkan instance. When working with external engines and renderers, this may sometimes not be desirable. When there is a ``VkInstance`` handle already available, call setVkInstance() before invoking :sip:ref:`~PyQt6.QtGui.QVulkanInstance.create`. This way no additional instances will get created, and :sip:ref:`~PyQt6.QtGui.QVulkanInstance` will not own the handle.

**Note:** It is up to the component creating the external instance to ensure the necessary extensions are enabled on it. These are: ``VK_KHR_surface``, the WSI-specific ``VK_KHR_\*_surface`` that is appropriate for the platform in question, and ``VK_EXT_debug_utils`` in case :sip:ref:`~PyQt6.QtGui.QVulkanInstance`'s debug output redirection is desired.

.. _qvulkaninstance-accessing-core-vulkan-commands:

Accessing Core Vulkan Commands
------------------------------

To access the ``VkInstance`` handle the :sip:ref:`~PyQt6.QtGui.QVulkanInstance` wraps, call vkInstance(). To resolve Vulkan functions, call getInstanceProcAddr(). For core Vulkan commands manual resolving is not necessary as they are provided via the QVulkanFunctions and QVulkanDeviceFunctions objects accessible via functions() and deviceFunctions().

**Note:** QVulkanFunctions and QVulkanDeviceFunctions are generated from the Vulkan API XML specifications when building the Qt libraries. Therefore no documentation is provided for them. They contain the Vulkan 1.2 functions with the same signatures as described in the `Vulkan API documentation <https://www.khronos.org/registry/vulkan/specs/1.2/html/>`_.

.. _qvulkaninstance-getting-a-native-vulkan-surface-for-a-window:

Getting a Native Vulkan Surface for a Window
--------------------------------------------

The two common windowing system specific operations are getting a surface (a ``VkSurfaceKHR`` handle) for a window, and querying if a given queue family supports presenting to a given surface. To avoid WSI-specific bits in the applications, these are abstracted by :sip:ref:`~PyQt6.QtGui.QVulkanInstance` and the underlying QPA layers.

To create a Vulkan surface for a window, or retrieve an existing one, call :sip:ref:`~PyQt6.QtGui.QVulkanInstance.surfaceForWindow`. Most platforms will only create the surface via ``VK_KHR_\*_surface`` when first calling :sip:ref:`~PyQt6.QtGui.QVulkanInstance.surfaceForWindow`, but there may be platform-specific variations in the internal behavior. Once created, subsequent calls to :sip:ref:`~PyQt6.QtGui.QVulkanInstance.surfaceForWindow` just return the same handle. This fits the structure of typical Vulkan-enabled :sip:ref:`~PyQt6.QtGui.QWindow` subclasses well.

To query if a given queue family within a physical device can be used to perform presentation to a given surface, call supportsPresent(). This encapsulates both the generic ``vkGetPhysicalDeviceSurfaceSupportKHR`` and the WSI-specific ``vkGetPhysicalDevice\*PresentationSupportKHR`` checks.

.. _qvulkaninstance-troubleshooting:

Troubleshooting
---------------

Besides returning ``false`` from :sip:ref:`~PyQt6.QtGui.QVulkanInstance.create` or ``0`` from :sip:ref:`~PyQt6.QtGui.QVulkanInstance.surfaceForWindow`, critical errors will also get printed to the debug output via :sip:ref:`~PyQt6.QtCore.qWarning`. Additional logging can be requested by enabling debug output for the logging category ``qt.vulkan``. The actual Vulkan error code from instance creation can be retrieved by calling errorCode() after a failing :sip:ref:`~PyQt6.QtGui.QVulkanInstance.create`.

In some special cases it may be necessary to override the Vulkan library name. This can be achieved by setting the ``QT_VULKAN_LIB`` environment variable.

.. _qvulkaninstance-example:

Example
-------

The following is the basic outline of creating a Vulkan-capable :sip:ref:`~PyQt6.QtGui.QWindow`:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_vulkan_qvulkaninstance.py
    :lines: 76-129

**Note:** In addition to expose, a well-behaving window implementation will also have to take care of additional events like resize and :sip:ref:`~PyQt6.QtGui.QPlatformSurfaceEvent` in order to ensure proper management of the swap chain. Additionally, some platforms may require releasing resources when not being exposed anymore.

.. _qvulkaninstance-using-c-bindings-for-vulkan:

Using C++ Bindings for Vulkan
-----------------------------

Combining Qt's Vulkan enablers with a C++ Vulkan wrapper, for example `Vulkan-Hpp <https://github.com/KhronosGroup/Vulkan-Hpp>`_, is possible as well. The pre-requisite here is that the C++ layer must be able to adopt native handles (VkInstance, VkSurfaceKHR) in its classes without taking ownership (since the ownership stays with :sip:ref:`~PyQt6.QtGui.QVulkanInstance` and :sip:ref:`~PyQt6.QtGui.QWindow`). Consider also the following:

* Some wrappers require exception support to be enabled. Qt does not use exceptions. To enable exceptions for the application, add ``CONFIG += exceptions`` to the ``.pro`` file.

* Some wrappers call Vulkan functions directly, assuming ``vulkan.h`` provides prototypes and the application links to a Vulkan library exporting all necessary symbols. Qt may not directly link to a Vulkan library. Therefore, on some platforms it may be necessary to add ``LIBS += -lvulkan`` or similar in the application's ``.pro`` file.

* The headers for the QVulkan classes may include ``vulkan.h`` with ``VK_NO_PROTOTYPES`` enabled. This can cause issues in C++ wrapper headers that rely on the prototypes. Hence in application code it may be necessary to include ``vulkan.hpp`` or similar before any of the QVulkan headers.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QSurface.SurfaceType`, QVulkanFunctions.
