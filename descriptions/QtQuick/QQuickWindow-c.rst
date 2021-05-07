.. sip:class-description::
    :status: todo
    :brief: The window for displaying a graphical QML scene
    :digest: 261021f257c5329548b0e250f8ea6539

The :sip:ref:`~PyQt6.QtQuick.QQuickWindow` class provides the window for displaying a graphical QML scene.

:sip:ref:`~PyQt6.QtQuick.QQuickWindow` provides the graphical scene management needed to interact with and display a scene of QQuickItems.

A :sip:ref:`~PyQt6.QtQuick.QQuickWindow` always has a single invisible root item. To add items to this window, reparent the items to the root item or to an existing item in the scene.

For easily displaying a scene from a QML file, see :sip:ref:`~PyQt6.QtQuick.QQuickView`.

.. _qquickwindow-rendering:

Rendering
---------

:sip:ref:`~PyQt6.QtQuick.QQuickWindow` uses a scene graph to represent what needs to be rendered. This scene graph is disconnected from the QML scene and potentially lives in another thread, depending on the platform implementation. Since the rendering scene graph lives independently from the QML scene, it can also be completely released without affecting the state of the QML scene.

The :sip:ref:`~PyQt6.QtQuick.QQuickWindow.sceneGraphInitialized` signal is emitted on the rendering thread before the QML scene is rendered to the screen for the first time. If the rendering scene graph has been released, the signal will be emitted again before the next frame is rendered. A visible, on-screen :sip:ref:`~PyQt6.QtQuick.QQuickWindow` is driven internally by a ``render loop``, of which there are multiple implementations provided in the scene graph. For details on the scene graph rendering process, see `Qt Quick Scene Graph <https://doc.qt.io/qt-6/qtquick-visualcanvas-scenegraph.html>`_.

By default, a :sip:ref:`~PyQt6.QtQuick.QQuickWindow` renders using an accelerated 3D graphics API, such as OpenGL or Vulkan. See `Scene Graph Adaptations <https://doc.qt.io/qt-6/qtquick-visualcanvas-adaptations.html>`_ for a detailed overview of scene graph backends and the supported graphics APIs.

**Warning:** It is crucial that graphics operations and interaction with the scene graph happens exclusively on the rendering thread, primarily during the updatePaintNode() phase.

**Warning:** As many of the signals related to rendering are emitted from the rendering thread, connections should be made using :sip:ref:`~PyQt6.QtCore.Qt.ConnectionType.DirectConnection`.

.. _qquickwindow-integration-with-accelerated-3d-graphics-apis:

Integration with Accelerated 3D Graphics APIs
.............................................

It is possible to integrate OpenGL, Vulkan, Metal, or Direct3D 11 calls directly into the :sip:ref:`~PyQt6.QtQuick.QQuickWindow`, as long as the :sip:ref:`~PyQt6.QtQuick.QQuickWindow` and the underlying scene graph is rendering using the same API. To access native graphics objects, such as device or context object handles, use :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface`. An instance of :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface` is queriable from :sip:ref:`~PyQt6.QtQuick.QQuickWindow` by calling :sip:ref:`~PyQt6.QtQuick.QQuickWindow.rendererInterface`. The enablers for this integration are the :sip:ref:`~PyQt6.QtQuick.QQuickWindow.beforeRendering`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.beforeRenderPassRecording`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.afterRenderPassRecording`, and related signals. These allow rendering underlays or overlays. Alternatively, :sip:ref:`~PyQt6.QtQuick.QNativeInterface.QSGOpenGLTexture`, QNativeInterface::QSGVulkanTexture, and other similar classes allow wrapping an existing native texture or image object in a :sip:ref:`~PyQt6.QtQuick.QSGTexture` that can then be used with the scene graph.

.. _qquickwindow-rendering-without-acceleration:

Rendering without Acceleration
..............................

A limited, pure software based rendering path is available as well. With the ``software`` backend, a number of Qt Quick features are not available, QML items relying on these will not be rendered at all. At the same time, this allows :sip:ref:`~PyQt6.QtQuick.QQuickWindow` to be functional even on systems where there is no 3D graphics API available at all. See `Qt Quick Software Adaptation <https://doc.qt.io/qt-6/qtquick-visualcanvas-adaptations-software.html>`_ for more details.

.. _qquickwindow-redirected-rendering:

Redirected Rendering
....................

A :sip:ref:`~PyQt6.QtQuick.QQuickWindow` is not necessarily backed by a native window on screen. The rendering can be redirected to target a custom render target, such as a given native texture. This is achieved in combination with the :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl` class, and functions such as :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setRenderTarget`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setGraphicsDevice`, and :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setGraphicsConfiguration`.

