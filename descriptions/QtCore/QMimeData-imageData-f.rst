.. sip:method-description::
    :status: todo
    :pysig: ed36a1ef76a59ee3f15180e0441188ad
    :realsig: () const
    :digest: e383f06ebb44492be17a55d1bd1848ec

Returns a `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ storing a QImage if the object can return an image; otherwise returns a null variant.

A `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ is used because :sip:ref:`~PyQt6.QtCore.QMimeData` belongs to the Qt Core module, whereas QImage belongs to Qt GUI. To convert the `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ to a QImage, simply use qvariant_cast(). For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qmimedata.py
    :lines: 103-106

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMimeData.setImageData`, :sip:ref:`~PyQt6.QtCore.QMimeData.hasImage`.
