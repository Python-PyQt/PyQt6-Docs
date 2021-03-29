.. sip:class-description::
    :status: todo
    :brief: Default implementation for rendering the color properties set for each vertex
    :realname: Qt3DExtras::QPerVertexColorMaterial
    :digest: 863e5ec98aeccc20ee7f341275ace0d2

The :sip:ref:`~PyQt6.Qt3DExtras.QPerVertexColorMaterial` class provides a default implementation for rendering the color properties set for each vertex.

This lighting effect is based on the combination of 2 lighting components ambient and diffuse. Ambient is set by the vertex color. Diffuse takes in account the normal distribution of each vertex.

* Ambient is the color that is emitted by an object without any other light source.

* Diffuse is the color that is emitted for rough surface reflections with the lights

This material uses an effect with a single render pass approach and forms fragment lighting. Techniques are provided for OpenGL 2, OpenGL 3 or above as well as OpenGL ES 2.
