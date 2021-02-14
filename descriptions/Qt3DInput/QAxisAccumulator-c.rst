.. sip:class-description::
    :status: todo
    :brief: Processes velocity or acceleration data from a QAxis
    :realname: Qt3DInput::QAxisAccumulator
    :digest: fd0d7f9788ddcc7f481649c8bb3c1241

Constructs a new :sip:ref:`~PyQt6.Qt3DInput.QAxisAccumulator` instance with *parent*.

:sip:ref:`~PyQt6.Qt3DInput.QAxisAccumulator` processes velocity or acceleration data from a QAxis.

A :sip:ref:`~PyQt6.Qt3DInput.QAxis` reports the current position of an axis on an input device. When the axis is returned to its neutral position the value of that axis returns to 0. Often, it is required to have the input from an axis control a variable in other ways, for example treating the value from the :sip:ref:`~PyQt6.Qt3DInput.QAxis` as a velocity (first derivative with respect to time) or as an acceleration (second derivative with respect to time). This can be done with user code or with a :sip:ref:`~PyQt6.Qt3DLogic.QFrameAction` but those approached are not ideal as they add more work to the main thread and are inherently imperative. The :sip:ref:`~PyQt6.Qt3DInput.QAxisAccumulator` class allows for this common task to be performed on the Qt 3D backend and be specified in a declarative manner.
