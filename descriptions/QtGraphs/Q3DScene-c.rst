.. sip:class-description::
    :status: todo
    :brief: Description of the 3D scene being visualized
    :digest: 3d8158255304cfab0dfeabf615a27167

:sip:ref:`~PyQt6.QtGraphs.Q3DScene` class provides description of the 3D scene being visualized.

The 3D scene contains a single active camera and a single active light source. Visualized data is assumed to be at a fixed location.

The 3D scene also keeps track of the viewport in which graph rendering is done, the primary subviewport inside the viewport where the main 3D graphs view resides and the secondary subviewport where the 2D sliced view of the data resides. The subviewports are by default resized by the *Q3DScene*. To override the resize behavior you need to listen to both :sip:ref:`~PyQt6.QtGraphs.Q3DScene.viewportChanged` and :sip:ref:`~PyQt6.QtGraphs.Q3DScene.slicingActiveChanged` signals and recalculate the subviewports accordingly.

Also the scene has flag for tracking if the secondary 2D slicing view is currently active or not.

**Note:** Not all graphs support the secondary 2D slicing view.
