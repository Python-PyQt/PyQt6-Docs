.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 7b9748dec54dbaf9e0b6e8367b57242c

When enabled, GPU timing data is collected from command buffers on platforms and 3D APIs where this is supported. This data is then printed in the renderer logs that can be enabled via ``QSG_RENDER_TIMING`` environment variable or logging categories such as ``qt.scenegraph.time.renderloop``, and may also be made visible to other modules, such as Qt Quick 3D's `DebugView <https://doc.qt.io/qt-6/qml-qtquick3d-helpers-debugview.html>`_ item.

By default this is disabled, because collecting the data may involve additional work, such as inserting timestamp queries in the command stream, depending on the underlying graphics API. To enable, either call this function with *enable* set to true, or set the ``QSG_RHI_PROFILE`` environment variable to a non-zero value.

Graphics APIs where this can be expected to be supported are Direct 3D 11, Direct 3D 12, Vulkan (as long as the underlying Vulkan implementation supports timestamp queries), Metal, and OpenGL with a core or compatibility profile context for version 3.3 or newer. Timestamps are not supported with OpenGL ES.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration.timestampsEnabled`, :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration.setDebugMarkers`.
