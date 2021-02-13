.. sip:class-description::
    :status: todo
    :brief: Vertical or horizontal scroll bar
    :digest: 9d10ebbe40b283aa210f77fcd9a6e8d2

The :sip:ref:`~PyQt6.QtWidgets.QScrollBar` widget provides a vertical or horizontal scroll bar.

A scroll bar is a control that enables the user to access parts of a document that is larger than the widget used to display it. It provides a visual indication of the user's current position within the document and the amount of the document that is visible. Scroll bars are usually equipped with other controls that enable more accurate navigation. Qt displays scroll bars in a way that is appropriate for each platform.

If you need to provide a scrolling view onto another widget, it may be more convenient to use the :sip:ref:`~PyQt6.QtWidgets.QScrollArea` class because this provides a viewport widget and scroll bars. :sip:ref:`~PyQt6.QtWidgets.QScrollBar` is useful if you need to implement similar functionality for specialized widgets using :sip:ref:`~PyQt6.QtWidgets.QAbstractScrollArea`; for example, if you decide to subclass :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView`. For most other situations where a slider control is used to obtain a value within a given range, the :sip:ref:`~PyQt6.QtWidgets.QSlider` class may be more appropriate for your needs.

+---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| .. image:: ../../../images/qscrollbar-picture.png | Scroll bars typically include four separate controls: a slider, scroll arrows, and a page control.                                                                                                                                                                                                                                                                                                                |
|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                   | * a. The slider provides a way to quickly go to any part of the document, but does not support accurate navigation within large documents.                                                                                                                                                                                                                                                                        |
|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                   | * b. The scroll arrows are push buttons which can be used to accurately navigate to a particular place in a document. For a vertical scroll bar connected to a text editor, these typically move the current position one "line" up or down, and adjust the position of the slider by a small amount. In editors and list boxes a "line" might mean one line of text; in an image viewer it might mean 20 pixels. |
|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                   | * c. The page control is the area over which the slider is dragged (the scroll bar's background). Clicking here moves the scroll bar towards the click by one "page". This value is usually the same as the length of the slider.                                                                                                                                                                                 |
+---------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Each scroll bar has a value that indicates how far the slider is from the start of the scroll bar; this is obtained with value() and set with setValue(). This value always lies within the range of values defined for the scroll bar, from :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.minimum` to :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.minimum` inclusive. The range of acceptable values can be set with setMinimum() and setMaximum(). At the minimum value, the top edge of the slider (for a vertical scroll bar) or left edge (for a horizontal scroll bar) will be at the top (or left) end of the scroll bar. At the maximum value, the bottom (or right) edge of the slider will be at the bottom (or right) end of the scroll bar.

The length of the slider is usually related to the value of the page step, and typically represents the proportion of the document area shown in a scrolling view. The page step is the amount that the value changes by when the user presses the Page Up and Page Down keys, and is set with setPageStep(). Smaller changes to the value defined by the line step are made using the cursor keys, and this quantity is set with :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.setSingleStep`.

Note that the range of values used is independent of the actual size of the scroll bar widget. You do not need to take this into account when you choose values for the range and the page step.

The range of values specified for the scroll bar are often determined differently to those for a :sip:ref:`~PyQt6.QtWidgets.QSlider` because the length of the slider needs to be taken into account. If we have a document with 100 lines, and we can only show 20 lines in a widget, we may wish to construct a scroll bar with a page step of 20, a minimum value of 0, and a maximum value of 80. This would give us a scroll bar with five "pages".

+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image-qscrollbar-values-png| | The relationship between a document length, the range of values used in a scroll bar, and the page step is simple in many common situations. The scroll bar's range of values is determined by subtracting a chosen page step from some value representing the length of the document. In such cases, the following equation is useful: *document length* = maximum() - minimum() + pageStep(). |
+-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

:sip:ref:`~PyQt6.QtWidgets.QScrollBar` only provides integer ranges. Note that although :sip:ref:`~PyQt6.QtWidgets.QScrollBar` handles very large numbers, scroll bars on current screens cannot usefully represent ranges above about 100,000 pixels. Beyond that, it becomes difficult for the user to control the slider using either the keyboard or the mouse, and the scroll arrows will have limited use.

ScrollBar inherits a comprehensive set of signals from :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider`:

* :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.valueChanged` is emitted when the scroll bar's value has changed. The tracking() determines whether this signal is emitted during user interaction.

* :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.rangeChanged` is emitted when the scroll bar's range of values has changed.

* :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.sliderPressed` is emitted when the user starts to drag the slider.

* :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.sliderMoved` is emitted when the user drags the slider.

* :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.sliderReleased` is emitted when the user releases the slider.

* :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.actionTriggered` is emitted when the scroll bar is changed by user interaction or via the :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.triggerAction` function.

A scroll bar can be controlled by the keyboard, but it has a default focusPolicy() of :sip:ref:`~PyQt6.QtCore.Qt.FocusPolicy.NoFocus`. Use setFocusPolicy() to enable keyboard interaction with the scroll bar:

* Left/Right move a horizontal scroll bar by one single step.

* Up/Down move a vertical scroll bar by one single step.

* PageUp moves up one page.

* PageDown moves down one page.

* Home moves to the start (mininum).

* End moves to the end (maximum).

The slider itself can be controlled by using the :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.triggerAction` function to simulate user interaction with the scroll bar controls. This is useful if you have many different widgets that use a common range of values.

Most GUI styles use the pageStep() value to calculate the size of the slider.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QScrollArea`, :sip:ref:`~PyQt6.QtWidgets.QSlider`, :sip:ref:`~PyQt6.QtWidgets.QDial`, :sip:ref:`~PyQt6.QtWidgets.QSpinBox`, `GUI Design Handbook: Scroll Bar <https://doc.qt.io/qt-6/guibooks.html#fowler>`_, `Sliders Example <https://doc.qt.io/qt-6/qtwidgets-widgets-sliders-example.html>`_.

.. |image-qscrollbar-values-png| image:: ../../../images/qscrollbar-values.png
