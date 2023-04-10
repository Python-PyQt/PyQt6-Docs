.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 8e0237e8d307a89141bdc9412d56590e

This function tries to release redundant resources currently held by the QML scene.

Calling this function requests the scene graph to release cached graphics resources, such as graphics pipeline objects, shader programs, or image data.

Additionally, depending on the render loop in use, this function may also result in the scene graph and all window-related rendering resources to be released. If this happens, the :sip:ref:`~PyQt6.QtQuick.QQuickWindow.sceneGraphInvalidated` signal will be emitted, allowing users to clean up their own graphics resources. The :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setPersistentGraphics` and :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setPersistentSceneGraph` functions can be used to prevent this from happening, if handling the cleanup is not feasible in the application, at the cost of higher memory usage.

**Note:** The releasing of cached graphics resources, such as graphics pipelines or shader programs is not dependent on the persistency hints. The releasing of those will happen regardless of the values of the persistent graphics and scenegraph hints.

**Note:** This function is not related to the :sip:ref:`~PyQt6.QtQuick.QQuickItem.releaseResources` virtual function.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.sceneGraphInvalidated`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setPersistentGraphics`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setPersistentSceneGraph`.
