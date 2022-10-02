.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 4a916728f0e1daaad28ce6126bc69a95

Stop rendering and release resources.

This is the equivalent of the cleanup operations that happen with a real :sip:ref:`~PyQt6.QtQuick.QQuickWindow` when the window becomes hidden.

This function is called from the destructor. Therefore there will typically be no need to call it directly.

Once invalidate() has been called, it is possible to reuse the :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl` instance by calling :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.initialize` again.

**Note:** This function does not take QQuickWindow::persistentSceneGraph() or QQuickWindow::persistentGraphics() into account. This means that context-specific resources are always released.
