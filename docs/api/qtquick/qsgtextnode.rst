:orphan:

.. sip:class:: PyQt6.QtQuick.QSGTextNode
    :inherits: :sip:ref:`~PyQt6.QtQuick.QSGTransformNode`
    :description: QtQuick/QSGTextNode-c.rst

    .. sip:enum:: PyQt6.QtQuick.QSGTextNode.RenderType
        :description: QtQuick/QSGTextNode-RenderType-e.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGTextNode.RenderType.CurveRendering
            :description: QtQuick/QSGTextNode-RenderType-CurveRendering-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGTextNode.RenderType.NativeRendering
            :description: QtQuick/QSGTextNode-RenderType-NativeRendering-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGTextNode.RenderType.QtRendering
            :description: QtQuick/QSGTextNode-RenderType-QtRendering-v.rst

    .. sip:enum:: PyQt6.QtQuick.QSGTextNode.TextStyle
        :description: QtQuick/QSGTextNode-TextStyle-e.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGTextNode.TextStyle.Normal
            :description: QtQuick/QSGTextNode-TextStyle-Normal-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGTextNode.TextStyle.Outline
            :description: QtQuick/QSGTextNode-TextStyle-Outline-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGTextNode.TextStyle.Raised
            :description: QtQuick/QSGTextNode-TextStyle-Raised-v.rst

        .. sip:enum-member:: PyQt6.QtQuick.QSGTextNode.TextStyle.Sunken
            :description: QtQuick/QSGTextNode-TextStyle-Sunken-v.rst

    .. sip:method:: PyQt6.QtQuick.QSGTextNode.addTextDocument
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
            :sip:ref:`~PyQt6.QtGui.QTextDocument`
            selectionStart: int = -1
            selectionCount: int = -1
        :description: QtQuick/QSGTextNode-addTextDocument-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGTextNode.addTextLayout
        :args:
            :sip:ref:`~PyQt6.QtCore.QPointF`
            :sip:ref:`~PyQt6.QtGui.QTextLayout`
            selectionStart: int = -1
            selectionCount: int = -1
            lineStart: int = 0
            lineCount: int = -1
        :description: QtQuick/QSGTextNode-addTextLayout-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGTextNode.clear
        :description: QtQuick/QSGTextNode-clear-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGTextNode.color
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtQuick/QSGTextNode-color-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGTextNode.filtering
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGTexture.Filtering`
        :description: QtQuick/QSGTextNode-filtering-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGTextNode.linkColor
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtQuick/QSGTextNode-linkColor-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGTextNode.renderType
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGTextNode.RenderType`
        :description: QtQuick/QSGTextNode-renderType-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGTextNode.renderTypeQuality
        :returns:
            int
        :description: QtQuick/QSGTextNode-renderTypeQuality-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGTextNode.selectionColor
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtQuick/QSGTextNode-selectionColor-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGTextNode.selectionTextColor
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtQuick/QSGTextNode-selectionTextColor-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGTextNode.setColor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtQuick/QSGTextNode-setColor-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGTextNode.setFiltering
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGTexture.Filtering`
        :description: QtQuick/QSGTextNode-setFiltering-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGTextNode.setLinkColor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtQuick/QSGTextNode-setLinkColor-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGTextNode.setRenderType
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGTextNode.RenderType`
        :description: QtQuick/QSGTextNode-setRenderType-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGTextNode.setRenderTypeQuality
        :args:
            int
        :description: QtQuick/QSGTextNode-setRenderTypeQuality-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGTextNode.setSelectionColor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtQuick/QSGTextNode-setSelectionColor-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGTextNode.setSelectionTextColor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtQuick/QSGTextNode-setSelectionTextColor-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGTextNode.setStyleColor
        :args:
            Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int]
        :description: QtQuick/QSGTextNode-setStyleColor-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGTextNode.setTextStyle
        :args:
            :sip:ref:`~PyQt6.QtQuick.QSGTextNode.TextStyle`
        :description: QtQuick/QSGTextNode-setTextStyle-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGTextNode.setViewport
        :args:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtQuick/QSGTextNode-setViewport-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGTextNode.styleColor
        :returns:
            :sip:ref:`~PyQt6.QtGui.QColor`
        :description: QtQuick/QSGTextNode-styleColor-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGTextNode.textStyle
        :returns:
            :sip:ref:`~PyQt6.QtQuick.QSGTextNode.TextStyle`
        :description: QtQuick/QSGTextNode-textStyle-f.rst

    .. sip:method:: PyQt6.QtQuick.QSGTextNode.viewport
        :returns:
            :sip:ref:`~PyQt6.QtCore.QRectF`
        :description: QtQuick/QSGTextNode-viewport-f.rst
