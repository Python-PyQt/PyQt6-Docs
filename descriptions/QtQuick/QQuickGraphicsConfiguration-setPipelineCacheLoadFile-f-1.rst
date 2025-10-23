.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 9f383f8ad6598ebcf94b2d79fa6340f4

Sets the *filename* where the :sip:ref:`~PyQt6.QtQuick.QQuickWindow` is expected to load the initial contents of its graphics/compute pipeline cache from. The default value is empty, which means pipeline cache loading is disabled.

See :ref:`qquickgraphicsconfiguration-pipeline-cache-save-and-load` for a discussion on pipeline caches.

Persistently storing the pipeline cache can lead to performance improvements in future runs of the application since expensive shader compilation and pipeline construction steps may be avoided.

If and when the loading of the file's contents happens is not defined, apart from that it will happen at some point during the initialization of the scenegraph of the :sip:ref:`~PyQt6.QtQuick.QQuickWindow`. Therefore, the file must continue to exist after calling this function. :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration` only stores the filename, it cannot perform any actual I/O and graphics operations on its own. The real work is going to happen later on, possibly on another thread.

When running with a graphics API where retrieving and reloading the pipeline cache (or shader/program binaries) is not applicable or not supported, calling this function has no effect.

Calling this function is mostly equivalent to setting the environment variable ``QSG_RHI_PIPELINE_CACHE_LOAD`` to *filename*, with one important difference: this function controls the pipeline cache storage for the associated :sip:ref:`~PyQt6.QtQuick.QQuickWindow` only. Applications with multiple :sip:ref:`~PyQt6.QtQuick.QQuickWindow` or :sip:ref:`~PyQt6.QtQuick.QQuickView` instances can therefore store and later reload the cache contents via files dedicated to each window. The environment variable does not allow this.

**Note:** If the data in the file does not match the graphics device and driver version at run time, the contents will be ignored, transparently to the application. This applies to a number of graphics APIs, and the necessary checks are taken care of by Qt. There are exceptions, most notably Direct 3D 11, where the "pipeline cache" is used only to store the results of runtime HLSL->DXBC compilation and is therefore device and vendor independent.

**Warning:** The serialized pipeline cache data is assumed to be trusted content. Application developers are advised to never pass in data from untrusted sources.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration.pipelineCacheLoadFile`, :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration.setPipelineCacheSaveFile`.
