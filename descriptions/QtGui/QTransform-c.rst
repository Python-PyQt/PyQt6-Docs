.. sip:class-description::
    :status: todo
    :brief: Specifies 2D transformations of a coordinate system
    :digest: f6ca2d49b4342dbd59edbd53fb4f1fca

The :sip:ref:`~PyQt6.QtGui.QTransform` class specifies 2D transformations of a coordinate system.

A transformation specifies how to translate, scale, shear, rotate or project the coordinate system, and is typically used when rendering graphics.

A :sip:ref:`~PyQt6.QtGui.QTransform` object can be built using the :sip:ref:`~PyQt6.QtGui.QTransform.setMatrix`, :sip:ref:`~PyQt6.QtGui.QTransform.scale`, :sip:ref:`~PyQt6.QtGui.QTransform.rotate`, :sip:ref:`~PyQt6.QtGui.QTransform.translate` and :sip:ref:`~PyQt6.QtGui.QTransform.shear` functions. Alternatively, it can be built by applying basic matrix operations. The matrix can also be defined when constructed, and it can be reset to the identity matrix (the default) using the :sip:ref:`~PyQt6.QtGui.QTransform.reset` function.

The :sip:ref:`~PyQt6.QtGui.QTransform` class supports mapping of graphic primitives: A given point, line, polygon, region, or painter path can be mapped to the coordinate system defined by *this* matrix using the :sip:ref:`~PyQt6.QtGui.QTransform.map` function. In case of a rectangle, its coordinates can be transformed using the :sip:ref:`~PyQt6.QtGui.QTransform.mapRect` function. A rectangle can also be transformed into a *polygon* (mapped to the coordinate system defined by *this* matrix), using the :sip:ref:`~PyQt6.QtGui.QTransform.mapToPolygon` function.

:sip:ref:`~PyQt6.QtGui.QTransform` provides the :sip:ref:`~PyQt6.QtGui.QTransform.isIdentity` function which returns ``true`` if the matrix is the identity matrix, and the :sip:ref:`~PyQt6.QtGui.QTransform.isInvertible` function which returns ``true`` if the matrix is non-singular (i.e. AB = BA = I). The :sip:ref:`~PyQt6.QtGui.QTransform.inverted` function returns an inverted copy of *this* matrix if it is invertible (otherwise it returns the identity matrix), and :sip:ref:`~PyQt6.QtGui.QTransform.adjoint` returns the matrix's classical adjoint. In addition, :sip:ref:`~PyQt6.QtGui.QTransform` provides the :sip:ref:`~PyQt6.QtGui.QTransform.determinant` function which returns the matrix's determinant.

Finally, the :sip:ref:`~PyQt6.QtGui.QTransform` class supports matrix multiplication, addition and subtraction, and objects of the class can be streamed as well as compared.

.. _qtransform-rendering-graphics:

Rendering Graphics
------------------

When rendering graphics, the matrix defines the transformations but the actual transformation is performed by the drawing routines in :sip:ref:`~PyQt6.QtGui.QPainter`.

By default, :sip:ref:`~PyQt6.QtGui.QPainter` operates on the associated device's own coordinate system. The standard coordinate system of a :sip:ref:`~PyQt6.QtGui.QPaintDevice` has its origin located at the top-left position. The *x* values increase to the right; *y* values increase downward. For a complete description, see the `coordinate system <https://doc.qt.io/qt-6/coordsys.html>`_ documentation.

:sip:ref:`~PyQt6.QtGui.QPainter` has functions to translate, scale, shear and rotate the coordinate system without using a :sip:ref:`~PyQt6.QtGui.QTransform`. For example:

+---------------------------------------------+-------------------------------------------------------------------------------------+
| |image-qtransform-simpletransformation-png| | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-transform-main.py |
|                                             |     :lines: 64-75                                                                   |
+---------------------------------------------+-------------------------------------------------------------------------------------+

Although these functions are very convenient, it can be more efficient to build a :sip:ref:`~PyQt6.QtGui.QTransform` and call :sip:ref:`~PyQt6.QtGui.QPainter.setTransform` if you want to perform more than a single transform operation. For example:

