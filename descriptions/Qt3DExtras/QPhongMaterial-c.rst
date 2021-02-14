.. sip:class-description::
    :status: todo
    :brief: Default implementation of the phong lighting effect
    :realname: Qt3DExtras::QPhongMaterial
    :digest: be33650500b6594005d823eed4a0bc33

The :sip:ref:`~PyQt6.Qt3DExtras.QPhongMaterial` class provides a default implementation of the phong lighting effect.

This class is deprecated; use QDiffuseSpecularMaterial instead.

The phong lighting effect is based on the combination of 3 lighting components ambient, diffuse and specular. The relative strengths of these components are controlled by means of their reflectivity coefficients which are modelled as RGB triplets:

* Ambient is the color that is emitted by an object without any other light source.

* Diffuse is the color that is emitted for rought surface reflections with the lights.

* Specular is the color emitted for shiny surface reflections with the lights.

* The shininess of a surface is controlled by a float property.

This material uses an effect with a single render pass approach and performs per fragment lighting. Techniques are provided for OpenGL 2, OpenGL 3 or above as well as OpenGL ES 2.
