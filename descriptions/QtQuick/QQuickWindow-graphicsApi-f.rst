.. sip:method-description::
    :status: todo
    :pysig: 6aab5aa96e141296ce2145edf1228f05
    :realsig: ()
    :digest: b81a563247bfc45b6fce73cb7e12f164

Returns the graphics API that would be used by the scene graph if it was initialized at this point in time.

The standard way to query the API used by the scene graph is to use :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface.graphicsApi` once the scene graph has initialized, for example when or after the :sip:ref:`~PyQt6.QtQuick.QQuickWindow.sceneGraphInitialized` signal is emitted. In that case one gets the true, real result, because then it is known that everything was initialized correctly using that graphics API.

This is not always convenient. If the application needs to set up external frameworks, or needs to work with :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setGraphicsDevice` in a manner that depends on the scene graph's built in API selection logic, it is not always feasiable to defer such operations until after the :sip:ref:`~PyQt6.QtQuick.QQuickWindow` has been made visible or :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.initialize` has been called.

Therefore, this static function is provided as a counterpart to :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setGraphicsApi`: it can be called at any time, and the result reflects what API the scene graph would choose if it was initialized at the point of the call.

**Note:** This static function is intended to be called on the main (GUI) thread only. For querying the API when rendering, use :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface` since that object lives on the render thread.

**Note:** This function does not take scene graph backends into account.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setGraphicsApi`.
