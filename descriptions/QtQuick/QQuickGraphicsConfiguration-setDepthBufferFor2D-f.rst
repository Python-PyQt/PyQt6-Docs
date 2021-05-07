.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: f1acd9757630e30b95eca96b966658c0

Sets the usage of depth buffer for 2D content to *enable*. When disabled, the Qt Quick scene graph never writes into the depth buffer.

By default the value is true, unless the ``QSG_NO_DEPTH_BUFFER`` environment variable is set.

The default value of true is the most optimal setting for the vast majority of scenes. Disabling depth buffer usage reduces the efficiency of the scene graph's batching.

There are cases however, when allowing the 2D content write to the depth buffer is not ideal. Consider a 3D scene as an "overlay" on top the 2D scene, rendered via Qt Quick 3D using a `View3D <https://doc.qt.io/qt-6/qml-qtquick3d-view3d.html>`_ with `renderMode <https://doc.qt.io/qt-6/qml-qtquick3d-view3d.html#renderMode-prop>`_ set to ``Overlay``. In this case, having the depth buffer filled by 2D content can cause unexpected results. This is because the way the 2D scene graph renderer generates and handles depth values is not necessarily compatible with how a 3D scene works. This may end up in depth value clashes, collisions, and unexpected depth test failures. Therefore, the robust approach here is to call this function with *enable* set to false, and disable depth buffer writes for the 2D content in the :sip:ref:`~PyQt6.QtQuick.QQuickWindow`.

**Note:** This flag is not fully identical to setting the ``QSG_NO_DEPTH_BUFFER`` environment variable. This flag does not control the depth-stencil buffers' presence. It is rather relevant for the rendering pipeline. To force not having depth/stencil attachments at all, set ``QSG_NO_DEPTH_BUFFER`` and ``QSG_NO_STENCIL_BUFFER``. Be aware however that such a :sip:ref:`~PyQt6.QtQuick.QQuickWindow`, and any Item layers in it, may then become incompatible with items, such as `View3D <https://doc.qt.io/qt-6/qml-qtquick3d-view3d.html>`_ with certain operating modes, because 3D content requires a depth buffer. Calling this function is always safe, but can mean that resources, such as depth buffers, are created even though they are not actively used.
