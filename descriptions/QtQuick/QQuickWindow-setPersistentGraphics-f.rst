.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: e79c80794b7d6adc2d072e51e7934210

Sets whether the graphics resources (graphics device or context, swapchain, buffers, textures) should be preserved, and cannot be released until the last window is deleted, to *persistent*. The default value is true.

When calling :sip:ref:`~PyQt6.QtQuick.QQuickWindow.releaseResources`, or when the window gets hidden (more specifically, not renderable), some render loops have the possibility to release all, not just the cached, graphics resources. This can free up memory temporarily, but it also means the rendering engine will have to do a full, potentially costly reinitialization of the resources when the window needs to render again.

**Note:** The rules for when a window is not renderable are platform and window manager specific.

**Note:** All graphics resources are released when the last :sip:ref:`~PyQt6.QtQuick.QQuickWindow` is deleted, regardless of this setting.

**Note:** This is a hint, and is not guaranteed that it is taken into account.

**Note:** This hint does not apply to cached resources, that are relatively cheap to drop and then recreate later. Therefore, calling :sip:ref:`~PyQt6.QtQuick.QQuickWindow.releaseResources` will typically lead to releasing those regardless of the value of this hint.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.isPersistentGraphics`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setPersistentSceneGraph`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.sceneGraphInitialized`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.sceneGraphInvalidated`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.releaseResources`.
