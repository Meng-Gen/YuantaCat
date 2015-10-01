var chart = AmCharts.makeChart("net_income_to_operating_activities_yearly_chart_div", {
    "type" : "serial",
    "dataLoader": {
        "url": "cash_flow_yearly_data.json",
        "format": "json"
    },
    "categoryField" : "date",
    "titles" : [
        {
            "size": 15,
            "text": "會計盈餘與營運活動之現金流量之差異分析",
        },
    ],
    "numberFormatter" : {
        "precision" : 0, 
    },
    "valueAxes" : [
        {
            "id" : "left_axis",
            "axisThickness" : 2,
            "axisAlpha" : 1,
            "position" : "left",
        }, 
    ],
    "graphs" : [
        {
            "valueAxis": "left_axis",
            "type" : "column", 
            "title" : "營運活動之現金流量",
            "valueField" : "cash_flow_from_operating_activities",
            "fillAlphas" : 0.6,
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
        },
        {
            "valueAxis": "left_axis",
            "type" : "column",
            "title" : "會計盈餘",
            "valueField" : "net_profit",
            "fillAlphas" : 0.6,
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
        },
    ],
    "legend" : {
        "align" : "center",
        "valueAlign" : "left",
    },
    "chartCursor" : {
        "zoomable" : false, // as the chart displayes not too many values, we disabled zooming
        "cursorPosition": "mouse",
    },
    "balloon": {
        "borderThickness": 1,
        "shadowAlpha": 0
    },
});
