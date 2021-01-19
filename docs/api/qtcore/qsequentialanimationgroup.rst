:orphan:

.. sip:class:: PyQt6.QtCore.QSequentialAnimationGroup
    :inherits: :sip:ref:`~PyQt6.QtCore.QAnimationGroup`
    :description: QtCore/QSequentialAnimationGroup-c.rst

    .. sip:method:: PyQt6.QtCore.QSequentialAnimationGroup.__init__
        :args:
            parent: :sip:ref:`~PyQt6.QtCore.QObject` = None
        :description: QtCore/QSequentialAnimationGroup-__init__-f.rst

    .. sip:method:: PyQt6.QtCore.QSequentialAnimationGroup.addPause
        :args:
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPauseAnimation`
        :description: QtCore/QSequentialAnimationGroup-addPause-f.rst

    .. sip:method:: PyQt6.QtCore.QSequentialAnimationGroup.currentAnimation
        :returns:
            :sip:ref:`~PyQt6.QtCore.QAbstractAnimation`
        :description: QtCore/QSequentialAnimationGroup-currentAnimation-f.rst

    .. sip:method:: PyQt6.QtCore.QSequentialAnimationGroup.duration
        :returns:
            int
        :description: QtCore/QSequentialAnimationGroup-duration-f.rst

    .. sip:method:: PyQt6.QtCore.QSequentialAnimationGroup.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtCore/QSequentialAnimationGroup-event-f.rst

    .. sip:method:: PyQt6.QtCore.QSequentialAnimationGroup.insertPause
        :args:
            int
            int
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPauseAnimation`
        :description: QtCore/QSequentialAnimationGroup-insertPause-f.rst

    .. sip:method:: PyQt6.QtCore.QSequentialAnimationGroup.updateCurrentTime
        :args:
            int
        :description: QtCore/QSequentialAnimationGroup-updateCurrentTime-f.rst

    .. sip:method:: PyQt6.QtCore.QSequentialAnimationGroup.updateDirection
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.Direction`
        :description: QtCore/QSequentialAnimationGroup-updateDirection-f.rst

    .. sip:method:: PyQt6.QtCore.QSequentialAnimationGroup.updateState
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.State`
            :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.State`
        :description: QtCore/QSequentialAnimationGroup-updateState-f.rst

    .. sip:signal:: PyQt6.QtCore.QSequentialAnimationGroup.currentAnimationChanged
        :args:
            :sip:ref:`~PyQt6.QtCore.QAbstractAnimation`
        :description: QtCore/QSequentialAnimationGroup-currentAnimationChanged-s.rst
