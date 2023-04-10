.. sip:class-description::
    :status: todo
    :brief: Methods for rendering 3D bar graphs
    :digest: 0dc52bcff9f15c3cc404c445d235ed31

The :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars` class provides methods for rendering 3D bar graphs.

This class enables developers to render bar graphs in 3D and to view them by rotating the scene freely. Rotation is done by holding down the right mouse button and moving the mouse. Zooming is done by mouse wheel. Selection, if enabled, is done by left mouse button. The scene can be reset to default camera view by clicking mouse wheel. In touch devices rotation is done by tap-and-move, selection by tap-and-hold and zoom by pinch.

If no axes are set explicitly to :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars`, temporary default axes with no labels are created. These default axes can be modified via axis accessors, but as soon any axis is set explicitly for the orientation, the default axis for that orientation is destroyed.

:sip:ref:`~PyQt6.QtDataVisualization.Q3DBars` supports more than one series visible at the same time. It is not necessary for all series to have the same amount of rows and columns. Row and column labels are taken from the first added series, unless explicitly defined to row and column axes.

.. _q3dbars-how-to-construct-a-minimal-q3dbars-graph:

How to construct a minimal Q3DBars graph
----------------------------------------

First, construct an instance of :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars`. Since we are running the graph as top level window in this example, we need to clear the ``Qt::FramelessWindowHint`` flag, which gets set by default:

.. literalinclude:: ../../../snippets/qtdatavis3d-src-datavisualization-doc-snippets-doc_src_q3dbars_construction.py
    :lines: 41-42

After constructing :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars`, you can set the data window by changing the range on the row and column axes. It is not mandatory, as data window will default to showing all of the data in the series. If the amount of data is large, it is usually preferable to show just a portion of it. For the example, let's set the data window to show first five rows and columns:

.. literalinclude:: ../../../snippets/qtdatavis3d-src-datavisualization-doc-snippets-doc_src_q3dbars_construction.py
    :lines: 45-46

Now :sip:ref:`~PyQt6.QtDataVisualization.Q3DBars` is ready to receive data to be rendered. Create a series with one row of 5 values:

.. literalinclude:: ../../../snippets/qtdatavis3d-src-datavisualization-doc-snippets-doc_src_q3dbars_construction.py
    :lines: 49-53

**Note:** We set the data window to 5 x 5, but we are adding only one row of data. This is ok, the rest of the rows will just be blank.

Finally you will need to set it visible:

.. literalinclude:: ../../../snippets/qtdatavis3d-src-datavisualization-doc-snippets-doc_src_q3dbars_construction.py
    :lines: 56-56

The complete code needed to create and display this graph is:

.. literalinclude:: ../../../snippets/qtdatavis3d-src-datavisualization-doc-snippets-doc_src_q3dbars_construction.py
    :lines: 33-60

And this is what those few lines of code produce:

.. image:: ../../../images/q3dbars-minimal.png

The scene can be rotated, zoomed into, and a bar can be selected to view its value, but no other interaction is included in this minimal code example. You can learn more by familiarizing yourself with the examples provided, like the `Bar Graph <https://doc.qt.io/qt-6/qtdatavis3d-graphgallery-example.html#bar-graph>`_.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.Q3DScatter`, :sip:ref:`~PyQt6.QtDataVisualization.Q3DSurface`, :sip:ref:`~PyQt6.Qt Data Visualization C++ Classes`.
