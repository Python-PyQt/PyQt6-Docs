.. sip:method-description::
    :status: todo
    :pysig: 60184add378f308c6e352e2af8c27883
    :realsig: (const QQuickGraphicsDevice&)
    :digest: 2b291552ddd4e68076c4a65ef3241c9b

Sets the graphics device objects for this window. The scenegraph will use existing device, physical device, and other objects specified by *device* instead of creating new ones.

This function is very often used in combination with :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl` and :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setRenderTarget`, in order to redirect Qt Quick rendering into a texture.

A default constructed :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsDevice` does not change the default behavior in any way. Once a *device* created via one of the :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsDevice` factory functions, such as, QQuickGraphicsDevice::fromDeviceObjects(), is passed in, and the scenegraph uses a matching graphics API (with the example of fromDeviceObjects(), that would be Vulkan), the scenegraph will use the existing device objects (such as, the ``VkPhysicalDevice``, ``VkDevice``, and graphics queue family index, in case of Vulkan) encapsulated by the :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsDevice`. This allows using the same device, and so sharing resources, such as buffers and textures, between Qt Quick and native rendering engines.

**Warning:** This function can only be called before initializing the scenegraph and will have no effect if called afterwards. In practice this typically means calling it right before :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.initialize`.

As an example, this time with Direct3D, the typical usage is expected to be the following:

::

    // native graphics resources set up by a custom D3D rendering engine
    ID3D11Device *device;
    ID3D11DeviceContext *context;
    ID3D11Texture2D *texture;
    ...
    // now to redirect Qt Quick content into 'texture' we could do the following:
    QQuickRenderControl *renderControl = new QQuickRenderControl;
    QQuickWindow *window = new QQuickWindow(renderControl); // this window will never be shown on-screen
    ...
    window->setGraphicsDevice(QQuickGraphicsDevice::fromDeviceAndContext(device, context));
    renderControl->initialize();
    window->setRenderTarget(QQuickRenderTarget::fromD3D11Texture(texture, textureSize);
    ...

The key aspect of using this function is to ensure that resources or handles to resources, such as ``texture`` in the above example, are visible to and usable by both the external rendering engine and the scenegraph renderer. This requires using the same graphics device (or with OpenGL, OpenGL context).

:sip:ref:`~PyQt6.QtQuick.QQuickGraphicsDevice` instances are implicitly shared, copyable, and can be passed by value. They do not own the associated native objects (such as, the ID3D11Device in the example).

**Note:** Using :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl` does not always imply having to call this function. When adopting an existing device or context is not needed, this function should not be called, and the scene graph will then initialize its own devices and contexts normally, just as it would with an on-screen :sip:ref:`~PyQt6.QtQuick.QQuickWindow`.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.graphicsDevice`, :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setRenderTarget`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setGraphicsApi`.
