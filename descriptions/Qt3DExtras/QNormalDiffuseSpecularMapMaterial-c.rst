.. sip:class-description::
    :status: todo
    :brief: Default implementation of the phong lighting and bump effect where the diffuse and specular light components are read from texture maps and the normals of the mesh being rendered from a normal texture map
    :realname: Qt3DExtras::QNormalDiffuseSpecularMapMaterial
    :digest: 17bf8c12850233c7a377dc7be42ad574

The :sip:ref:`~PyQt6.Qt3DExtras.QNormalDiffuseSpecularMapMaterial` provides a default implementation of the phong lighting and bump effect where the diffuse and specular light components are read from texture maps and the normals of the mesh being rendered from a normal texture map.

This class is deprecated; use QDiffuseSpecularMaterial instead.

The specular lighting effect is based on the combination of 3 lighting components ambient, diffuse and specular. The relative strengths of these components are controlled by means of their reflectivity coefficients which are modelled as RGB triplets:

* Ambient is the color that is emitted by an object without any other light source.

* Diffuse is the color that is emitted for rought surface reflections with the lights.

* Specular is the color emitted for shiny surface reflections with the lights.

* The shininess of a surface is controlled by a float property.

This material uses an effect with a single render pass approach and performs per fragment lighting. Techniques are provided for OpenGL 2, OpenGL 3 or above as well as OpenGL ES 2.
