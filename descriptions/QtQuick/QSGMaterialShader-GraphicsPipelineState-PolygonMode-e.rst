.. sip:enum-description::
    :status: todo
    :digest: bba9e58ca67179f776debedb2d5f8683

Specifies the polygon rasterization mode

Polygon Mode (Triangle Fill Mode in Metal, Fill Mode in D3D) specifies the fill mode used when rasterizing polygons. Polygons may be drawn as solids (Fill), or as a wire mesh (Line).

**Warning:** OpenGL ES does not support the ``Line`` polygon mode. OpenGL ES will rasterize all polygons as filled no matter what polygon mode is set. Using ``Line`` will make your application non-portable.