+-----------------------------------------------+-------------------------------------------------------------------------------------+
| |image-qtransform-combinedtransformation-png| | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-transform-main.py |
|                                               |     :lines: 84-99                                                                   |
+-----------------------------------------------+-------------------------------------------------------------------------------------+

.. _qtransform-basic-matrix-operations:

Basic Matrix Operations
-----------------------

.. image:: ../../../images/qtransform-representation.png

A :sip:ref:`~PyQt6.QtGui.QTransform` object contains a 3 x 3 matrix. The ``m31`` (``dx``) and ``m32`` (``dy``) elements specify horizontal and vertical translation. The ``m11`` and ``m22`` elements specify horizontal and vertical scaling. The ``m21`` and ``m12`` elements specify horizontal and vertical *shearing*. And finally, the ``m13`` and ``m23`` elements specify horizontal and vertical projection, with ``m33`` as an additional projection factor.

:sip:ref:`~PyQt6.QtGui.QTransform` transforms a point in the plane to another point using the following formulas:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qtransform.py
    :lines: 57-63

The point *(x, y)* is the original point, and *(x', y')* is the transformed point. *(x', y')* can be transformed back to *(x, y)* by performing the same operation on the :sip:ref:`~PyQt6.QtGui.QTransform.inverted` matrix.

The various matrix elements can be set when constructing the matrix, or by using the :sip:ref:`~PyQt6.QtGui.QTransform.setMatrix` function later on. They can also be manipulated using the :sip:ref:`~PyQt6.QtGui.QTransform.translate`, :sip:ref:`~PyQt6.QtGui.QTransform.rotate`, :sip:ref:`~PyQt6.QtGui.QTransform.scale` and :sip:ref:`~PyQt6.QtGui.QTransform.shear` convenience functions. The currently set values can be retrieved using the :sip:ref:`~PyQt6.QtGui.QTransform.m11`, :sip:ref:`~PyQt6.QtGui.QTransform.m12`, :sip:ref:`~PyQt6.QtGui.QTransform.m13`, :sip:ref:`~PyQt6.QtGui.QTransform.m21`, :sip:ref:`~PyQt6.QtGui.QTransform.m22`, :sip:ref:`~PyQt6.QtGui.QTransform.m23`, :sip:ref:`~PyQt6.QtGui.QTransform.m31`, :sip:ref:`~PyQt6.QtGui.QTransform.m32`, :sip:ref:`~PyQt6.QtGui.QTransform.m33`, :sip:ref:`~PyQt6.QtGui.QTransform.dx` and :sip:ref:`~PyQt6.QtGui.QTransform.dy` functions.

Translation is the simplest transformation. Setting ``dx`` and ``dy`` will move the coordinate system ``dx`` units along the X axis and ``dy`` units along the Y axis. Scaling can be done by setting ``m11`` and ``m22``. For example, setting ``m11`` to 2 and ``m22`` to 1.5 will double the height and increase the width by 50%. The identity matrix has ``m11``, ``m22``, and ``m33`` set to 1 (all others are set to 0) mapping a point to itself. Shearing is controlled by ``m12`` and ``m21``. Setting these elements to values different from zero will twist the coordinate system. Rotation is achieved by setting both the shearing factors and the scaling factors. Perspective transformation is achieved by setting both the projection factors and the scaling factors.

Here's the combined transformations example using basic matrix operations:

+------------------------------------------------+-------------------------------------------------------------------------------------+
| |image-qtransform-combinedtransformation2-png| | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-transform-main.py |
|                                                |     :lines: 108-132                                                                 |
+------------------------------------------------+-------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter`, `Coordinate System <https://doc.qt.io/qt-6/coordsys.html>`_.

.. |image-qtransform-simpletransformation-png| image:: ../../../images/qtransform-simpletransformation.png
.. |image-qtransform-combinedtransformation-png| image:: ../../../images/qtransform-combinedtransformation.png
.. |image-qtransform-combinedtransformation2-png| image:: ../../../images/qtransform-combinedtransformation2.png
