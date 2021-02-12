.. sip:method-description::
    :status: todo
    :pysig: c987eb0cc891477f2ba6af89f0e6a74b
    :realsig: (qreal,qreal,Qt::AspectRatioMode)
    :digest: 1d207cdf7558c100b0641f1ffea7986f

Scales the size to a rectangle with the given *width* and *height*, according to the specified *mode*.

* If *mode* is :sip:ref:`~PyQt6.QtCore.Qt.AspectRatioMode.IgnoreAspectRatio`, the size is set to (\ *width*, *height*).

* If *mode* is :sip:ref:`~PyQt6.QtCore.Qt.AspectRatioMode.KeepAspectRatio`, the current size is scaled to a rectangle as large as possible inside (\ *width*, *height*), preserving the aspect ratio.

* If *mode* is :sip:ref:`~PyQt6.QtCore.Qt.AspectRatioMode.KeepAspectRatioByExpanding`, the current size is scaled to a rectangle as small as possible outside (\ *width*, *height*), preserving the aspect ratio.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qsize.py
    :lines: 103-113

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSizeF.setWidth`, :sip:ref:`~PyQt6.QtCore.QSizeF.setHeight`, :sip:ref:`~PyQt6.QtCore.QSizeF.scaled`.
