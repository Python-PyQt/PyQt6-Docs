.. sip:class-description::
    :status: todo
    :brief: Allows creation of a 2D text in 3D space
    :realname: Qt3DExtras::QText2DEntity
    :digest: 2b5530208d25040fefd343de0197efd9

:sip:ref:`~PyQt6.Qt3DExtras.QText2DEntity` allows creation of a 2D text in 3D space.

The :sip:ref:`~PyQt6.Qt3DExtras.QText2DEntity` renders text as triangles in the XY plane. The geometry will be fitted in the rectangle of specified width and height. If the resulting geometry is wider than the specified width, the remainder will be rendered on the new line.

The entity can be positionned in the scene by adding a transform component.

:sip:ref:`~PyQt6.Qt3DExtras.QText2DEntity` will create geometry based on the shape of the glyphs and a solid material using the specified color.
