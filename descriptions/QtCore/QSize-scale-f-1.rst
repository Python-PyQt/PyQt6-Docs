.. sip:method-description::
    :status: todo
    :pysig: 3d8b87ee3e15288613f24a10102ac754
    :realsig: (int,int,Qt::AspectRatioMode)
    :digest: 1d207cdf7558c100b0641f1ffea7986f

Scales the size to a rectangle with the given *width* and *height*, according to the specified *mode*:

* If *mode* is :sip:ref:`~PyQt6.QtCore.Qt.AspectRatioMode.IgnoreAspectRatio`, the size is set to (\ *width*, *height*).

* If *mode* is :sip:ref:`~PyQt6.QtCore.Qt.AspectRatioMode.KeepAspectRatio`, the current size is scaled to a rectangle as large as possible inside (\ *width*, *height*), preserving the aspect ratio.

* If *mode* is :sip:ref:`~PyQt6.QtCore.Qt.AspectRatioMode.KeepAspectRatioByExpanding`, the current size is scaled to a rectangle as small as possible outside (\ *width*, *height*), preserving the aspect ratio.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qsize.py
    :lines: 54-64

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSize.setWidth`, :sip:ref:`~PyQt6.QtCore.QSize.setHeight`, :sip:ref:`~PyQt6.QtCore.QSize.scaled`.
