.. sip:method-description::
    :status: todo
    :pysig: 8851e0acc2178e167ff6e8b5fa63298c
    :realsig: (const QByteArrayList&)
    :digest: 3dd5e96d9674c93755e03e28c630c8d3

Sets the list of additional *extensions* to enable on the graphics device (such as, the ``VkDevice``).

When rendering with a graphics API where the concept is not applicable, *extensions* will be ignored.

**Note:** The list specifies additional, extra extensions. Qt Quick always enables extensions that are required by the scene graph.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickGraphicsConfiguration.deviceExtensions`.
