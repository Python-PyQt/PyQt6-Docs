.. sip:method-description::
    :status: todo
    :pysig: 12fa34a8fc679aa7d3a01c75261459cc
    :realsig: (int,QAbstractAnimation*)
    :digest: a464352cb73d410464a7332d3148e0fe

Inserts *animation* into this animation group at *index*. If *index* is 0 the animation is inserted at the beginning. If *index* is :sip:ref:`~PyQt6.QtCore.QAnimationGroup.animationCount`, the animation is inserted at the end.

**Note:** The group takes ownership of the animation.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAnimationGroup.takeAnimation`, :sip:ref:`~PyQt6.QtCore.QAnimationGroup.addAnimation`, :sip:ref:`~PyQt6.QtCore.QAnimationGroup.indexOfAnimation`, :sip:ref:`~PyQt6.QtCore.QAnimationGroup.removeAnimation`.
