.. sip:method-description::
    :status: todo
    :pysig: 69ba8ddc31689cc6e382e65bd55d95af
    :realsig: (QPainter*, const QRect&, int, const QPalette&, bool, const QString&, QPalette::ColorRole) const
    :digest: c406263a2f4256e9551beb31b4907ec4

Draws the given *text* in the specified *rectangle* using the provided *painter* and *palette*.

The text is drawn using the painter's pen, and aligned and wrapped according to the specified *alignment*. If an explicit *textRole* is specified, the text is drawn using the *palette*'s color for the given role. The *enabled* parameter indicates whether or not the item is enabled; when reimplementing this function, the *enabled* parameter should influence how the item is drawn.

.. seealso:: Qt::Alignment, :sip:ref:`~PyQt6.QtWidgets.QStyle.drawItemPixmap`.
