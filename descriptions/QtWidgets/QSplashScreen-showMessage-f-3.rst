.. sip:method-description::
    :status: todo
    :pysig: 02c947721ecaa1425d3a1533bee22bb4
    :realsig: (const QString&, int, const QColor&)
    :digest: b568875aa775ce7f43167366cd7d8428

Draws the *message* text onto the splash screen with color *color* and aligns the text according to the flags in *alignment*. This function calls :sip:ref:`~PyQt6.QtWidgets.QSplashScreen.repaint` to make sure the splash screen is repainted immediately. As a result the message is kept up to date with what your application is doing (e.g. loading files).

.. seealso:: Qt::Alignment, :sip:ref:`~PyQt6.QtWidgets.QSplashScreen.clearMessage`, :sip:ref:`~PyQt6.QtWidgets.QSplashScreen.message`.
