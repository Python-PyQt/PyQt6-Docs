.. sip:method-description::
    :status: todo
    :pysig: 6f916023b5ef6d23dd04c5719efc1630
    :realsig: (const int,const QHash<QXYSeries::PointConfiguration,QVariant>&)
    :digest: 15ef9e8db255be031ff657c100ff7e64

Enables customizing the appearance of a point located at *index* with desired *configuration*.

With points configuration you can change various aspects of every point's appearance.

A point's configuration is represented as a hash map with :sip:ref:`~PyQt6.QtCharts.QXYSeries.pointConfiguration` keys and :sip:ref:`~PyQt6.QtCore.QVariant` values. For example:

::

    QLineSeries *series = new QLineSeries();
    series->setName("Customized serie");
    series->setPointsVisible(true);

    *series << QPointF(0, 6) << QPointF(2, 4) << QPointF(3, 6) << QPointF(7, 4) << QPointF(10, 5)
            << QPointF(11, 1) << QPointF(13, 3) << QPointF(17, 6) << QPointF(18, 3)
            << QPointF(20, 2);

    QChart *chart = new QChart();
    chart->addSeries(series);
    chart->createDefaultAxes();

    QHash<QXYSeries::PointConfiguration, QVariant> conf;
    conf[QXYSeries::PointConfiguration::Color] = QColor(Qt::red);
    conf[QXYSeries::PointConfiguration::Size] = 8;
    conf[QXYSeries::PointConfiguration::LabelVisibility] = true;

    series->setPointConfiguration(4, conf);

    conf.remove(QXYSeries::PointConfiguration::LabelVisibility);
    series->setPointConfiguration(6, conf);

In this example, you can see a default :sip:ref:`~PyQt6.QtCharts.QLineSeries` with 10 points and with changed configuration of two points. Both changed points are red and visibly bigger than the others with a look derived from series. By default, points don't have labels, but the point at index 4 has the label thanks to the :sip:ref:`~PyQt6.QtCharts.QXYSeries.PointConfiguration.LabelVisibility` configuration value. Below is an example of a chart created in this way:

.. image:: ../../../images/xyseries_point_configuration.png

.. seealso:: :sip:ref:`~PyQt6.QtCharts.QXYSeries.pointConfiguration`, :sip:ref:`~PyQt6.QtCharts.QXYSeries.pointsConfiguration`, :sip:ref:`~PyQt6.QtCharts.QXYSeries.clearPointsConfiguration`.
