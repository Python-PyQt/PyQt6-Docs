.. sip:class-description::
    :status: todo
    :brief: Provides storage for the sort types to be used
    :realname: Qt3DRender::QSortPolicy
    :digest: b495c2a20987bd7a1e3fe900759c6e1c

Provides storage for the sort types to be used.

A :sip:ref:`~PyQt6.Qt3DRender.QSortPolicy` class stores the sorting type used by the FrameGraph. The sort types determine how drawable entities are sorted before drawing to determine the drawing order. When :sip:ref:`~PyQt6.Qt3DRender.QSortPolicy` is present in the FrameGraph, the sorting mechanism is determined by the :sip:ref:`~PyQt6.Qt3DRender.QSortPolicy.sortTypes` list. Multiple sort types can be used simultaneously. If :sip:ref:`~PyQt6.Qt3DRender.QSortPolicy` is not present in the FrameGraph, entities are drawn in the order they appear in the entity hierarchy.