In this case, the :sip:ref:`~PyQt6.QtQuick.QQuickWindow` represents the scene, and provides the intrastructure for rendering a frame. It will not be backed by a render loop and a native window. Instead, in this case the application drives rendering, effectively substituting for the render loops. This allows generating image sequences, rendering into textures for use in external 3D engines, or rendering Qt Quick content within a VR environment.

.. _qquickwindow-resource-management:

Resource Management
...................

QML will try to cache images and scene graph nodes to improve performance, but in some low-memory scenarios it might be required to aggressively release these resources. The :sip:ref:`~PyQt6.QtQuick.QQuickWindow.releaseResources` function can be used to force the clean up of certain resources, especially resource that are cached and can be recreated later when needed again.

Additionally, calling :sip:ref:`~PyQt6.QtQuick.QQuickWindow.releaseResources` may result in releasing the entire scene graph and the associated graphics resources. The :sip:ref:`~PyQt6.QtQuick.QQuickWindow.sceneGraphInvalidated` signal will be emitted when this happens. This behavior is controlled by the :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setPersistentGraphics` and :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setPersistentSceneGraph` functions.

**Note:** All classes with QSG prefix should be used solely on the scene graph's rendering thread. See `Scene Graph and Rendering <https://doc.qt.io/qt-6/qtquick-visualcanvas-scenegraph.html#scene-graph-and-rendering>`_ for more information.

.. _qquickwindow-exposure-and-visibility:

Exposure and Visibility
.......................

When a :sip:ref:`~PyQt6.QtQuick.QQuickWindow` instance is deliberately hidden with hide() or setVisible(false), it will stop rendering and its scene graph and graphics context might be released as well. This depends on the settings configured by :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setPersistentGraphics` and :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setPersistentSceneGraph`. The behavior in this respect is identical to explicitly calling the :sip:ref:`~PyQt6.QtQuick.QQuickWindow.releaseResources` function. A window can become not exposed, in other words non-renderable, by other means as well. This depends on the platform and windowing system. For example, on Windows minimizing a window makes it stop rendering. On macOS fully obscuring a window by other windows on top triggers the same. On Linux/X11, the behavior is dependent on the window manager.

.. _qquickwindow-opengl-context-and-surface-formats:

OpenGL Context and Surface Formats
..................................

While it is possible to specify a :sip:ref:`~PyQt6.QtGui.QSurfaceFormat` for every :sip:ref:`~PyQt6.QtQuick.QQuickWindow` by calling the member function setFormat(), windows may also be created from QML by using the Window and ApplicationWindow elements. In this case there is no C++ code involved in the creation of the window instance, yet applications may still wish to set certain surface format values, for example to request a given OpenGL version or profile. Such applications can call the static function :sip:ref:`~PyQt6.QtGui.QSurfaceFormat.setDefaultFormat` at startup. The specified format will be used for all Quick windows created afterwards.

.. _qquickwindow-vulkan-instance:

Vulkan Instance
...............

When using Vulkan, a :sip:ref:`~PyQt6.QtQuick.QQuickWindow` is automatically associated with a QVulkanInstance that is created and managed internally by the scene graph. This way most applications do not need to worry about having a ``VkInstance`` available since it all happens automatically. In advanced cases an application may wish to create its own QVulkanInstance, in order to configure it in a specific way. That is possible as well. Calling setVulkanInstance() on the :sip:ref:`~PyQt6.QtQuick.QQuickWindow` right after construction, before making it visible, leads to using the application-supplied QVulkanInstance (and the underlying ``VkInstance``). When redirecting via :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl`, there is no QVulkanInstance provided automatically, but rather the application is expected to provide its own and associate it with the :sip:ref:`~PyQt6.QtQuick.QQuickWindow`.

.. _qquickwindow-graphics-contexts-and-devices:

Graphics Contexts and Devices
.............................

When the scene graph is initialized, which typically happens when the window becomes exposed or, in case of redirected rendering, initialization is performed :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.initialize`, the context or device objects necessary for rendering are created automatically. This includes OpenGL contexts, Direct3D devices and device contexts, Vulkan and Metal devices. These are also queriable by application code afterwards via :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface.getResource`. When using the ``basic`` render loop, which performs all rendering on the GUI thread, the same context or device is used with all visible QQuickWindows. The ``threaded`` render loop uses a dedicated context or device object for each rendering thread, and so for each :sip:ref:`~PyQt6.QtQuick.QQuickWindow`. With some graphics APIs, there is a degree of customizability provided via :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setGraphicsConfiguration`. This makes it possible, for example, to specify the list of Vulkan extensions to enable on the ``VkDevice``. Alternatively, it is also possible to provide a set of existing context or device objects for use by the :sip:ref:`~PyQt6.QtQuick.QQuickWindow`, instead of letting it construct its own. This is achieved through :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setGraphicsDevice`.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickView`, :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl`, :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget`, :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsDevice`, :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration`, :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface`.
