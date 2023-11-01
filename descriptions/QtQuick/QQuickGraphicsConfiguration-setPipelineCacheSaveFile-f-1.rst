.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: eaf98a6b6265ef6b4ba1d9f40107738f

Sets the *filename* where the :sip:ref:`~PyQt6.QtQuick.QQuickWindow` is expected to store its graphics/compute pipeline cache contents. The default value is empty, which means pipeline cache loading is disabled.

See :ref:`qquickgraphicsconfiguration-pipeline-cache-save-and-load` for a discussion on pipeline caches.

Persistently storing the pipeline cache can lead to performance improvements in future runs of the application since expensive shader compilation and pipeline construction steps may be avoided.

If and when the writing of the file happens is not defined. It will likely happen at some point when tearing down the scenegraph due to closing the window. Therefore, applications should not assume availability of the file until the :sip:ref:`~PyQt6.QtQuick.QQuickWindow` is fully destructed. :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration` only stores the filename, it does not perform any actual I/O and graphics operations on its own.

When running with a graphics API where retrieving the pipeline cache (or shader/program binaries) is not applicable or not supported, calling this function has no effect.

Calling this function is mostly equivalent to setting the environment variable ``QSG_RHI_PIPELINE_CACHE_SAVE`` to *filename*, with one important difference: this function controls the pipeline cache storage for the associated :sip:ref:`~PyQt6.QtQuick.QQuickWindow` only. Applications with multiple :sip:ref:`~PyQt6.QtQuick.QQuickWindow` or :sip:ref:`~PyQt6.QtQuick.QQuickView` instances can therefore store and later reload the cache contents via files dedicated to each window. The environment variable does not allow this.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration.pipelineCacheSaveFile`, :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration.pipelineCacheLoadFile`.
