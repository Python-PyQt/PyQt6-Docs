.. sip:method-description::
    :status: todo
    :pysig: 050da550b66b6d55dbf02562bea57ba6
    :realsig: () const
    :digest: eed40a683280ad5716c20cad3760c6c0

Returns the current renderer interface. The value is always valid and is never null.

**Note:** This function can be called at any time after constructing the :sip:ref:`~PyQt6.QtQuick.QQuickWindow`, even while :sip:ref:`~PyQt6.QtQuick.QQuickWindow.isSceneGraphInitialized` is still false. However, some renderer interface functions, in particular :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface.getResource` will not be functional until the scenegraph is up and running. Backend queries, like :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface.graphicsApi` or :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface.shaderType`, will always be functional on the other hand.

**Note:** The ownership of the returned pointer stays with Qt. The returned instance may or may not be shared between different :sip:ref:`~PyQt6.QtQuick.QQuickWindow` instances, depending on the scenegraph backend in use. Therefore applications are expected to query the interface object for each :sip:ref:`~PyQt6.QtQuick.QQuickWindow` instead of reusing the already queried pointer.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGRenderNode`, :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface`.
