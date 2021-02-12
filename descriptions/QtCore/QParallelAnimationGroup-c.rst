.. sip:class-description::
    :status: todo
    :brief: Parallel group of animations
    :digest: 67d8bb2efc5d3b0445d3ee5c1171a7ae

The :sip:ref:`~PyQt6.QtCore.QParallelAnimationGroup` class provides a parallel group of animations.

:sip:ref:`~PyQt6.QtCore.QParallelAnimationGroup`--a :sip:ref:`~PyQt6.QtCore.QAnimationGroup`--starts all its animations when it is :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.start` itself, i.e., runs all animations in parallel. The animation group finishes when the longest lasting animation has finished.

You can treat :sip:ref:`~PyQt6.QtCore.QParallelAnimationGroup` as any other :sip:ref:`~PyQt6.QtCore.QAbstractAnimation`, e.g., pause, resume, or add it to other animation groups.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_animation_qparallelanimationgroup.py
    :lines: 54-58

In this example, ``anim1`` and ``anim2`` are two :sip:ref:`~PyQt6.QtCore.QPropertyAnimation`\ s that have already been set up.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAnimationGroup`, :sip:ref:`~PyQt6.QtCore.QPropertyAnimation`, `The Animation Framework <https://doc.qt.io/qt-6/animation-overview.html>`_.
