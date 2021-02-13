.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: 5dcfaac53552a606a9f6e3f13cac4b7f

Caching is enabled for the item's logical (local) coordinate system. :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem` creates an off-screen pixel buffer with a configurable size / resolution that you can pass to :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setCacheMode`. Rendering quality will typically degrade, depending on the resolution of the cache and the item transformation. The first time the item is redrawn, it will render itself into the cache, and the cache is then reused for every subsequent expose. The cache is also reused as the item is transformed. To adjust the resolution of the cache, you can call :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setCacheMode` again.
