.. sip:method-description::
    :status: todo
    :pysig: 6aab5aa96e141296ce2145edf1228f05
    :realsig: (QSGRendererInterface::GraphicsApi)
    :digest: 0ec3f0057791e3f624c861005ed6639e

Requests the specified graphics *api*.

When the built-in, default graphics adaptation is used, *api* specifies which graphics API (OpenGL, Vulkan, Metal, or Direct3D) the scene graph should use to render. In addition, the ``software`` backend is built-in as well, and can be requested by setting *api* to :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface.GraphicsApi.Software`.

Unlike :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setSceneGraphBackend`, which can only be used to request a given backend (shipped either built-in or installed as dynamically loaded plugins), this function works with the higher level concept of graphics APIs. It covers the backends that ship with Qt Quick, and thus have corresponding values in the :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface.GraphicsApi` enum.

When this function is not called at all, and the equivalent environment variable ``QSG_RHI_BACKEND`` is not set either, the scene graph will choose the graphics API to use based on the platform.

This function becomes important in applications that are only prepared for rendering with a given API. For example, if there is native OpenGL or Vulkan rendering done by the application, it will want to ensure Qt Quick is rendering using OpenGL or Vulkan too. Such applications are expected to call this function early in their main() function.

**Note:** The call to the function must happen before constructing the first :sip:ref:`~PyQt6.QtQuick.QQuickWindow` in the application. The graphics API cannot be changed afterwards.

**Note:** When used in combination with :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl`, this rule is relaxed: it is possible to change the graphics API, but only when all existing :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl` and :sip:ref:`~PyQt6.QtQuick.QQuickWindow` instances have been destroyed.

To query what graphics API the scene graph is using to render, :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface.graphicsApi` after the scene graph :sip:ref:`~PyQt6.QtQuick.QQuickWindow.isSceneGraphInitialized`, which typically happens either when the window becomes visible for the first time, or when :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.initialize` is called.

To switch back to the default behavior, where the scene graph chooses a graphics API based on the platform and other conditions, set *api* to :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface.GraphicsApi.Unknown`.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.graphicsApi`.
