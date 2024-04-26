.. sip:class-description::
    :status: todo
    :brief: Encapsulates the rendering of pages of a PDF document
    :digest: 4d433e99047dca23aa6c171ab32d52e8

The :sip:ref:`~PyQt6.QtPdf.QPdfPageRenderer` class encapsulates the rendering of pages of a PDF document.

The :sip:ref:`~PyQt6.QtPdf.QPdfPageRenderer` contains a queue that collects all render requests that are invoked through :sip:ref:`~PyQt6.QtPdf.QPdfPageRenderer.requestPage`. Depending on the configured :sip:ref:`~PyQt6.QtPdf.QPdfPageRenderer.RenderMode.RenderMode` the :sip:ref:`~PyQt6.QtPdf.QPdfPageRenderer` processes this queue in the main UI thread on next event loop invocation (``RenderMode::SingleThreaded``) or in a separate worker thread (``RenderMode::MultiThreaded``) and emits the result through the pageRendered() signal for each request once the rendering is done.

.. seealso:: :sip:ref:`~PyQt6.QtPdf.QPdfDocument`.
