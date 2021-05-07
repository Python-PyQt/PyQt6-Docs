.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 5c16753113b025e241613a05dfad7bdc

Initializes the scene graph resources. When using a graphics API, such as Vulkan, Metal, OpenGL, or Direct3D, for Qt Quick rendering, :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl` will set up an appropriate rendering engine when this function is called. This rendering infrastructure exists as long as the :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl` exists.

To control what graphics API Qt Quick uses, call :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setGraphicsApi` with one of the :sip:ref:`~PyQt6.QtQuick.QSGRendererInterface`:GraphicsApi constants. That must be done before calling this function.

To prevent the scenegraph from creating its own device and context objects, specify an appropriate :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsDevice`, wrapping existing graphics objects, by calling :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setGraphicsDevice`.

To configure which device extensions to enable (for example, for Vulkan), call :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setGraphicsConfiguration` before this function.

**Note:** When using Vulkan, :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl` does not create a QVulkanInstance automatically. Rather, it is the application's responsibility to create a suitable QVulkanInstance and associate it with the :sip:ref:`~PyQt6.QtQuick.QQuickWindow`. Before initializing the QVulkanInstance, it is strongly encouraged to query the list of Qt Quick's desired instance extensions by calling the static function :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration.preferredInstanceExtensions` and to pass the returned list to QVulkanInstance::setExtensions().

Returns ``true`` on success, ``false`` otherwise.

**Note:** This function does not need to be, and must not be, called when using the ``software`` adaptation of Qt Quick.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickRenderTarget`, :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsDevice`, :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration.preferredInstanceExtensions`.
