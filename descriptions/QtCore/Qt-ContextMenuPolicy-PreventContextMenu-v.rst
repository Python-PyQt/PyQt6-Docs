.. sip:enum-member-description::
    :status: todo
    :value: 4
    :digest: f5d5308d12a6704ff1aa04f1952f21c4

the widget does not feature a context menu, and in contrast to ``NoContextMenu``, the handling is *not* deferred to the widget's parent. This means that all right mouse button events are guaranteed to be delivered to the widget itself through QWidget::mousePressEvent(), and QWidget::mouseReleaseEvent().
