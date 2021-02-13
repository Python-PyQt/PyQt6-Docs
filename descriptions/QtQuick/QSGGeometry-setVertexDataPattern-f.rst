.. sip:method-description::
    :status: todo
    :pysig: b483627b01b1091417c62e4ced852518
    :realsig: (QSGGeometry::DataPattern)
    :digest: 7cdeaa1192e77e7ed810e747d69511dd

Sets the usage pattern for vertices to *p*.

The default is :sip:ref:`~PyQt6.QtQuick.QSGGeometry.DataPattern.AlwaysUploadPattern`. When set to anything other than the default, the user must call :sip:ref:`~PyQt6.QtQuick.QSGGeometry.markVertexDataDirty` after changing the vertex data, in addition to calling :sip:ref:`~PyQt6.QtQuick.QSGNode.markDirty` with :sip:ref:`~PyQt6.QtQuick.QSGNode.DirtyState.DirtyGeometry`.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGGeometry.vertexDataPattern`.
