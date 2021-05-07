.. sip:class-description::
    :status: todo
    :brief: Methods for rendering 3D surface plots
    :digest: ef28033277d778b2652b309b85d1a617

The :sip:ref:`~PyQt6.QtDataVisualization.Q3DSurface` class provides methods for rendering 3D surface plots.

This class enables developers to render 3D surface plots and to view them by rotating the scene freely. The visual properties of the surface such as draw mode and shading can be controlled via :sip:ref:`~PyQt6.QtDataVisualization.QSurface3DSeries`.

The :sip:ref:`~PyQt6.QtDataVisualization.Q3DSurface` supports selection by showing a highlighted ball on the data point where the user has clicked with left mouse button (when default input handler is in use) or selected via :sip:ref:`~PyQt6.QtDataVisualization.QSurface3DSeries`. The selection pointer is accompanied with a label which in default case shows the value of the data point and the coordinates of the point.

The value range and the label format shown on the axis can be controlled through :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxis`.

To rotate the graph, hold down the right mouse button and move the mouse. Zooming is done using mouse wheel. Both assume the default input handler is in use.

If no axes are set explicitly to :sip:ref:`~PyQt6.QtDataVisualization.Q3DSurface`, temporary default axes with no labels are created. These default axes can be modified via axis accessors, but as soon any axis is set explicitly for the orientation, the default axis for that orientation is destroyed.

.. _q3dsurface-how-to-construct-a-minimal-q3dsurface-graph:

How to construct a minimal Q3DSurface graph
-------------------------------------------

First, construct :sip:ref:`~PyQt6.QtDataVisualization.Q3DSurface`. Since we are running the graph as top level window in this example, we need to clear the ``Qt::FramelessWindowHint`` flag, which gets set by default:

.. literalinclude:: ../../../snippets/qtdatavis3d-src-datavisualization-doc-snippets-doc_src_q3dsurface_construction.py
    :lines: 41-42

Now :sip:ref:`~PyQt6.QtDataVisualization.Q3DSurface` is ready to receive data to be rendered. Create data elements to receive values:

.. literalinclude:: ../../../snippets/qtdatavis3d-src-datavisualization-doc-snippets-doc_src_q3dsurface_construction.py
    :lines: 45-47

First feed the data to the row elements and then add their pointers to the data element:

.. literalinclude:: ../../../snippets/qtdatavis3d-src-datavisualization-doc-snippets-doc_src_q3dsurface_construction.py
    :lines: 51-53

Create a new series and set data to it:

.. literalinclude:: ../../../snippets/qtdatavis3d-src-datavisualization-doc-snippets-doc_src_q3dsurface_construction.py
    :lines: 57-59

Finally you will need to set it visible:

.. literalinclude:: ../../../snippets/qtdatavis3d-src-datavisualization-doc-snippets-doc_src_q3dsurface_construction.py
    :lines: 62-62

The complete code needed to create and display this graph is:

.. literalinclude:: ../../../snippets/qtdatavis3d-src-datavisualization-doc-snippets-doc_src_q3dsurface_construction.py
    :lines: 33-66

And this is what those few lines of code produce:

.. image:: ../../../images/q3dsurface-minimal.png

The scene can be rotated, zoomed into, and a surface point can be selected to view its position, but no other interaction is included in this minimal code example. You can learn more by familiarizing yourself with the examples provided, like the `Surface Example <https://doc.qt.io/qt-6/qtdatavisualization-surface-example.html>`_.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DScatter`, :sip:ref:`~PyQt6.Qt Data Visualization C++ Classes`.
