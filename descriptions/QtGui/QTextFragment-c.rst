.. sip:class-description::
    :status: todo
    :brief: Holds a piece of text in a QTextDocument with a single QTextCharFormat
    :digest: 00db3e50cf5896acdca5ddc18152fdf0

The :sip:ref:`~PyQt6.QtGui.QTextFragment` class holds a piece of text in a :sip:ref:`~PyQt6.QtGui.QTextDocument` with a single :sip:ref:`~PyQt6.QtGui.QTextCharFormat`.

A text fragment describes a piece of text that is stored with a single character format. Text in which the character format changes can be represented by sequences of text fragments with different formats.

If the user edits the text in a fragment and introduces a different character format, the fragment's text will be split at each point where the format changes, and new fragments will be created. For example, changing the style of some text in the middle of a sentence will cause the fragment to be broken into three separate fragments: the first and third with the same format as before, and the second with the new style. The first fragment will contain the text from the beginning of the sentence, the second will contain the text from the middle, and the third takes the text from the end of the sentence.

.. image:: ../../../images/qtextfragment-split.png

A fragment's text and character format can be obtained with the :sip:ref:`~PyQt6.QtGui.QTextFragment.text` and :sip:ref:`~PyQt6.QtGui.QTextFragment.charFormat` functions. The :sip:ref:`~PyQt6.QtGui.QTextFragment.length` function gives the length of the text in the fragment. :sip:ref:`~PyQt6.QtGui.QTextFragment.position` gives the position in the document of the start of the fragment. To determine whether the fragment contains a particular position within the document, use the :sip:ref:`~PyQt6.QtGui.QTextFragment.contains` function.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextDocument`, `Rich Text Document Structure <https://doc.qt.io/qt-6/richtext-structure.html>`_.
