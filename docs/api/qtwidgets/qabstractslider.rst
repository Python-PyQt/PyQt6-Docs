:orphan:

.. sip:class:: PyQt6.QtWidgets.QAbstractSlider
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QWidget`
    :description: QtWidgets/QAbstractSlider-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QAbstractSlider.SliderAction
        :description: QtWidgets/QAbstractSlider-SliderAction-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QAbstractSlider.SliderAction.SliderMove
            :description: QtWidgets/QAbstractSlider-SliderAction-SliderMove-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QAbstractSlider.SliderAction.SliderNoAction
            :description: QtWidgets/QAbstractSlider-SliderAction-SliderNoAction-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QAbstractSlider.SliderAction.SliderPageStepAdd
            :description: QtWidgets/QAbstractSlider-SliderAction-SliderPageStepAdd-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QAbstractSlider.SliderAction.SliderPageStepSub
            :description: QtWidgets/QAbstractSlider-SliderAction-SliderPageStepSub-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QAbstractSlider.SliderAction.SliderSingleStepAdd
            :description: QtWidgets/QAbstractSlider-SliderAction-SliderSingleStepAdd-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QAbstractSlider.SliderAction.SliderSingleStepSub
            :description: QtWidgets/QAbstractSlider-SliderAction-SliderSingleStepSub-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QAbstractSlider.SliderAction.SliderToMaximum
            :description: QtWidgets/QAbstractSlider-SliderAction-SliderToMaximum-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QAbstractSlider.SliderAction.SliderToMinimum
            :description: QtWidgets/QAbstractSlider-SliderAction-SliderToMinimum-v.rst

    .. sip:enum:: PyQt6.QtWidgets.QAbstractSlider.SliderChange
        :description: QtWidgets/QAbstractSlider-SliderChange-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QAbstractSlider.SliderChange.SliderOrientationChange
            :description: QtWidgets/QAbstractSlider-SliderChange-SliderOrientationChange-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QAbstractSlider.SliderChange.SliderRangeChange
            :description: QtWidgets/QAbstractSlider-SliderChange-SliderRangeChange-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QAbstractSlider.SliderChange.SliderStepsChange
            :description: QtWidgets/QAbstractSlider-SliderChange-SliderStepsChange-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QAbstractSlider.SliderChange.SliderValueChange
            :description: QtWidgets/QAbstractSlider-SliderChange-SliderValueChange-v.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtWidgets.QWidget` = None
        :description: QtWidgets/QAbstractSlider-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.changeEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :description: QtWidgets/QAbstractSlider-changeEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QAbstractSlider-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.hasTracking
        :returns:
            bool
        :description: QtWidgets/QAbstractSlider-hasTracking-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.invertedAppearance
        :returns:
            bool
        :description: QtWidgets/QAbstractSlider-invertedAppearance-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.invertedControls
        :returns:
            bool
        :description: QtWidgets/QAbstractSlider-invertedControls-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.isSliderDown
        :returns:
            bool
        :description: QtWidgets/QAbstractSlider-isSliderDown-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.keyPressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QKeyEvent`
        :description: QtWidgets/QAbstractSlider-keyPressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.maximum
        :returns:
            int
        :description: QtWidgets/QAbstractSlider-maximum-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.minimum
        :returns:
            int
        :description: QtWidgets/QAbstractSlider-minimum-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.orientation
        :returns:
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
        :description: QtWidgets/QAbstractSlider-orientation-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.pageStep
        :returns:
            int
        :description: QtWidgets/QAbstractSlider-pageStep-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.repeatAction
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.SliderAction`
        :description: QtWidgets/QAbstractSlider-repeatAction-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.setInvertedAppearance
        :args:
            bool
        :description: QtWidgets/QAbstractSlider-setInvertedAppearance-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.setInvertedControls
        :args:
            bool
        :description: QtWidgets/QAbstractSlider-setInvertedControls-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.setMaximum
        :args:
            int
        :description: QtWidgets/QAbstractSlider-setMaximum-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.setMinimum
        :args:
            int
        :description: QtWidgets/QAbstractSlider-setMinimum-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.setOrientation
        :args:
            :sip:ref:`~PyQt6.QtCore.Qt.Orientation`
        :description: QtWidgets/QAbstractSlider-setOrientation-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.setPageStep
        :args:
            int
        :description: QtWidgets/QAbstractSlider-setPageStep-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.setRange
        :args:
            int
            int
        :description: QtWidgets/QAbstractSlider-setRange-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.setRepeatAction
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.SliderAction`
            thresholdTime: int = 500
            repeatTime: int = 50
        :description: QtWidgets/QAbstractSlider-setRepeatAction-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.setSingleStep
        :args:
            int
        :description: QtWidgets/QAbstractSlider-setSingleStep-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.setSliderDown
        :args:
            bool
        :description: QtWidgets/QAbstractSlider-setSliderDown-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.setSliderPosition
        :args:
            int
        :description: QtWidgets/QAbstractSlider-setSliderPosition-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.setTracking
        :args:
            bool
        :description: QtWidgets/QAbstractSlider-setTracking-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.setValue
        :args:
            int
        :description: QtWidgets/QAbstractSlider-setValue-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.singleStep
        :returns:
            int
        :description: QtWidgets/QAbstractSlider-singleStep-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.sliderChange
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.SliderChange`
        :description: QtWidgets/QAbstractSlider-sliderChange-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.sliderPosition
        :returns:
            int
        :description: QtWidgets/QAbstractSlider-sliderPosition-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.timerEvent
        :args:
            :sip:ref:`~PyQt6.QtCore.QTimerEvent`
        :description: QtWidgets/QAbstractSlider-timerEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.triggerAction
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QAbstractSlider.SliderAction`
        :description: QtWidgets/QAbstractSlider-triggerAction-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.value
        :returns:
            int
        :description: QtWidgets/QAbstractSlider-value-f.rst

    .. sip:method:: PyQt6.QtWidgets.QAbstractSlider.wheelEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QWheelEvent`
        :description: QtWidgets/QAbstractSlider-wheelEvent-f.rst

    .. sip:signal:: PyQt6.QtWidgets.QAbstractSlider.actionTriggered
        :args:
            int
        :description: QtWidgets/QAbstractSlider-actionTriggered-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QAbstractSlider.rangeChanged
        :args:
            int
            int
        :description: QtWidgets/QAbstractSlider-rangeChanged-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QAbstractSlider.sliderMoved
        :args:
            int
        :description: QtWidgets/QAbstractSlider-sliderMoved-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QAbstractSlider.sliderPressed
        :description: QtWidgets/QAbstractSlider-sliderPressed-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QAbstractSlider.sliderReleased
        :description: QtWidgets/QAbstractSlider-sliderReleased-s.rst

    .. sip:signal:: PyQt6.QtWidgets.QAbstractSlider.valueChanged
        :args:
            int
        :description: QtWidgets/QAbstractSlider-valueChanged-s.rst
