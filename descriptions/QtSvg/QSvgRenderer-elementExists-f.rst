.. sip:method-description::
    :status: todo
    :pysig: 9d2496c01394f04863ec354dfad3b4be
    :realsig: (const QString&) const
    :digest: 497e339954929992e22d8111630e615a

Returns true if the element with the given *id* exists in the currently parsed SVG file and is a renderable element.

Note: this method returns true only for elements that can be rendered. Which implies that elements that are considered part of the fill/stroke style properties, e.g. radialGradients even tough marked with "id" attributes will not be found by this method.
