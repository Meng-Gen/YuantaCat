var chart = AmCharts.makeChart("capital_structure_chart_div", {
    "type" : "serial",
    "dataLoader": {
        "url": "capital_structure_data.json",
        "format": "json"
    },
    "categoryField" : "year",
    "titles" : [
        {
            "size": 15,
            "text": "Chart Title",
        },
    ],
    "categoryAxis" : {
        "gridAlpha" : 0.07,
        "axisColor" : "#DADADA",
        "startOnAxis" : true,
    },
    "valueAxes" : [
        {
            "title" : "percent", // this line makes the chart "stacked"
            "stackType" : "100%",
            "gridAlpha" : 0.07,
        },
    ],
    "graphs" : [
        {
            "type" : "line", // it's simple line graph
            "title" : "Cars",
            "valueField" : "cars",
            "lineAlpha" : 0,
            "fillAlphas" : 0.6, // setting fillAlphas to > 0 value makes it area graph
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
        },
        {
            "type" : "line",
            "title" : "Motorcycles",
            "valueField" : "motorcycles",
            "lineAlpha" : 0,
            "fillAlphas" : 0.6,
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
        },
        {
            "type" : "line",
            "title" : "Bicycles",
            "valueField" : "bicycles",
            "lineAlpha" : 0,
            "fillAlphas" : 0.6,
            "balloonText" : "<span style='font-size:14px; color:#000000;'><b>[[value]]</b></span>",
        },
    ],
    "legend" : {
        "align" : "center",
        "valueText" : "[[value]] ([[percents]]%)",
        "valueWidth" : 100,
        "valueAlign" : "left",
        "equalWidths" : false,
        "periodValueText" : "total: [[value.sum]]",
    },
    "chartCursor" : {
        "zoomable" : false, // as the chart displayes not too many values, we disabled zooming
        "cursorAlpha" : 0,
    },
});
