.. sip:method-description::
    :status: todo
    :pysig: ed36a1ef76a59ee3f15180e0441188ad
    :realsig: () const
    :digest: 98036733218d95e702dd8ad91c539030

Returns a color if the data stored in the object represents a color (MIME type ``application/x-color``); otherwise returns a null variant.

A `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ is used because :sip:ref:`~PyQt6.QtCore.QMimeData` belongs to the Qt Core module, whereas QColor belongs to Qt GUI. To convert the `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_ to a QColor, simply use qvariant_cast(). For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qmimedata.py
    :lines: 116-119

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMimeData.hasColor`, :sip:ref:`~PyQt6.QtCore.QMimeData.setColorData`, :sip:ref:`~PyQt6.QtCore.QMimeData.data`.
