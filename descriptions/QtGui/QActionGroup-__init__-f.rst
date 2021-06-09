.. sip:method-description::
    :status: todo
    :pysig: 2b9057d9b4a06375acf76e6922f506e2
    :realsig: (QObject*)
    :digest: 63de9287fe01d870e33ada511ab13c2a

Constructs an action group for the *parent* object.

The action group is exclusive by default. Call :sip:ref:`~PyQt6.QtGui.QActionGroup.setExclusive`\ (false) to make the action group non-exclusive. To make the group exclusive but allow unchecking the active action call instead :sip:ref:`~PyQt6.QtGui.QActionGroup.setExclusionPolicy`\ (\ :sip:ref:`~PyQt6.QtGui.QActionGroup.ExclusionPolicy.ExclusiveOptional`)
