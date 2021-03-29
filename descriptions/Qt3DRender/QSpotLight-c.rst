.. sip:class-description::
    :status: todo
    :brief: Encapsulate a Spot Light object in a Qt 3D scene
    :realname: Qt3DRender::QSpotLight
    :digest: b9f2ae914c4b1e49b4ee02624aece170

Encapsulate a Spot Light object in a Qt 3D scene.

A spotlight is a light source that emits a cone of light in a particular direction.

A spotlight uses three attenuation factors to describe how the intensity of the light decreases over distance. These factors are designed to be used together in calcuating total attenuation. For the materials in Qt3D Extras the following formula is used, where distance is the distance from the light to the surface being rendered:

::

    totalAttenuation = 1.0 / (constantAttenuation + (linearAttenuation * distance) + (quadraticAttenuation * distance * distance));

Custom materials may choose to interpret these factors differently.
