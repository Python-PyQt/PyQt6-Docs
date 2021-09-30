.. sip:class-description::
    :status: todo
    :brief: Window and render loop for graphs
    :digest: 14bf2f6b7170bdb4a193030c87c1467f

The :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph` class provides a window and render loop for graphs.

This class subclasses a :sip:ref:`~PyQt6.QtGui.QWindow` and provides render loop for graphs inheriting it.

You should not need to use this class directly, but one of its subclasses instead.

Anti-aliasing is turned on by default on C++, except in OpenGL ES2 environments, where anti-aliasing is not supported by Qt Data Visualization. To specify non-default anti-aliasing for a graph, give a custom surface format as a constructor parameter. You can use the convenience function ``qDefaultSurfaceFormat()`` to create the surface format object.

**Note:** :sip:ref:`~PyQt6.QtDataVisualization.QAbstract3DGraph` sets window flag ``Qt::FramelessWindowHint`` on by default. If you want to display graph windows as standalone windows with regular window frame, clear this flag after constructing the graph. For example:

::

    Q3DBars *graphWindow = new Q3DBars;
    graphWindow->setFlags(graphWindow->flags() ^ Qt::FramelessWindowHint);

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DScatter`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DSurface`, :sip:ref:`~PyQt6.Qt Data Visualization C++ Classes`.
