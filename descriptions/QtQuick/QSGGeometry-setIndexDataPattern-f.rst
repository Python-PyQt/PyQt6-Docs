.. sip:method-description::
    :status: todo
    :pysig: b483627b01b1091417c62e4ced852518
    :realsig: (QSGGeometry::DataPattern)
    :digest: 64ec91bdbbc39b57d3419929cce35811

Sets the usage pattern for indices to *p*.

The default is :sip:ref:`~PyQt6.QtQuick.QSGGeometry.DataPattern.AlwaysUploadPattern`. When set to anything other than the default, the user must call :sip:ref:`~PyQt6.QtQuick.QSGGeometry.markIndexDataDirty` after changing the index data, in addition to calling :sip:ref:`~PyQt6.QtQuick.QSGNode.markDirty` with :sip:ref:`~PyQt6.QtQuick.QSGNode.DirtyState.DirtyGeometry`.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGGeometry.indexDataPattern`.
