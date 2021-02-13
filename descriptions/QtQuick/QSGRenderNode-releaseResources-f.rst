.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: b37b1db5ac9a847aa48958ff7c82f013

This function is called when all custom graphics resources allocated by this node have to be freed immediately. In case the node does not directly allocate graphics resources (buffers, textures, render targets, fences, etc.) through the graphics API that is in use, there is nothing to do here.

Failing to release all custom resources can lead to incorrect behavior in graphics device loss scenarios on some systems since subsequent reinitialization of the graphics system may fail.

**Note:** Some scenegraph backends may choose not to call this function. Therefore it is expected that :sip:ref:`~PyQt6.QtQuick.QSGRenderNode` implementations perform cleanup both in their destructor and in .

Unlike with the destructor, it is expected that :sip:ref:`~PyQt6.QtQuick.QSGRenderNode.render` can reinitialize all resources it needs when called after a call to .

With OpenGL, the scenegraph's OpenGL context will be current both when calling the destructor and this function.
