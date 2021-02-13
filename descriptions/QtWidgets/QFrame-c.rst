.. sip:class-description::
    :status: todo
    :brief: The base class of widgets that can have a frame
    :digest: c432f9057a24dfa5471cdaa15e1c90cc

The :sip:ref:`~PyQt6.QtWidgets.QFrame` class is the base class of widgets that can have a frame.

:sip:ref:`~PyQt6.QtWidgets.QMenu` uses this to "raise" the menu above the surrounding screen. :sip:ref:`~PyQt6.QtWidgets.QProgressBar` has a "sunken" look. :sip:ref:`~PyQt6.QtWidgets.QLabel` has a flat look. The frames of widgets like these can be changed.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qframe.py
    :lines: 54-59

The :sip:ref:`~PyQt6.QtWidgets.QFrame` class can also be used directly for creating simple placeholder frames without any contents.

The frame style is specified by a :sip:ref:`~PyQt6.QtWidgets.QFrame.Shape` and a :sip:ref:`~PyQt6.QtWidgets.QFrame.Shadow` that is used to visually separate the frame from surrounding widgets. These properties can be set together using the :sip:ref:`~PyQt6.QtWidgets.QFrame.setFrameStyle` function and read with :sip:ref:`~PyQt6.QtWidgets.QFrame.frameStyle`.

The frame shapes are :sip:ref:`~PyQt6.QtWidgets.QFrame.Shape.NoFrame`, :sip:ref:`~PyQt6.QtWidgets.QFrame.Shape.Box`, :sip:ref:`~PyQt6.QtWidgets.QFrame.Shape.Panel`, :sip:ref:`~PyQt6.QtWidgets.QFrame.Shape.StyledPanel`, :sip:ref:`~PyQt6.QtWidgets.QFrame.Shape.HLine` and :sip:ref:`~PyQt6.QtWidgets.QFrame.Shape.VLine`; the shadow styles are :sip:ref:`~PyQt6.QtWidgets.QFrame.Shadow.Plain`, :sip:ref:`~PyQt6.QtWidgets.QFrame.Shadow.Raised` and :sip:ref:`~PyQt6.QtWidgets.QFrame.Shadow.Sunken`.

A frame widget has three attributes that describe the thickness of the border: :sip:ref:`~PyQt6.QtWidgets.QFrame.lineWidth`, :sip:ref:`~PyQt6.QtWidgets.QFrame.midLineWidth`, and :sip:ref:`~PyQt6.QtWidgets.QFrame.frameWidth`.

* The line width is the width of the frame border. It can be modified to customize the frame's appearance.

* The mid-line width specifies the width of an extra line in the middle of the frame, which uses a third color to obtain a special 3D effect. Notice that a mid-line is only drawn for :sip:ref:`~PyQt6.QtWidgets.QFrame.Shape.Box`, :sip:ref:`~PyQt6.QtWidgets.QFrame.Shape.HLine` and :sip:ref:`~PyQt6.QtWidgets.QFrame.Shape.VLine` frames that are raised or sunken.

* The frame width is determined by the frame style, and the :sip:ref:`~PyQt6.QtWidgets.QFrame.frameWidth` function is used to obtain the value defined for the style used.

The margin between the frame and the contents of the frame can be customized with the :sip:ref:`~PyQt6.QtWidgets.QWidget.setContentsMargins` function.

.. _qframe-picture:

This table shows some of the combinations of styles and line widths:

.. image:: ../../../images/frames.png
