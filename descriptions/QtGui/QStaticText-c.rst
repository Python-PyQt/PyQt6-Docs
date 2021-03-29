.. sip:class-description::
    :status: todo
    :brief: Enables optimized drawing of text when the text and its layout is updated rarely
    :digest: ca0058e422bfcc42729dff3c13c0ac99

The :sip:ref:`~PyQt6.QtGui.QStaticText` class enables optimized drawing of text when the text and its layout is updated rarely.

:sip:ref:`~PyQt6.QtGui.QStaticText` provides a way to cache layout data for a block of text so that it can be drawn more efficiently than by using :sip:ref:`~PyQt6.QtGui.QPainter.drawText` in which the layout information is recalculated with every call.

The class primarily provides an optimization for cases where the text, its font and the transformations on the painter are static over several paint events. If the text or its layout is changed for every iteration, :sip:ref:`~PyQt6.QtGui.QPainter.drawText` is the more efficient alternative, since the static text's layout would have to be recalculated to take the new state into consideration.

Translating the painter will not cause the layout of the text to be recalculated, but will cause a very small performance impact on drawStaticText(). Altering any other parts of the painter's transformation or the painter's font will cause the layout of the static text to be recalculated. This should be avoided as often as possible to maximize the performance benefit of using :sip:ref:`~PyQt6.QtGui.QStaticText`.

In addition, only affine transformations are supported by drawStaticText(). Calling drawStaticText() on a projected painter will perform slightly worse than using the regular drawText() call, so this should be avoided.

::

    class MyWidget: public QWidget
    {
    public:
        MyWidget(QWidget *parent = nullptr) : QWidget(parent), m_staticText("This is static text")

    protected:
        void paintEvent(QPaintEvent *)
        {
            QPainter painter(this);
            painter.drawStaticText(0, 0, m_staticText);
        }

    private:
        QStaticText m_staticText;
    };

The :sip:ref:`~PyQt6.QtGui.QStaticText` class can be used to mimic the behavior of :sip:ref:`~PyQt6.QtGui.QPainter.drawText` to a specific point with no boundaries, and also when :sip:ref:`~PyQt6.QtGui.QPainter.drawText` is called with a bounding rectangle.

If a bounding rectangle is not required, create a :sip:ref:`~PyQt6.QtGui.QStaticText` object without setting a preferred text width. The text will then occupy a single line.

If you set a text width on the :sip:ref:`~PyQt6.QtGui.QStaticText` object, this will bound the text. The text will be formatted so that no line exceeds the given width. The text width set for :sip:ref:`~PyQt6.QtGui.QStaticText` will not automatically be used for clipping. To achieve clipping in addition to line breaks, use :sip:ref:`~PyQt6.QtGui.QPainter.setClipRect`. The position of the text is decided by the argument passed to :sip:ref:`~PyQt6.QtGui.QPainter.drawStaticText` and can change from call to call with a minimal impact on performance.

For extra convenience, it is possible to apply formatting to the text using the HTML subset supported by :sip:ref:`~PyQt6.QtGui.QTextDocument`. :sip:ref:`~PyQt6.QtGui.QStaticText` will attempt to guess the format of the input text using Qt::mightBeRichText(), and interpret it as rich text if this function returns ``true``. To force :sip:ref:`~PyQt6.QtGui.QStaticText` to display its contents as either plain text or rich text, use the function :sip:ref:`~PyQt6.QtGui.QStaticText.setTextFormat` and pass in, respectively, :sip:ref:`~PyQt6.QtCore.Qt.TextFormat.PlainText` and :sip:ref:`~PyQt6.QtCore.Qt.TextFormat.RichText`.

:sip:ref:`~PyQt6.QtGui.QStaticText` can only represent text, so only HTML tags which alter the layout or appearance of the text will be respected. Adding an image to the input HTML, for instance, will cause the image to be included as part of the layout, affecting the positions of the text glyphs, but it will not be displayed. The result will be an empty area the size of the image in the output. Similarly, using tables will cause the text to be laid out in table format, but the borders will not be drawn.

If it's the first time the static text is drawn, or if the static text, or the painter's font has been altered since the last time it was drawn, the text's layout has to be recalculated. On some paint engines, changing the matrix of the painter will also cause the layout to be recalculated. In particular, this will happen for any engine except for the OpenGL2 paint engine. Recalculating the layout will impose an overhead on the :sip:ref:`~PyQt6.QtGui.QPainter.drawStaticText` call where it occurs. To avoid this overhead in the paint event, you can call :sip:ref:`~PyQt6.QtGui.QStaticText.prepare` ahead of time to ensure that the layout is calculated.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.drawText`, :sip:ref:`~PyQt6.QtGui.QPainter.drawStaticText`, :sip:ref:`~PyQt6.QtGui.QTextLayout`, :sip:ref:`~PyQt6.QtGui.QTextDocument`.
