.. sip:method-description::
    :status: todo
    :pysig: a81259cef8e959c624df1d456e5d3297
    :realsig: ()
    :digest: a977b9059639d5455ed0235bc273583c

Undoes the last :sip:ref:`~PyQt6.QtGui.QGuiApplication.setOverrideCursor`.

If :sip:ref:`~PyQt6.QtGui.QGuiApplication.setOverrideCursor` has been called twice, calling  will activate the first cursor set. Calling this function a second time restores the original widgets' cursors.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.setOverrideCursor`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.overrideCursor`.
