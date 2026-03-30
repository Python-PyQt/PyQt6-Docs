.. sip:method-description::
    :status: todo
    :pysig: 502f7d3e77c89e5ef63bfbd42eaccbfd
    :realsig: (const QString&) const
    :digest: 497e339954929992e22d8111630e615a

Returns true if the element with the given *id* exists in the currently parsed SVG file and is a renderable element.

Note: this method returns true only for elements that can be rendered. Which implies that elements that are considered part of the fill/stroke style properties, e.g. radialGradients even tough marked with "id" attributes will not be found by this method.
