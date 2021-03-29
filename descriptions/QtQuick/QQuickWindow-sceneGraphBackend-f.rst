.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: ()
    :digest: 0a6e9dc67355de2e68a32133483ef824

Returns the requested Qt Quick scenegraph backend.

**Note:** The return value of this function may still be outdated by subsequent calls to :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setSceneGraphBackend` until the first :sip:ref:`~PyQt6.QtQuick.QQuickWindow` in the application has been constructed.

**Note:** The value only reflects the request in the ``QT_QUICK_BACKEND`` environment variable after a :sip:ref:`~PyQt6.QtQuick.QQuickWindow` has been constructed.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.setSceneGraphBackend`.
