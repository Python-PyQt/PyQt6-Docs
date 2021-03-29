.. sip:class-description::
    :status: todo
    :brief: Encapsulate a Point Light object in a Qt 3D scene
    :realname: Qt3DRender::QPointLight
    :digest: ba35a743f485e68351395cd432bb3b2b

Encapsulate a Point Light object in a Qt 3D scene.

A point light is a light source that emits light in all directions, from a single point. Conceptually, this is similar to light given off by a standard light bulb.

A point light uses three attenuation factors to describe how the intensity of the light decreases over distance. These factors are designed to be used together in calcuating total attenuation. For the materials in Qt3D Extras the following formula is used, where distance is the distance from the light to the surface being rendered:

::

    totalAttenuation = 1.0 / (constantAttenuation + (linearAttenuation * distance) + (quadraticAttenuation * distance * distance));

Custom materials may choose to interpret these factors differently.
