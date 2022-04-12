.. sip:class-description::
    :status: todo
    :brief: Vertical or horizontal slider
    :digest: 3affc082b0291bd6ef634c893a9b8ba1

The :sip:ref:`~PyQt6.QtWidgets.QSlider` widget provides a vertical or horizontal slider.

.. image:: ../../../images/windows-slider.png

The slider is the classic widget for controlling a bounded value. It lets the user move a slider handle along a horizontal or vertical groove and translates the handle's position into an integer value within the legal range.

:sip:ref:`~PyQt6.QtWidgets.QSlider` has very few of its own functions; most of the functionality is in :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider`. The most useful functions are setValue() to set the slider directly to some value; triggerAction() to simulate the effects of clicking (useful for shortcut keys); setSingleStep(), setPageStep() to set the steps; and setMinimum() and setMaximum() to define the range of the scroll bar.

:sip:ref:`~PyQt6.QtWidgets.QSlider` provides methods for controlling tickmarks. You can use :sip:ref:`~PyQt6.QtWidgets.QSlider.setTickPosition` to indicate where you want the tickmarks to be, :sip:ref:`~PyQt6.QtWidgets.QSlider.setTickInterval` to indicate how many of them you want. the currently set tick position and interval can be queried using the :sip:ref:`~PyQt6.QtWidgets.QSlider.tickPosition` and :sip:ref:`~PyQt6.QtWidgets.QSlider.tickInterval` functions, respectively.

:sip:ref:`~PyQt6.QtWidgets.QSlider` inherits a comprehensive set of signals:

+------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Signal           | Description                                                                                                                    |
+==================+================================================================================================================================+
| valueChanged()   | Emitted when the slider's value has changed. The tracking() determines whether this signal is emitted during user interaction. |
+------------------+--------------------------------------------------------------------------------------------------------------------------------+
| sliderPressed()  | Emitted when the user starts to drag the slider.                                                                               |
+------------------+--------------------------------------------------------------------------------------------------------------------------------+
| sliderMoved()    | Emitted when the user drags the slider.                                                                                        |
+------------------+--------------------------------------------------------------------------------------------------------------------------------+
| sliderReleased() | Emitted when the user releases the slider.                                                                                     |
+------------------+--------------------------------------------------------------------------------------------------------------------------------+

:sip:ref:`~PyQt6.QtWidgets.QSlider` only provides integer ranges. Note that although :sip:ref:`~PyQt6.QtWidgets.QSlider` handles very large numbers, it becomes difficult for users to use a slider accurately for very large ranges.

A slider accepts focus on Tab and provides both a mouse wheel and a keyboard interface. The keyboard interface is the following:

* Left/Right move a horizontal slider by one single step.

* Up/Down move a vertical slider by one single step.

* PageUp moves up one page.

* PageDown moves down one page.

* Home moves to the start (minimum).

* End moves to the end (maximum).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QScrollBar`, :sip:ref:`~PyQt6.QtWidgets.QSpinBox`, :sip:ref:`~PyQt6.QtWidgets.QDial`, `GUI Design Handbook: Slider <https://doc.qt.io/qt-6/guibooks.html#fowler>`_, `Sliders Example <https://doc.qt.io/qt-6/qtwidgets-widgets-sliders-example.html>`_.
