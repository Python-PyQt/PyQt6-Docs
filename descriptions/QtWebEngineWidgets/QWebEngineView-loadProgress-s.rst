.. sip:signal-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: ac7dc4e2c340acbeb2942c53814a7f83

This signal is emitted every time an element in the web view completes loading, such as an embedded image or a script. Therefore, it tracks the collective progress of loading the web view.

The current value is provided by *progress* and scales from 0 to 100, which is the default range of :sip:ref:`~PyQt6.QtWidgets.QProgressBar`.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.loadStarted`, :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.loadFinished`.
