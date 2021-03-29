.. sip:class-description::
    :status: todo
    :brief: Provides a way to have a synchronous function executed each frame
    :realname: Qt3DLogic::QFrameAction
    :digest: b197d39b44798a672b3b8450ca0080ba

Provides a way to have a synchronous function executed each frame.

The :sip:ref:`~PyQt6.Qt3DLogic.QFrameAction` provides a way to perform tasks each frame in a synchronized way with the Qt3D backend. This is useful to implement some aspects of application logic and to prototype functionality that can later be folded into an additional Qt3D aspect.

For example, the :sip:ref:`~PyQt6.Qt3DLogic.QFrameAction` can be used to animate a property in sync with the Qt3D engine where a Qt Quick animation element is not perfectly synchronized and may lead to stutters in some cases.

To execute your own code each frame connect to the QFrameAction::triggered signal.
