.. sip:enum-member-description::
    :status: todo
    :value: 3
    :digest: 1200bf2b4bb452f3cdc871bfd46688bc

:sip:ref:`~PyQt6.QtWidgets.QGraphicsView` will never update its viewport when the scene changes; the user is expected to control all updates. This mode disables all (potentially slow) item visibility testing in :sip:ref:`~PyQt6.QtWidgets.QGraphicsView`, and is suitable for scenes that either require a fixed frame rate, or where the viewport is otherwise updated externally.
