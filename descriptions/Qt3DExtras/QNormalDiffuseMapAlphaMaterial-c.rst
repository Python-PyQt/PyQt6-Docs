.. sip:class-description::
    :status: todo
    :brief: Specialization of QNormalDiffuseMapMaterial with alpha coverage and a depth test performed in the rendering pass
    :realname: Qt3DExtras::QNormalDiffuseMapAlphaMaterial
    :digest: 6c57526bcd6d2a0189d69654aa394885

The :sip:ref:`~PyQt6.Qt3DExtras.QNormalDiffuseMapAlphaMaterial` provides a specialization of QNormalDiffuseMapMaterial with alpha coverage and a depth test performed in the rendering pass.

This class is deprecated; use :sip:ref:`~PyQt6.Qt3DExtras.QDiffuseSpecularMaterial` instead.

The specular lighting effect is based on the combination of 3 lighting components ambient, diffuse and specular. The relative strengths of these components are controlled by means of their reflectivity coefficients which are modelled as RGB triplets:

* Ambient is the color that is emitted by an object without any other light source.

* Diffuse is the color that is emitted for rought surface reflections with the lights.

* Specular is the color emitted for shiny surface reflections with the lights.

* The shininess of a surface is controlled by a float property.

This material uses an effect with a single render pass approach and performs per fragment lighting. Techniques are provided for OpenGL 2, OpenGL 3 or above as well as OpenGL ES 2.
