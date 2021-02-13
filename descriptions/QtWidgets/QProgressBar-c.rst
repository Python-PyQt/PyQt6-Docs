.. sip:class-description::
    :status: todo
    :brief: Horizontal or vertical progress bar
    :digest: 2814a75b9f5212ccbc69626a759f8f50

The :sip:ref:`~PyQt6.QtWidgets.QProgressBar` widget provides a horizontal or vertical progress bar.

.. image:: ../../../images/windows-progressbar.png

A progress bar is used to give the user an indication of the progress of an operation and to reassure them that the application is still running.

The progress bar uses the concept of *steps*. You set it up by specifying the minimum and maximum possible step values, and it will display the percentage of steps that have been completed when you later give it the current step value. The percentage is calculated by dividing the progress (\ :sip:ref:`~PyQt6.QtWidgets.QProgressBar.value` - :sip:ref:`~PyQt6.QtWidgets.QProgressBar.minimum`) divided by :sip:ref:`~PyQt6.QtWidgets.QProgressBar.maximum` - :sip:ref:`~PyQt6.QtWidgets.QProgressBar.minimum`.

You can specify the minimum and maximum number of steps with :sip:ref:`~PyQt6.QtWidgets.QProgressBar.setMinimum` and :sip:ref:`~PyQt6.QtWidgets.QProgressBar.setMaximum`. The current number of steps is set with :sip:ref:`~PyQt6.QtWidgets.QProgressBar.setValue`. The progress bar can be rewound to the beginning with :sip:ref:`~PyQt6.QtWidgets.QProgressBar.reset`.

If minimum and maximum both are set to 0, the bar shows a busy indicator instead of a percentage of steps. This is useful, for example, when using QNetworkAccessManager to download items when they are unable to determine the size of the item being downloaded.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QProgressDialog`, `GUI Design Handbook: Progress Indicator <https://doc.qt.io/qt-6/guibooks.html#fowler>`_.
