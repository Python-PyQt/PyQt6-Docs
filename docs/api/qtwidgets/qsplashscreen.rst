:orphan:

.. sip:class:: PyQt6.QtWidgets.QSplashScreen
    :inherits: :sip:ref:`~PyQt6.QtWidgets.QWidget`
    :description: QtWidgets/QSplashScreen-c.rst

    .. sip:method:: PyQt6.QtWidgets.QSplashScreen.__init__
        :args:
            pixmap: :sip:ref:`~PyQt6.QtGui.QPixmap` = QPixmap()
            flags: :sip:ref:`~PyQt6.QtCore.Qt.WindowType` = Qt.WindowFlags()
        :description: QtWidgets/QSplashScreen-__init__-f-2.rst

    .. sip:method:: PyQt6.QtWidgets.QSplashScreen.__init__
        :args:
            :sip:ref:`~PyQt6.QtGui.QScreen`
            pixmap: :sip:ref:`~PyQt6.QtGui.QPixmap` = QPixmap()
            flags: :sip:ref:`~PyQt6.QtCore.Qt.WindowType` = Qt.WindowFlags()
        :description: QtWidgets/QSplashScreen-__init__-f-3.rst

    .. sip:method:: PyQt6.QtWidgets.QSplashScreen.clearMessage
        :description: QtWidgets/QSplashScreen-clearMessage-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplashScreen.drawContents
        :args:
            :sip:ref:`~PyQt6.QtGui.QPainter`
        :description: QtWidgets/QSplashScreen-drawContents-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplashScreen.event
        :args:
            :sip:ref:`~PyQt6.QtCore.QEvent`
        :returns:
            bool
        :description: QtWidgets/QSplashScreen-event-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplashScreen.finish
        :args:
            :sip:ref:`~PyQt6.QtWidgets.QWidget`
        :description: QtWidgets/QSplashScreen-finish-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplashScreen.message
        :returns:
            str
        :description: QtWidgets/QSplashScreen-message-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplashScreen.mousePressEvent
        :args:
            :sip:ref:`~PyQt6.QtGui.QMouseEvent`
        :description: QtWidgets/QSplashScreen-mousePressEvent-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplashScreen.pixmap
        :returns:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtWidgets/QSplashScreen-pixmap-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplashScreen.repaint
        :description: QtWidgets/QSplashScreen-repaint-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplashScreen.setPixmap
        :args:
            :sip:ref:`~PyQt6.QtGui.QPixmap`
        :description: QtWidgets/QSplashScreen-setPixmap-f.rst

    .. sip:method:: PyQt6.QtWidgets.QSplashScreen.showMessage
        :args:
            str
            alignment: int = :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag.AlignLeft`
            color: Union[:sip:ref:`~PyQt6.QtGui.QColor`, :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor`, int] = :sip:ref:`~PyQt6.QtCore.Qt.GlobalColor.black`
        :description: QtWidgets/QSplashScreen-showMessage-f-2.rst

    .. sip:signal:: PyQt6.QtWidgets.QSplashScreen.messageChanged
        :args:
            str
        :description: QtWidgets/QSplashScreen-messageChanged-s.rst
