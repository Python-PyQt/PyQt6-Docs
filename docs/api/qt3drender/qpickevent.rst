:orphan:

.. sip:class:: PyQt6.Qt3DRender.QPickEvent
    :inherits: :sip:ref:`~PyQt6.QtCore.QObject`
    :description: Qt3DRender/QPickEvent-c.rst

    .. sip:enum:: PyQt6.Qt3DRender.QPickEvent.Buttons
        :description: Qt3DRender/QPickEvent-Buttons-e.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QPickEvent.Buttons.BackButton
            :description: Qt3DRender/QPickEvent-Buttons-BackButton-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QPickEvent.Buttons.LeftButton
            :description: Qt3DRender/QPickEvent-Buttons-LeftButton-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QPickEvent.Buttons.MiddleButton
            :description: Qt3DRender/QPickEvent-Buttons-MiddleButton-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QPickEvent.Buttons.NoButton
            :description: Qt3DRender/QPickEvent-Buttons-NoButton-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QPickEvent.Buttons.RightButton
            :description: Qt3DRender/QPickEvent-Buttons-RightButton-v.rst

    .. sip:enum:: PyQt6.Qt3DRender.QPickEvent.Modifiers
        :description: Qt3DRender/QPickEvent-Modifiers-e.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QPickEvent.Modifiers.AltModifier
            :description: Qt3DRender/QPickEvent-Modifiers-AltModifier-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QPickEvent.Modifiers.ControlModifier
            :description: Qt3DRender/QPickEvent-Modifiers-ControlModifier-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QPickEvent.Modifiers.KeypadModifier
            :description: Qt3DRender/QPickEvent-Modifiers-KeypadModifier-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QPickEvent.Modifiers.MetaModifier
            :description: Qt3DRender/QPickEvent-Modifiers-MetaModifier-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QPickEvent.Modifiers.NoModifier
            :description: Qt3DRender/QPickEvent-Modifiers-NoModifier-v.rst

        .. sip:enum-member:: PyQt6.Qt3DRender.QPickEvent.Modifiers.ShiftModifier
            :description: Qt3DRender/QPickEvent-Modifiers-ShiftModifier-v.rst

    .. sip:method:: PyQt6.Qt3DRender.QPickEvent.__init__
        :description: Qt3DRender/QPickEvent-__init__-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QPickEvent.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
            :sip:ref:`~PyQt6.QtGui.QVector3D`
            :sip:ref:`~PyQt6.QtGui.QVector3D`
            float
        :description: Qt3DRender/QPickEvent-__init__-f-1.rst

    .. sip:method:: PyQt6.Qt3DRender.QPickEvent.__init__
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
            :sip:ref:`~PyQt6.QtGui.QVector3D`
            :sip:ref:`~PyQt6.QtGui.QVector3D`
            float
            :sip:ref:`~PyQt6.Qt3DRender.QPickEvent.Buttons`
            int
            int
        :description: Qt3DRender/QPickEvent-__init__-f-2.rst

    .. sip:method:: PyQt6.Qt3DRender.QPickEvent.button
        :returns:
            :sip:ref:`~PyQt6.Qt3DRender.QPickEvent.Buttons`
        :description: Qt3DRender/QPickEvent-button-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QPickEvent.buttons
        :returns:
            int
        :description: Qt3DRender/QPickEvent-buttons-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QPickEvent.distance
        :returns:
            float
        :description: Qt3DRender/QPickEvent-distance-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QPickEvent.entity
        :returns:
            :sip:ref:`~PyQt6.Qt3DCore.QEntity`
        :description: Qt3DRender/QPickEvent-entity-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QPickEvent.isAccepted
        :returns:
            bool
        :description: Qt3DRender/QPickEvent-isAccepted-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QPickEvent.localIntersection
        :returns:
            :sip:ref:`~PyQt6.QtGui.QVector3D`
        :description: Qt3DRender/QPickEvent-localIntersection-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QPickEvent.modifiers
        :returns:
            int
        :description: Qt3DRender/QPickEvent-modifiers-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QPickEvent.position
        :returns:
            :sip:ref:`~PyQt6.QtCore.QPointF`
        :description: Qt3DRender/QPickEvent-position-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QPickEvent.setAccepted
        :args:
            bool
        :description: Qt3DRender/QPickEvent-setAccepted-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QPickEvent.viewport
        :returns:
            :sip:ref:`~PyQt6.Qt3DRender.QViewport`
        :description: Qt3DRender/QPickEvent-viewport-f.rst

    .. sip:method:: PyQt6.Qt3DRender.QPickEvent.worldIntersection
        :returns:
            :sip:ref:`~PyQt6.QtGui.QVector3D`
        :description: Qt3DRender/QPickEvent-worldIntersection-f.rst

    .. sip:signal:: PyQt6.Qt3DRender.QPickEvent.acceptedChanged
        :args:
            bool
        :description: Qt3DRender/QPickEvent-acceptedChanged-s.rst
