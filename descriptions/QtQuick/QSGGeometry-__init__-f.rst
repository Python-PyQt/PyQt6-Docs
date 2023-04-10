.. sip:method-description::
    :status: todo
    :pysig: 398f8272eed7656d66501d1a89516855
    :realsig: (const QSGGeometry::AttributeSet&,int,int,int)
    :digest: 1fad3bff56f0b54252bf8788c5021d61

Constructs a geometry object based on *attributes*.

The object allocate space for *vertexCount* vertices based on the accumulated size in *attributes* and for *indexCount*.

The *indexType* can be :sip:ref:`~PyQt6.QtQuick.QSGGeometry.Type.UnsignedShortType` or ``UnsignedIntType``. Support for the latter depends on the graphics API implementation used at run time, and may not always be available.

Geometry objects are constructed by default with :sip:ref:`~PyQt6.QtQuick.QSGGeometry.DrawingMode.DrawTriangleStrip` as the drawing mode.

**Note:** *attributes* and the :sip:ref:`~PyQt6.QtQuick.QSGGeometry.Attribute` objects referenced by it must stay valid for the entire lifetime of the :sip:ref:`~PyQt6.QtQuick.QSGGeometry`. :sip:ref:`~PyQt6.QtQuick.QSGGeometry` stores a reference to *attributes* and does not delete the :sip:ref:`~PyQt6.QtQuick.QSGGeometry.Attribute` objects.
