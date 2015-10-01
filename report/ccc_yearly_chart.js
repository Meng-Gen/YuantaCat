var chart = AmCharts.makeChart("ccc_yearly_chart_div", {
    "type" : "serial",
    "dataLoader" : {
        "url" : "profitability_yearly_data.json",
        "format" : "json"
    },
    "categoryField" : "date",
    "titles" : [
        {
            "size" : 15,
            "text" : "現金轉換循環",
        },
    ],
    "categoryAxis" : {
        "gridAlpha" : 0.07,
        "axisColor" : "#DADADA",
        "startOnAxis" : true,
    },
    "numberFormatter" : {
        "precision" : 1, 
    },
    "valueAxes" : [
        {
            "id" : "left_axis",
            "axisThickness" : 2,
            "gridAlpha" : 0,
            "axisAlpha" : 1,
            "position" : "left",
            "title" : "Days",
        }, 
    ],
    "graphs" : [
        {
            "valueAxis" : "left_axis",
            "type" : "line", 
            "title" : "平均銷貨天數",
            "valueField" : "dio",
            "bullet" : "round",
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
        },
        {
            "valueAxis" : "left_axis",
            "type" : "line",
            "title" : "平均應收帳款收現天數",
            "valueField" : "dso",
            "bullet" : "square",
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
        },
        {
            "valueAxis": "left_axis",
            "type" : "line",
            "title" : "平均應付帳款付款天數",
            "valueField" : "dpo",
            "bullet" : "triangleUp",
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
        },
        {
            "valueAxis" : "left_axis",
            "type" : "line",
            "title" : "現金轉換循環",
            "valueField" : "ccc",
            "bullet" : "diamond",
            "fillAlphas" : 0.1,
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
        },
    ],
    "legend" : {
        "align" : "center",
        "valueAlign" : "left",
    },
    "chartCursor" : {
        "zoomable" : false, // as the chart displayes not too many values, we disabled zooming
        "cursorPosition" : "mouse",
    },
    "balloon" : {
        "borderThickness" : 1,
        "shadowAlpha" : 0
    },
});
