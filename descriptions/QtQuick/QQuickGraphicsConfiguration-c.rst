.. sip:class-description::
    :status: todo
    :brief: Controls lower level graphics settings for the QQuickWindow
    :digest: 93e0fe3158c59ce4fca9cafcd30d757a

:sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration` controls lower level graphics settings for the :sip:ref:`~PyQt6.QtQuick.QQuickWindow`.

The :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration` class is a container for low-level graphics settings that can affect how the underlying graphics API, such as Vulkan, is initialized by the Qt Quick scene graph. It can also control certain aspects of the scene graph renderer.

**Note:** Setting a :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration` on a :sip:ref:`~PyQt6.QtQuick.QQuickWindow` must happen early enough, before the scene graph is initialized for the first time for that window. With on-screen windows this means the call must be done before invoking show() on the :sip:ref:`~PyQt6.QtQuick.QQuickWindow` or :sip:ref:`~PyQt6.QtQuick.QQuickView`. With :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl` the configuration must be finalized before calling :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.initialize`.

.. _qquickgraphicsconfiguration-configuration-for-external-rendering-engines-or-xr-apis:

Configuration for External Rendering Engines or XR APIs
-------------------------------------------------------

When constructing and showing a :sip:ref:`~PyQt6.QtQuick.QQuickWindow` that uses Vulkan to render, a Vulkan instance (``VkInstance``), a physical device (``VkPhysicalDevice``), a device (``VkDevice``) and associated objects (queues, pools) are initialized through the Vulkan API. The same is mostly true when using :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl` to redirect the rendering into a custom render target, such as a texture. While QVulkanInstance construction is under the application's control then, the initialization of other graphics objects happen the same way in :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.initialize` as with an on-screen :sip:ref:`~PyQt6.QtQuick.QQuickWindow`.

For the majority of applications no additional configuration is needed because Qt Quick provides reasonable defaults for many low-level graphics settings, for example which device extensions to enable.

This will not alway be sufficient, however. In advanced use cases, when integrating direct Vulkan or other graphics API content, or when integrating with an external 3D or VR engine, such as, OpenXR, the application will want to specify its own set of settings when it comes to details, such as which device extensions to enable.

That is what this class enables. It allows specifying, for example, a list of device extensions that is then picked up by the scene graph when using Vulkan, or graphics APIs where the concept is applicable. Where some concepts are not applicable, the related settings are simply ignored.

Examples of functions in this category are :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration.preferredInstanceExtensions` and :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration.setDeviceExtensions`.

.. _qquickgraphicsconfiguration-qt-quick-scene-graph-renderer-configuration:

Qt Quick Scene Graph Renderer Configuration
-------------------------------------------

Another class of settings are related to the scene graph's renderer. In some cases applications may want to control certain behavior,such as using the depth buffer when rendering 2D content. In Qt 5 such settings were either not controllable at all, or were managed through environment variables. In Qt 6, :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration` provides a new home for these settings, while keeping support for the legacy environment variables, where applicable.

An example in this category is :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration.setDepthBufferFor2D`.

.. _qquickgraphicsconfiguration-graphics-device-configuration:

Graphics Device Configuration
-----------------------------

When the graphics instance and device objects (for example, the VkInstance and VkDevice with Vulkan, the ID3D11Device with Direct 3D, etc.) are created by Qt when initializing a :sip:ref:`~PyQt6.QtQuick.QQuickWindow`, there are settings which applications or libraries will want to control under certain circumstances.

Before Qt 6.5, some of such settings were available to control via environment variables. For example, ``QSG_RHI_DEBUG_LAYER`` or ``QSG_RHI_PREFER_SOFTWARE_RENDERER``. These are still available and continue to function as before. :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration` provides C++ setters in addition.

For example, the following main() function opens a :sip:ref:`~PyQt6.QtQuick.QQuickView` while specifying that the Vulkan validation or Direct3D debug layer should be enabled:

::

    int main(int argc, char *argv[])
    {
        QGuiApplication app(argc, argv);

        QQuickGraphicsConfiguration config;
        config.setDebugLayer(true);

        QQuickView *view = new QQuickView;
        view->setGraphicsConfiguration(config);

        view->setSource(QUrl::fromLocalFile("myqmlfile.qml"));
        view->show();
        return app.exec();
    }

.. _qquickgraphicsconfiguration-pipeline-cache-save-and-load:

Pipeline Cache Save and Load
----------------------------

