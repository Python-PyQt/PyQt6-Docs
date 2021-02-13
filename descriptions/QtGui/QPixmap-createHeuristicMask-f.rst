.. sip:method-description::
    :status: todo
    :pysig: 79ba933dec236434c1b9b0fbf8a8ace6
    :realsig: (bool) const
    :digest: 753f86fd6c188c4989a55e862552777f

Creates and returns a heuristic mask for this pixmap.

The function works by selecting a color from one of the corners and then chipping away pixels of that color, starting at all the edges. If *clipTight* is true (the default) the mask is just large enough to cover the pixels; otherwise, the mask is larger than the data pixels.

The mask may not be perfect but it should be reasonable, so you can do things such as the following:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_image_qpixmap.py
    :lines: 60-61

This function is slow because it involves converting to/from a :sip:ref:`~PyQt6.QtGui.QImage`, and non-trivial computations.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.createHeuristicMask`, :sip:ref:`~PyQt6.QtGui.QPixmap.createMaskFromColor`.
