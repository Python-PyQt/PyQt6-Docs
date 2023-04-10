.. sip:class-description::
    :status: todo
    :brief: Methods for rendering 3D scatter graphs
    :digest: 9f4fc50a8c92bda53b86c6cec813400c

The :sip:ref:`~PyQt6.QtDataVisualization.Q3DScatter` class provides methods for rendering 3D scatter graphs.

This class enables developers to render scatter graphs in 3D and to view them by rotating the scene freely. Rotation is done by holding down the right mouse button and moving the mouse. Zooming is done by mouse wheel. Selection, if enabled, is done by left mouse button. The scene can be reset to default camera view by clicking mouse wheel. In touch devices rotation is done by tap-and-move, selection by tap-and-hold and zoom by pinch.

If no axes are set explicitly to :sip:ref:`~PyQt6.QtDataVisualization.Q3DScatter`, temporary default axes with no labels are created. These default axes can be modified via axis accessors, but as soon any axis is set explicitly for the orientation, the default axis for that orientation is destroyed.

:sip:ref:`~PyQt6.QtDataVisualization.Q3DScatter` supports more than one series visible at the same time.

.. _q3dscatter-how-to-construct-a-minimal-q3dscatter-graph:

How to construct a minimal Q3DScatter graph
-------------------------------------------

First, construct :sip:ref:`~PyQt6.QtDataVisualization.Q3DScatter`. Since we are running the graph as top level window in this example, we need to clear the ``Qt::FramelessWindowHint`` flag, which gets set by default:

.. literalinclude:: ../../../snippets/qtdatavis3d-src-datavisualization-doc-snippets-doc_src_q3dscatter_construction.py
    :lines: 41-42

Now :sip:ref:`~PyQt6.QtDataVisualization.Q3DScatter` is ready to receive data to be rendered. Add one series of 3 :sip:ref:`~PyQt6.QtGui.QVector3D` items:

.. literalinclude:: ../../../snippets/qtdatavis3d-src-datavisualization-doc-snippets-doc_src_q3dscatter_construction.py
    :lines: 45-49

Finally you will need to set it visible:

.. literalinclude:: ../../../snippets/qtdatavis3d-src-datavisualization-doc-snippets-doc_src_q3dscatter_construction.py
    :lines: 52-52

The complete code needed to create and display this graph is:

.. literalinclude:: ../../../snippets/qtdatavis3d-src-datavisualization-doc-snippets-doc_src_q3dscatter_construction.py
    :lines: 33-56

And this is what those few lines of code produce:

.. image:: ../../../images/q3dscatter-minimal.png

The scene can be rotated, zoomed into, and an item can be selected to view its position, but no other interaction is included in this minimal code example. You can learn more by familiarizing yourself with the examples provided, like the `Scatter Graph <https://doc.qt.io/qt-6/qtdatavis3d-graphgallery-example.html#scatter-graph>`_.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DSurface`, :sip:ref:`~PyQt6.Qt Data Visualization C++ Classes`.
