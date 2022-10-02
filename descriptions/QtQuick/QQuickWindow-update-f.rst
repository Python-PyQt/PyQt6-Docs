.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: a8b46e13bae1264fc4408441d69b963d

Schedules the window to render another frame.

Calling QQuickWindow::update() differs from :sip:ref:`~PyQt6.QtQuick.QQuickItem.update` in that it always triggers a repaint, regardless of changes in the underlying scene graph or not.
