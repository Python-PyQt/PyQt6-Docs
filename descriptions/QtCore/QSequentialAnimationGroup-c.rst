.. sip:class-description::
    :status: todo
    :brief: Sequential group of animations
    :digest: 4f4ed80465467b5e42a2bed700de59b4

The :sip:ref:`~PyQt6.QtCore.QSequentialAnimationGroup` class provides a sequential group of animations.

:sip:ref:`~PyQt6.QtCore.QSequentialAnimationGroup` is a :sip:ref:`~PyQt6.QtCore.QAnimationGroup` that runs its animations in sequence, i.e., it starts one animation after another has finished playing. The animations are played in the order they are added to the group (using :sip:ref:`~PyQt6.QtCore.QAnimationGroup.addAnimation` or :sip:ref:`~PyQt6.QtCore.QAnimationGroup.insertAnimation`). The animation group finishes when its last animation has finished.

At each moment there is at most one animation that is active in the group; it is returned by :sip:ref:`~PyQt6.QtCore.QSequentialAnimationGroup.currentAnimation`. An empty group has no current animation.

A sequential animation group can be treated as any other animation, i.e., it can be started, stopped, and added to other groups. You can also call :sip:ref:`~PyQt6.QtCore.QSequentialAnimationGroup.addPause` or :sip:ref:`~PyQt6.QtCore.QSequentialAnimationGroup.insertPause` to add a pause to a sequential animation group.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_animation_qsequentialanimationgroup.py
    :lines: 54-59

In this example, ``anim1`` and ``anim2`` are two already set up :sip:ref:`~PyQt6.QtCore.QPropertyAnimation`\ s.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAnimationGroup`, :sip:ref:`~PyQt6.QtCore.QAbstractAnimation`, `The Animation Framework <https://doc.qt.io/qt-6/animation-overview.html>`_.
