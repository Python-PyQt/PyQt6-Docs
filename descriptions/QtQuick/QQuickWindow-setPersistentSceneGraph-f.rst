.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 2d8f126d5778c60e2ee2f29cbc27199b

Sets whether the scene graph nodes and resources are *persistent*. Persistent means the nodes and resources cannot be released. The default value is ``true``.

When calling :sip:ref:`~PyQt6.QtQuick.QQuickWindow.releaseResources`, when the window gets hidden (more specifically, not renderable), some render loops have the possibility to release the scene graph nodes and related graphics resources. This frees up memory temporarily, but will also mean the scene graph has to be rebuilt when the window renders next time.

**Note:** The rules for when a window is not renderable are platform and window manager specific.

**Note:** The scene graph nodes and resources are always released when the last :sip:ref:`~PyQt6.QtQuick.QQuickWindow` is deleted, regardless of this setting.

**Note:** This is a hint, and is not guaranteed that it is taken into account.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.isPersistentSceneGraph`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setPersistentGraphics`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.sceneGraphInvalidated`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.sceneGraphInitialized`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.releaseResources`.
