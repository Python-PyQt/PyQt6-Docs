.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 443047a833b8f624ac9999a2e0b22ba1

This function tries to release redundant resources currently held by the QML scene.

Calling this function requests the scene graph to release cached graphics resources, such as graphics pipeline objects or shader programs.

**Note:** The releasing of cached graphics resources is not dependent on the hint from :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setPersistentGraphics`.

Additionally, depending on the render loop in use, this function may also result in the scene graph and all rendering resources to be released. If this happens, the :sip:ref:`~PyQt6.QtQuick.QQuickWindow.sceneGraphInvalidated` signal will be emitted, allowing users to clean up their own graphics resources. The :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setPersistentGraphics` and :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setPersistentSceneGraph` functions can be used to prevent this from happening, if handling the cleanup is not feasible in the application, at the cost of higher memory usage.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.sceneGraphInvalidated`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setPersistentGraphics`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setPersistentSceneGraph`.
