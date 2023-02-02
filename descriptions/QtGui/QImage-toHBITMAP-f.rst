.. sip:method-description::
    :status: todo
    :pysig: 9daeab2db5574297592cfe242f3e4da3
    :realsig: () const
    :digest: bb75c9c44e88fd0a90023699549a919d

Creates a ``HBITMAP`` equivalent of the :sip:ref:`~PyQt6.QtGui.QImage`.

Returns the ``HBITMAP`` handle.

It is the caller's responsibility to free the ``HBITMAP`` data after use.

For usage with with standard GDI calls, such as ``BitBlt()``, the image should have the format :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_RGB32`.

When using the resulting HBITMAP for the ``AlphaBlend()`` GDI function, the image should have the format :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_ARGB32_Premultiplied` (use :sip:ref:`~PyQt6.QtGui.QImage.convertToFormat`).

When using the resulting HBITMAP as application icon or a systray icon, the image should have the format :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_ARGB32`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.fromHBITMAP`, :sip:ref:`~PyQt6.QtGui.QImage.convertToFormat`.
