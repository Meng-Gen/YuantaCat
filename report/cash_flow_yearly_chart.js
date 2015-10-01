var chart = AmCharts.makeChart("cash_flow_yearly_chart_div", {
    "type" : "serial",
    "dataLoader": {
        "url": "cash_flow_yearly_data.json",
        "format": "json"
    },
    "categoryField" : "date",
    "titles" : [
        {
            "size": 15,
            "text": "現金流量表分析重點",
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
        {
            "id" : "minor_left_axis",
            "axisThickness" : 2,
            "gridAlpha" : 0,
            "offset" : 50,
            "axisAlpha" : 1,
            "position" : "left",
        },
        {
            "id" : "right_axis",
            "axisThickness" : 2,
            "gridAlpha" : 0,
            "axisAlpha" : 1,
            "position" : "right",
        },
    ],
    "graphs" : [
        {
            "valueAxis": "left_axis",
            "type" : "line", 
            "title" : "營運活動之現金流量",
            "valueField" : "cash_flow_from_operating_activities",
            "bullet" : "round",
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
        },
        {
            "valueAxis": "left_axis",
            "type" : "line",
            "title" : "投資活動之現金流量",
            "valueField" : "cash_flow_from_investing_activities",
            "bullet" : "square",
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
        },
        {
            "valueAxis": "left_axis",
            "type" : "line",
            "title" : "理財活動之現金流量",
            "valueField" : "cash_flow_from_financing_activities",
            "bullet" : "triangleUp",
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
        },
        {
            "valueAxis": "left_axis",
            "type" : "line",
            "title" : "自由現金流量",
            "valueField" : "free_cash_flow",
            "bullet" : "triangleDown",
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
        },    
        {
            "valueAxis": "left_axis",
            "type" : "line",
            "title" : "累積自由現金流量",
            "valueField" : "accumulated_free_cash_flow",
            "bullet" : "diamond",
            "fillAlphas" : 0.2,
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
            "lineColor": "#04D215",
            "negativeLineColor": "#D1655D",
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
