.. sip:method-description::
    :status: todo
    :pysig: 355cfff1ee7088f98f22de9e16b9f94b
    :realsig: (const QRectF&,Qt::AspectRatioMode)
    :digest: 60a49c9d9ac2e91bd34bbaf01c102abd

Scales the view matrix and scrolls the scroll bars to ensure that the scene rectangle *rect* fits inside the viewport. *rect* must be inside the scene rect; otherwise, fitInView() cannot guarantee that the whole rect is visible.

This function keeps the view's rotation, translation, or shear. The view is scaled according to *aspectRatioMode*. *rect* will be centered in the view if it does not fit tightly.

It's common to call fitInView() from inside a reimplementation of :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.resizeEvent`, to ensure that the whole scene, or parts of the scene, scales automatically to fit the new size of the viewport as the view is resized. Note though, that calling fitInView() from inside :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.resizeEvent` can lead to unwanted resize recursion, if the new transformation toggles the automatic state of the scrollbars. You can toggle the scrollbar policies to always on or always off to prevent this (see horizontalScrollBarPolicy() and verticalScrollBarPolicy()).

If *rect* is empty, or if the viewport is too small, this function will do nothing.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.setTransform`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.ensureVisible`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsView.centerOn`.
