.. sip:class-description::
    :status: todo
    :brief: Adds a volume rendered object to a graph
    :digest: ed36f880eec909e67194a8ab4f7edf11

The :sip:ref:`~PyQt6.QtDataVisualization.QCustom3DVolume` class adds a volume rendered object to a graph.

A volume rendered object is a box with a 3D texture. Three slice planes are supported for the volume, one along each main axis of the volume.

Rendering volume objects is very performance intensive, especially when the volume is largely transparent, as the contents of the volume are ray-traced. The performance scales nearly linearly with the amount of pixels that the volume occupies on the screen, so showing the volume in a smaller view or limiting the zoom level of the graph are easy ways to improve performance. Similarly, the volume texture dimensions have a large impact on performance. If the frame rate is more important than pixel-perfect rendering of the volume contents, consider turning the high definition shader off by setting the :sip:ref:`~PyQt6.QtDataVisualization.QCustom3DVolume.useHighDefShader` property to ``false``.

**Note:** Volumetric objects are only supported with orthographic projection.

**Note:** Volumetric objects utilize 3D textures, which are not supported in OpenGL ES2 environments.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph.addCustomItem`, QAbstract3DGraph::orthoProjection, :sip:ref:`~PyQt6.QtDataVisualization.QCustom3DVolume.useHighDefShader`.
