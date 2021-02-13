.. sip:class-description::
    :status: todo
    :brief: Formatting information for frames in a QTextDocument
    :digest: 41be1eaf387b4e78b58285cf63072bc9

The :sip:ref:`~PyQt6.QtGui.QTextFrameFormat` class provides formatting information for frames in a :sip:ref:`~PyQt6.QtGui.QTextDocument`.

A text frame groups together one or more blocks of text, providing a layer of structure larger than the paragraph. The format of a frame specifies how it is rendered and positioned on the screen. It does not directly specify the behavior of the text formatting within, but provides constraints on the layout of its children.

The frame format defines the :sip:ref:`~PyQt6.QtGui.QTextFrameFormat.width` and :sip:ref:`~PyQt6.QtGui.QTextFrameFormat.height` of the frame on the screen. Each frame can have a :sip:ref:`~PyQt6.QtGui.QTextFrameFormat.border` that surrounds its contents with a rectangular box. The border is surrounded by a :sip:ref:`~PyQt6.QtGui.QTextFrameFormat.margin` around the frame, and the contents of the frame are kept separate from the border by the frame's :sip:ref:`~PyQt6.QtGui.QTextFrameFormat.padding`. This scheme is similar to the box model used by Cascading Style Sheets for HTML pages.

.. image:: ../../../images/qtextframe-style.png

The :sip:ref:`~PyQt6.QtGui.QTextFrameFormat.position` of a frame is set using :sip:ref:`~PyQt6.QtGui.QTextFrameFormat.setPosition` and determines how it is located relative to the surrounding text.

The validity of a :sip:ref:`~PyQt6.QtGui.QTextFrameFormat` object can be determined with the :sip:ref:`~PyQt6.QtGui.QTextFrameFormat.isValid` function.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextFrame`, :sip:ref:`~PyQt6.QtGui.QTextBlockFormat`.
