.. sip:method-description::
    :status: todo
    :pysig: ed36a1ef76a59ee3f15180e0441188ad
    :realsig: (const QVariant&)
    :digest: 5770c354de033b1109a1d3e815845007

Sets the data in the object to the given *image*.

A `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ is used because :sip:ref:`~PyQt6.QtCore.QMimeData` belongs to the Qt Core module, whereas QImage belongs to Qt GUI. The conversion from QImage to `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ is implicit. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qmimedata.py
    :lines: 111-111

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMimeData.imageData`, :sip:ref:`~PyQt6.QtCore.QMimeData.hasImage`, :sip:ref:`~PyQt6.QtCore.QMimeData.setData`.
