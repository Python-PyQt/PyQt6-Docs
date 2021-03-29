.. sip:class-description::
    :status: todo
    :brief: Means to quit an event loop when it is no longer needed
    :digest: c7f04926a0af3606f083c38c2cc9a808

The :sip:ref:`~PyQt6.QtCore.QEventLoopLocker` class provides a means to quit an event loop when it is no longer needed.

The :sip:ref:`~PyQt6.QtCore.QEventLoopLocker` operates on particular objects - either a :sip:ref:`~PyQt6.QtCore.QCoreApplication` instance, a :sip:ref:`~PyQt6.QtCore.QEventLoop` instance or a :sip:ref:`~PyQt6.QtCore.QThread` instance.

This makes it possible to, for example, run a batch of jobs with an event loop and exit that event loop after the last job is finished. That is accomplished by keeping a :sip:ref:`~PyQt6.QtCore.QEventLoopLocker` with each job instance.

The variant which operates on :sip:ref:`~PyQt6.QtCore.QCoreApplication` makes it possible to finish asynchronously running jobs after the last gui window has been closed. This can be useful for example for running a job which uploads data to a network.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QEventLoop`, :sip:ref:`~PyQt6.QtCore.QCoreApplication`.
