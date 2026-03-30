.. sip:method-description::
    :status: todo
    :pysig: 4121a8b50e31c1aad4d296e24c14c2b2
    :realsig: (const QByteArrayList&)
    :digest: 3dd5e96d9674c93755e03e28c630c8d3

Sets the list of additional *extensions* to enable on the graphics device (such as, the ``VkDevice``).

When rendering with a graphics API where the concept is not applicable, *extensions* will be ignored.

**Note:** The list specifies additional, extra extensions. Qt Quick always enables extensions that are required by the scene graph.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration.deviceExtensions`.
