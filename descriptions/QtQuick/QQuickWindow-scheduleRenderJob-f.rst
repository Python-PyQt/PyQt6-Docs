.. sip:method-description::
    :status: todo
    :pysig: 236020f4961db80f223dcd9a28b2f27f
    :realsig: (QRunnable*,QQuickWindow::RenderStage)
    :digest: aaa077f02d4dff3846842a2bd29764f6

Schedules *job* to run when the rendering of this window reaches the given *stage*.

This is a convenience to the equivalent signals in :sip:ref:`~PyQt6.QtQuick.QQuickWindow` for "one shot" tasks.

The window takes ownership over *job* and will delete it when the job is completed.

If rendering is shut down before *job* has a chance to run, the job will be run and then deleted as part of the scene graph cleanup. If the window is never shown and no rendering happens before the :sip:ref:`~PyQt6.QtQuick.QQuickWindow` is destroyed, all pending jobs will be destroyed without their run() method being called.

If the rendering is happening on a different thread, then the job will happen on the rendering thread.

If *stage* is :sip:ref:`~PyQt6.QtQuick.QQuickWindow.RenderStage.NoStage`, *job* will be run at the earliest opportunity whenever the render thread is not busy rendering a frame. If the window is not exposed, and is not renderable, at the time the job is either posted or handled, the job is deleted without executing the run() method. If a non-threaded renderer is in use, the run() method of the job is executed synchronously. When rendering with OpenGL, the OpenGL context is changed to the renderer's context before executing any job, including :sip:ref:`~PyQt6.QtQuick.QQuickWindow.RenderStage.NoStage` jobs.

**Note:** This function does not trigger rendering; the jobs targeting any other stage than :sip:ref:`~PyQt6.QtQuick.QQuickWindow.RenderStage.NoStage` will be stored run until rendering is triggered elsewhere. To force the job to run earlier, call :sip:ref:`~PyQt6.QtQuick.QQuickWindow.update`;

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QQuickWindow.beforeRendering`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.afterRendering`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.beforeSynchronizing`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.afterSynchronizing`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.frameSwapped`, :sip:ref:`~PyQt6.QtQuick.QQuickWindow.sceneGraphInvalidated`.
