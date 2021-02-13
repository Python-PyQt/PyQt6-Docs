.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 33a95ae1f3bab575f9ce76e4fa21a91b

This signal is emitted when the scene graph is updated, meaning that :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.polishItems` and :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.sync` needs to be called. If :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.sync` returns true, then :sip:ref:`~PyQt6.QtQuick.QQuickRenderControl.render` needs to be called.

**Note:** Avoid triggering polishing, synchronization and rendering directly when this signal is emitted. Instead, prefer deferring it by using a timer for example. This will lead to better performance.
