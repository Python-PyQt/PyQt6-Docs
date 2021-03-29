.. sip:method-description::
    :status: todo
    :pysig: 398f8272eed7656d66501d1a89516855
    :realsig: (const QSGGeometry::AttributeSet&,int,int,int)
    :digest: 0b48e07655a32016e0d205fc8b2fce44

Constructs a geometry object based on *attributes*.

The object allocate space for *vertexCount* vertices based on the accumulated size in *attributes* and for *indexCount*.

The *indexType* can be :sip:ref:`~PyQt6.QtQuick.QSGGeometry.Type.UnsignedShortType` or ``UnsignedIntType``. Support for the latter depends on the graphics API implementation used at run time, and may not always be available.

Geometry objects are constructed by default with :sip:ref:`~PyQt6.QtQuick.QSGGeometry.DrawingMode.DrawTriangleStrip` as the drawing mode.

The attribute structure is assumed to be POD and the geometry object assumes this will not go away. There is no memory management involved.
