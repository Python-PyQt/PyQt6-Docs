.. sip:class-description::
    :status: todo
    :brief: Default implementation of the phong lighting effect with alpha
    :realname: Qt3DExtras::QPhongAlphaMaterial
    :digest: 48a104d25ae831bd8f06d0a307c79cc9

The :sip:ref:`~PyQt6.Qt3DExtras.QPhongAlphaMaterial` class provides a default implementation of the phong lighting effect with alpha.

This class is deprecated; use QDiffuseSpecularMaterial instead.

The phong lighting effect is based on the combination of 3 lighting components ambient, diffuse and specular. The relative strengths of these components are controlled by means of their reflectivity coefficients which are modelled as RGB triplets:

* Ambient is the color that is emitted by an object without any other light source.

* Diffuse is the color that is emitted for rought surface reflections with the lights.

* Specular is the color emitted for shiny surface reflections with the lights.

* The shininess of a surface is controlled by a float property.

* Alpha is the transparency of the surface between 0 (fully transparent) and 1 (opaque).

This material uses an effect with a single render pass approach and performs per fragment lighting. Techniques are provided for OpenGL 2, OpenGL 3 or above as well as OpenGL ES 2.
