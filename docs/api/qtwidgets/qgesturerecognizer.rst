:orphan:

.. sip:class:: PyQt6.QtWidgets.QGestureRecognizer
    :description: QtWidgets/QGestureRecognizer-c.rst

    .. sip:enum:: PyQt6.QtWidgets.QGestureRecognizer.ResultFlag
        :description: QtWidgets/QGestureRecognizer-ResultFlag-e.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QGestureRecognizer.ResultFlag.CancelGesture
            :description: QtWidgets/QGestureRecognizer-ResultFlag-CancelGesture-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QGestureRecognizer.ResultFlag.ConsumeEventHint
            :description: QtWidgets/QGestureRecognizer-ResultFlag-ConsumeEventHint-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QGestureRecognizer.ResultFlag.FinishGesture
            :description: QtWidgets/QGestureRecognizer-ResultFlag-FinishGesture-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QGestureRecognizer.ResultFlag.Ignore
            :description: QtWidgets/QGestureRecognizer-ResultFlag-Ignore-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QGestureRecognizer.ResultFlag.MayBeGesture
            :description: QtWidgets/QGestureRecognizer-ResultFlag-MayBeGesture-v.rst

        .. sip:enum-member:: PyQt6.QtWidgets.QGestureRecognizer.ResultFlag.TriggerGesture
            :description: QtWidgets/QGestureRecognizer-ResultFlag-TriggerGesture-v.rst

    .. sip:method:: PyQt6.QtWidgets.QGestureRecognizer.__init__
        :description: QtWidgets/QGestureRecognizer-__init__-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGestureRecognizer.__init__
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGestureRecognizer`
        :description: QtWidgets/QGestureRecognizer-__init__-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QGestureRecognizer.create
        :args:
            :sip:ref:`~PyQt6.QtCore.QObject`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QGesture`
        :description: QtWidgets/QGestureRecognizer-create-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGestureRecognizer.recognize
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGesture`
            :sip:ref:`~PyQt6.QtCore.QObject`
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            :sip:ref:`~PyQt6.QtWidgets.QGestureRecognizer.ResultFlag`
        :description: QtWidgets/QGestureRecognizer-recognize-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QGestureRecognizer.registerRecognizer
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGestureRecognizer`
        :returns:
            int
        :static:
        :description: QtWidgets/QGestureRecognizer-registerRecognizer-f-1.rst

    .. sip:method:: PyQt6.QtWidgets.QGestureRecognizer.reset
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QGesture`
        :description: QtWidgets/QGestureRecognizer-reset-f.rst

    .. sip:method:: PyQt6.QtWidgets.QGestureRecognizer.unregisterRecognizer
        :args:
            int
        :static:
        :description: QtWidgets/QGestureRecognizer-unregisterRecognizer-f-1.rst
