.. sip:class-description::
    :status: todo
    :brief: Abstract base class for groups of animations
    :digest: bb5b62a04619946bb73f3f09af8b7b10

The :sip:ref:`~PyQt6.QtCore.QAnimationGroup` class is an abstract base class for groups of animations.

An animation group is a container for animations (subclasses of :sip:ref:`~PyQt6.QtCore.QAbstractAnimation`). A group is usually responsible for managing the :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.State` of its animations, i.e., it decides when to start, stop, resume, and pause them. Currently, Qt provides two such groups: :sip:ref:`~PyQt6.QtCore.QParallelAnimationGroup` and :sip:ref:`~PyQt6.QtCore.QSequentialAnimationGroup`. Look up their class descriptions for details.

Since :sip:ref:`~PyQt6.QtCore.QAnimationGroup` inherits from :sip:ref:`~PyQt6.QtCore.QAbstractAnimation`, you can combine groups, and easily construct complex animation graphs. You can query :sip:ref:`~PyQt6.QtCore.QAbstractAnimation` for the group it belongs to (using the :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.group` function).

To start a top-level animation group, you simply use the :sip:ref:`~PyQt6.QtCore.QAbstractAnimation.start` function from :sip:ref:`~PyQt6.QtCore.QAbstractAnimation`. By a top-level animation group, we think of a group that itself is not contained within another group. Starting sub groups directly is not supported, and may lead to unexpected behavior.

:sip:ref:`~PyQt6.QtCore.QAnimationGroup` provides methods for adding and retrieving animations. Besides that, you can remove animations by calling :sip:ref:`~PyQt6.QtCore.QAnimationGroup.removeAnimation`, and clear the animation group by calling :sip:ref:`~PyQt6.QtCore.QAnimationGroup.clear`. You may keep track of changes in the group's animations by listening to :sip:ref:`~PyQt6.QtCore.QEvent.Type.ChildAdded` and :sip:ref:`~PyQt6.QtCore.QEvent.Type.ChildRemoved` events.

:sip:ref:`~PyQt6.QtCore.QAnimationGroup` takes ownership of the animations it manages, and ensures that they are deleted when the animation group is deleted.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractAnimation`, :sip:ref:`~PyQt6.QtCore.QVariantAnimation`, `The Animation Framework <https://doc.qt.io/qt-6/animation-overview.html>`_.