Qt Quick supports storing the graphics/compute pipeline cache to disk, and reloading it in subsequent runs of an application. What exactly the pipeline cache contains, how lookups work, and what exactly gets accelerated all depend on the Qt RHI backend and the underlying native graphics API that is used at run time. Different 3D APIs have different concepts when it comes to shaders, programs, and pipeline state objects, and corresponding cache mechanisms. The high level pipeline cache concept here abstracts all this to storing and retrieving a single binary blob to and from a file.

**Note:** Storing the cache on disk can lead to improvements, sometimes significant, in subsequent runs of the application.

When the same shader program and/or pipeline state is encountered as in a previous run, a number of operations are likely skipped, leading to faster shader and material initialization times, which means startup may become faster and lags and "janks" during rendering may be reduced or avoided.

When running with a graphics API where retrieving and reloading the pipeline cache (or shader/program binaries) is not applicable or not supported, attempting to use a file to save and load the cache has no effect.

**Note:** In many cases the retrieved data is dependent on and tied to the graphics driver (and possibly the exact version of it). Qt performs the necessary checks automatically, by storing additional metadata in the pipeline cache file. If the data in the file does not match the graphics device and driver version at run time, the contents will be ignored transparently to the application. It is therefore safe to reference a cache that was generated on another device or driver.

There are exceptions to the driver dependency problem, most notably Direct 3D 11, where the "pipeline cache" is used only to store the results of runtime HLSL->DXBC compilation and is therefore device and vendor independent.

In some cases it may be desirable to improve the very first run of the application, by "pre-seeding" the cache. This is possible by shipping the cache file saved from a previous run, and referencing it on another machine or device. This way, the application or device has the shader programs/pipelines that have been encountered before in the run that saved the cache file available already during its first run. Shipping and deploying the cache file only makes sense if the device and graphics drivers are the same on the target system, otherwise the cache file is ignored if the device or driver version does not match (with the exception of D3D11), as described above.

Once the cache contents is loaded, there is still a chance that the application builds graphics and compute pipelines that have not been encountered in previous runs. In this cases the cache is grown, with the pipelines / shader programs added to it. If the application also chooses to save the contents (perhaps to the same file even), then both the old and new pipelines will get stored. Loading from and saving to the same file in every run allows an ever growing cache that stores all encountered pipelines and shader programs.

In practice the Qt pipeline cache can be expected to map to the following native graphics API features:

* Vulkan - `VkPipelineCache <https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VkPipelineCache.html>`_ - Saving the pipeline cache effectively stores the blob retrieved from `vkGetPipelineCacheData <https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/vkGetPipelineCacheData.html>`_, with additional metadata to safely identify the device and the driver since the pipeline cache blob is dependent on the exact driver.

* Metal - `MTLBinaryArchive <https://developer.apple.com/documentation/metal/mtlbinaryarchive?language=objc>`_ - With pipeline cache saving enabled, Qt stores all render and compute pipelines encountered into an MTLBinaryArchive. Saving the pipeline cache stores the blob retrieved from the archive, with additional metadata to identify the device. **Note:** currently MTLBinaryArchive usage is disabled on macOS and iOS due to various issues on some hardware and OS versions.

* OpenGL - There is no native concept of pipelines, the "pipeline cache" stores a collection of program binaries retrieved via `glGetProgramBinary <https://registry.khronos.org/OpenGL-Refpages/gl4/html/glGetProgramBinary.xhtml>`_. The program binaries are packaged into a single blob, with additional metadata to identify the device, driver, and its version that the binaries were retrieved from. Persistent caching of program binaries is not new in Qt: Qt 5 already had similar functionality in :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram`, see :sip:ref:`~PyQt6.QtOpenGL.QOpenGLShaderProgram.addCacheableShaderFromSourceCode` for example. In fact that mechanism is always active in Qt 6 as well when using Qt Quick with OpenGL. However, when using the new, graphics API independent pipeline cache abstraction provided here, the Qt 5 era program binary cache gets automatically disabled, since the same content is packaged in the "pipeline cache" now.

* Direct 3D 11 - There is no native concept of pipelines or retrieving binaries for the second phase compilation (where the vendor independent, intermediate bytecode is compiled into the device specific instruction set). Drivers will typically employ their own caching system on that level. Instead, the Qt Quick "pipeline cache" is used to speed up cases where the shaders contain HLSL source code that needs to be compiled into the intermediate bytecode format first. This can present significant performance improvements in application and libraries that compose shader code at run time, because in subsequent runs the potentially expensive, uncached calls to `D3DCompile() <https://docs.microsoft.com/en-us/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dcompile>`_ can be avoided if the bytecode is already available for the encountered HLSL shader. A good example is Qt Quick 3D, where the runtime-generated shaders for materials imply having to deal with HLSL source code. Saving and reloading the Qt Quick pipeline cache can therefore bring considerable improvements in scenes with one or more `View3D <https://doc.qt.io/qt-6/qml-qtquick3d-view3d.html>`_ items in them. A counterexample may be Qt Quick itself: as most built-in shaders for 2D content ship with DirectX bytecode generated at build time, the cache is not going to present any significant improvements.

