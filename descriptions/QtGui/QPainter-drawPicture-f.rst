.. sip:method-description::
    :status: todo
    :pysig: 5bb5d3c9e8ef08fea611b5a0e5b0e6aa
    :realsig: (const QPointF&,const QPicture&)
    :digest: 65e7f061496c980ebcd3635781341c34

Replays the given *picture* at the given *point*.

The :sip:ref:`~PyQt6.QtGui.QPicture` class is a paint device that records and replays :sip:ref:`~PyQt6.QtGui.QPainter` commands. A picture serializes the painter commands to an IO device in a platform-independent format. Everything that can be painted on a widget or pixmap can also be stored in a picture.

This function does exactly the same as :sip:ref:`~PyQt6.QtGui.QPicture.play` when called with *point* = :sip:ref:`~PyQt6.QtCore.QPointF`\ (0, 0).

**Note:** The state of the painter is preserved by this function.

+-----------------------------------------------------------------------------------------------------+
| .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainter.py |
|     :lines: 339-344                                                                                 |
+-----------------------------------------------------------------------------------------------------+

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPicture.play`.
