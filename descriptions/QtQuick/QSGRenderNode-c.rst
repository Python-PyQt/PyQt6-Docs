.. sip:class-description::
    :status: todo
    :brief: Represents a set of custom rendering commands targeting the graphics API that is in use by the scenegraph
    :digest: 52e3c0e922f63ee5e9d266270e444c9b

The :sip:ref:`~PyQt6.QtQuick.QSGRenderNode` class represents a set of custom rendering commands targeting the graphics API that is in use by the scenegraph.

:sip:ref:`~PyQt6.QtQuick.QSGRenderNode` allows creating scene graph nodes that perform their own custom rendering via QRhi (the common approach from Qt 6.6 on), directly via a 3D graphics API such as OpenGL, Vulkan, or Metal, or, when the ``software`` backend is in use, via :sip:ref:`~PyQt6.QtGui.QPainter`.

:sip:ref:`~PyQt6.QtQuick.QSGRenderNode` is the enabler for one of the three ways to integrate custom 2D/3D rendering into a Qt Quick scene. The other two options are to perform the rendering ``before`` or ``after`` the Qt Quick scene's own rendering, or to generate a whole separate render pass targeting a dedicated render target (a texture) and then have an item in the scene display the texture. The :sip:ref:`~PyQt6.QtQuick.QSGRenderNode`-based approach is similar to the former, in the sense that no additional render passes or render targets are involved, and allows injecting custom rendering commands "inline" with the Qt Quick scene's own rendering. See `Qt Quick Scene Graph <https://doc.qt.io/qt-6/qtquick-visualcanvas-scenegraph.html>`_ for a further discussion of the three approaches.

.. seealso:: `Scene Graph - Custom QSGRenderNode <https://doc.qt.io/qt-6/qtquick-scenegraph-customrendernode-example.html>`_.
