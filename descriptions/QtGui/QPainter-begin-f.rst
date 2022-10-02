.. sip:method-description::
    :status: todo
    :pysig: a6e3c1ac98eb4944976ba11508f63fd1
    :realsig: (QPaintDevice*)
    :digest: 3ba5b8c9f553e3138dce6b141120fa75

Begins painting the paint *device* and returns ``true`` if successful; otherwise returns ``false``.

Notice that all painter settings (\ :sip:ref:`~PyQt6.QtGui.QPainter.setPen`, :sip:ref:`~PyQt6.QtGui.QPainter.setBrush` etc.) are reset to default values when begin() is called.

The errors that can occur are serious problems, such as these:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainter.py
    :lines: 132-138

Note that most of the time, you can use one of the constructors instead of begin(), and that :sip:ref:`~PyQt6.QtGui.QPainter.end` is automatically done at destruction.

**Warning:** A paint device can only be painted by one painter at a time.

**Warning:** Painting on a :sip:ref:`~PyQt6.QtGui.QImage` with the format :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_Indexed8` is not supported.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.end`, :sip:ref:`~PyQt6.QtGui.QPainter`.
