.. sip:class-description::
    :status: todo
    :brief: Tests the fragment shader's depth value against the depth of a sample being written to
    :realname: Qt3DRender::QDepthTest
    :digest: 5475c083fd9fbba7ab85e344e512e3a5

The :sip:ref:`~PyQt6.Qt3DRender.QDepthTest` class tests the fragment shader's depth value against the depth of a sample being written to.

A :sip:ref:`~PyQt6.Qt3DRender.QDepthTest` class is used to enable depth testing with a given depth test function. The depth test enables writing fragment color values when the depth test passes, and reject fragments which fail the test. The depth test uses the depth function to test the fragments depth value to the value against z-buffer. If the underlying surface does not have z-buffer, then :sip:ref:`~PyQt6.Qt3DRender.QDepthTest` does nothing.

.. seealso:: QAlphaTest, QStencilTest.