All this is independent from the shader processing performed by the Qt Shader Tools module and its command-line tools such as ``qsb``. As an example, take Vulkan. Having the Vulkan-compatible GLSL source code compiled to SPIR-V either at offline or build time (directly via qsb or CMake) is good, because the expensive compilation from source form is avoided at run time. SPIR-V is however a vendor-independent intermediate format. At runtime, when constructing graphics or compute pipelines, there is likely another round of compilation happening, this time from the intermediate format to the vendor-specific instruction set of the GPU (and this may be dependent on certain state in the graphics pipeline and the render targets as well). The pipeline cache helps with this latter phase.

**Note:** Many graphics API implementation employ their own persistent disk cache transparently to the applications. Using the pipeline cache feature of Qt Quick will likely provide improvements in this case, but the gains might be smaller.

Call :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration.setPipelineCacheSaveFile` and :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration.setPipelineCacheLoadFile` to control which files a :sip:ref:`~PyQt6.QtQuick.QQuickWindow` or :sip:ref:`~PyQt6.QtQuick.QQuickView` saves and loads the pipeline cache to/from.

To get an idea of the effects of enabling disk storage of the pipeline cache, enable the most important scenegraph and graphics logs either via the environment variable ``QSG_INFO=1``, or both the ``qt.scenegraph.general`` and ``qt.rhi.general`` logging categories. When closing the :sip:ref:`~PyQt6.QtQuick.QQuickWindow`, there is log message like the following:

::

    Total time spent on pipeline creation during the lifetime of the QRhi was 123 ms

This gives an approximate idea of how much time was spent in graphics and compute pipeline creation (which may include various stages of shader compilation) during the lifetime of the window.

When loading from a pipeline cache file is enabled, this is confirmed with a message:

::

    Attempting to seed pipeline cache from 'filename'

Similarly, to check if saving of the cache is successfully enabled, look for a message such as this:

::

    Writing pipeline cache contents to 'filename'

.. _qquickgraphicsconfiguration-the-automatic-pipeline-cache:

The Automatic Pipeline Cache
----------------------------

When no filename is provided for save and load, the automatic pipeline caching strategy is used. This involves storing data to the application-specific cache location of the system (\ :sip:ref:`~PyQt6.QtCore.QStandardPaths.StandardLocation.CacheLocation`).

This can be disabled by one of the following means:

* Set the application attribute :sip:ref:`~PyQt6.QtCore.Qt.ApplicationAttribute.AA_DisableShaderDiskCache`. (completely disables the automatic storage)

* Set the environment variable QT_DISABLE_SHADER_DISK_CACHE to a non-zero value. (completely disables the automatic storage)

* Set the environment variable QSG_RHI_DISABLE_SHADER_DISK_CACHE to a non-zero value. (completely disables the automatic storage)

* Call setAutomaticPiplineCache() with the enable argument set to false. (completely disables the automatic storage)

* Set a filename by calling :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration.setPipelineCacheLoadFile`. (only disables loading from the automatic storage, prefering the specified file instead)

* Set a filename by calling :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration.setPipelineCacheSaveFile`. (only disables writing to the automatic storage, prefering the specified file instead)

The first two are existing mechanisms that are used since Qt 5.9 to control the OpenGL program binary cache. For compatibility and familiarity the same attribute and environment variable are supported for Qt 6's enhanced pipeline cache.

The automatic pipeline cache uses a single file per application, but a different one for each RHI backend (graphics API). This means that changing to another graphics API in the next run of the application will not lead to losing the pipeline cache generated in the previous run. Applications with multiple :sip:ref:`~PyQt6.QtQuick.QQuickWindow` instances shown simultaneously may however not benefit 100% since the automatic cache can only store the data collected from one RHI object at a time. (and with the default ``threaded`` render loop each window has its own RHI as rendering operates independently on dedicated threads). To fully benefit from the disk cache in application with multiple windows, prefer setting the filename explicitly, per-window via :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration.setPipelineCacheSaveFile`.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setGraphicsConfiguration`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow`, :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl`.
