.. sip:method-description::
    :status: todo
    :pysig: c7970e5b7fe96858a6e9e37ea638819f
    :realsig: (QObject*,QJSEngine::ObjectOwnership)
    :digest: 0459aa43f87fb7ba49eed6ee3f836079

Sets the *ownership* of *object*.

An object with ``JavaScriptOwnership`` is not garbage collected as long as it still has a parent, even if there are no references to it.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QJSEngine.objectOwnership`, :sip:ref:`~PyQt6.QtQml.QJSEngine.ObjectOwnership`.
