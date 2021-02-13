.. sip:enum-member-description::
    :status: todo
    :value: 0x00010000
    :realname: QPaintEngine::PaintEngineFeature::ObjectBoundingModeGradients
    :digest: 9c421cf8c89d3e1b47fe46d203680a6e

The engine has native support for gradients with coordinate mode :sip:ref:`~PyQt6.QtGui.QGradient.CoordinateMode.ObjectBoundingMode`. Otherwise, if  is supported, object bounding mode gradients are converted to gradients with coordinate mode :sip:ref:`~PyQt6.QtGui.QGradient.CoordinateMode.LogicalMode` and a brush transform for the coordinate mapping.
