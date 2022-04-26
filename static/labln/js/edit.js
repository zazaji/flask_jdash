function init() {
    var $ = go.GraphObject.make;
    myDiagram = $(go.Diagram, "myDiagramDiv", {
        initialContentAlignment: go.Spot.Center,
        validCycle: go.Diagram.CycleDestinationTree,
        "clickCreatingTool.archetypeNodeData": {},
        "clickCreatingTool.insertPart": function(loc) {
            this.archetypeNodeData = {
                key: getNextKey(),
                parent: "",
                名字: "(佚名)",
                性别: "",
                双亲: "",
                生年: "",
                卒年: "",
                备注: ""
            };
            return go.ClickCreatingTool.prototype.insertPart.call(this, loc)
        },
        layout: $(go.TreeLayout, {
            sorting: go.TreeLayout.SortingAscending,
            comparer: function(a, b) {
                var av = a.node.data.生年;
                var bv = b.node.data.生年;
                if (av < bv) {
                    return -1
                }
                if (av > bv) {
                    return 1
                }
                return 0
            },
            treeStyle: go.TreeLayout.StyleLastParents,
            arrangement: go.TreeLayout.ArrangementHorizontal,
            angle: 90,
            layerSpacing: 35,
            alternateAngle: 90,
            alternateLayerSpacing: 35,
            alternateAlignment: go.TreeLayout.AlignmentBus,
            alternateNodeSpacing: 20
        }),
        "undoManager.isEnabled": true
    });
    fitBrowserWindow();
    myDiagram.add($(go.Part, "Table", {
        position: new go.Point(-100,0),
        selectable: false
    }, $(go.Panel, "Horizontal", {
        row: 0,
        alignment: go.Spot.Left
    }, $(go.Shape, "Rectangle", {
        desiredSize: new go.Size(30,30),
        fill: "#0099CC",
        margin: 5,
        stroke: "#0099CC"
    }), $(go.TextBlock, "男", {
        font: "500 15px Droid Serif, sans-serif",
        stroke: "white"
    })), $(go.Panel, "Horizontal", {
        row: 1,
        alignment: go.Spot.Left
    }, $(go.Shape, "Rectangle", {
        desiredSize: new go.Size(30,30),
        fill: "#FF6666",
        margin: 5,
        stroke: "#FF6666"
    }), $(go.TextBlock, "女", {
        font: "500 15px Droid Serif, sans-serif",
        stroke: "white"
    })), $(go.Panel, "Horizontal", {
        row: 2,
        alignment: go.Spot.Left
    }, $(go.Shape, "Rectangle", {
        desiredSize: new go.Size(30,30),
        fill: "#FFA100",
        margin: 5,
        stroke: "#FFA100"
    }), $(go.TextBlock, "未知", {
        font: "500 15px Droid Serif, sans-serif",
        stroke: "white"
    }))));
    myDiagram.addDiagramListener("Modified", function(e) {
        var button = document.getElementById("SaveButton");
        if (button) {
            button.disabled = !myDiagram.isModified
        }
        var idx = document.title.indexOf("*");
        if (myDiagram.isModified) {
            if (idx < 0) {
                document.title += "*"
            }
        } else {
            if (idx >= 0) {
                document.title = document.title.substr(0, idx)
            }
        }
    });
    function getNextKey() {
        var key = nodeIdCounter;
        while (myDiagram.model.findNodeDataForKey(key) !== null) {
            key = nodeIdCounter++
        }
        return key
    }
    var nodeIdCounter = 1;
    function nodeDoubleClick(e, obj) {
        var clicked = obj.part;
        if (clicked !== null) {
            var thisemp = clicked.data;
            myDiagram.startTransaction("add employee");
            var Yparent = myDiagram.model.findNodeDataForKey(thisemp.key);
            var newemp;
            newemp = {
                key: getNextKey(),
                名字: "(佚名)",
                parent: thisemp.key,
                性别: "",
                双亲: "",
                生年: "",
                卒年: "",
                备注: ""
            };
            myDiagram.model.addNodeData(newemp);
            myDiagram.commitTransaction("add employee")
        }
    }
    function mayWorkFor(node1, node2) {
        if (!(node1 instanceof go.Node)) {
            return false
        }
        if (node1 === node2) {
            return false
        }
        if (node2.isInTreeOf(node1)) {
            return false
        }
        return true
    }
    function textStyle() {
        return {
            font: "9pt  Segoe UI,sans-serif",
            stroke: "white"
        }
    }
    function tooltipTextConverter(person) {
        var str = "";
        var YnewJson = myDiagram.model.toJSON();
        var result = JSON.parse(YnewJson);
        var Yparent = myDiagram.model.findNodeDataForKey(person.parent);
        var Yself = myDiagram.model.findNodeDataForKey(person.key);
        var YchildNumber = 0;
        var YgrandChildNumber = 0;
        var YallChild = 0;
        for (var i = 1; i <= result.nodeDataArray.length; i++) {
            var Ytemp = myDiagram.model.findNodeDataForKey(i);
            if (Ytemp.parent === undefined) {
                continue
            } else {
                if (Ytemp.parent == Yself.key) {
                    YchildNumber++
                }
            }
        }
        var Ytemps = [];
        for (var i = 1; i <= result.nodeDataArray.length; i++) {
            var Ytemp = myDiagram.model.findNodeDataForKey(i);
            if (Ytemp.parent === undefined) {
                continue
            } else {
                if (Ytemp.parent == Yself.key) {
                    Ytemps.push(Ytemp.key)
                }
            }
        }
        while (Ytemps.length != 0) {
            var hello = Ytemps.pop();
            var Ytemp1 = myDiagram.model.findNodeDataForKey(hello);
            for (var i = 1; i <= result.nodeDataArray.length; i++) {
                var Ytemp = myDiagram.model.findNodeDataForKey(i);
                if (Ytemp.parent === undefined) {
                    continue
                } else {
                    if (Ytemp.parent == Ytemp1.key) {
                        YgrandChildNumber++
                    }
                }
            }
        }
        var Ytemp2s = [];
        Ytemp2s.push(person.key);
        do {
            var hello = Ytemp2s.pop();
            var Ytemp1 = myDiagram.model.findNodeDataForKey(hello);
            for (var i = 1; i <= result.nodeDataArray.length; i++) {
                var Ytemp = myDiagram.model.findNodeDataForKey(i);
                if (Ytemp.parent === undefined) {
                    continue
                } else {
                    if (Ytemp.parent == Ytemp1.key) {
                        YallChild++;
                        Ytemp2s.push(Ytemp.key)
                    }
                }
            }
        } while (Ytemp2s.length != 0);str += "名字: " + person.名字;
        if (person.性别 !== undefined) {
            str += "\n性别: " + person.性别
        }
        if (person.双亲 !== undefined && person.parent !== undefined && Yparent.性别 === "男") {
            str += "\n父亲: " + Yparent.名字 + "\n母亲: " + person.双亲
        }
        if (person.双亲 !== undefined && person.parent !== undefined && Yparent.性别 === "女") {
            str += "\n母亲: " + Yparent.名字 + "\n父亲: " + person.双亲
        }
        if (person.生年 !== undefined) {
            str += "\n生年: " + person.生年
        }
        if (person.卒年 !== undefined) {
            str += "\n卒年: " + person.卒年
        }
        str += "\n孩子数: " + YchildNumber;
        str += "\n孙子数: " + YgrandChildNumber;
        str += "\n后代数: " + YallChild;
        return str
    }
    var tooltiptemplate = $(go.Adornment, "Auto", $(go.Shape, "Rectangle", {
        fill: "whitesmoke",
        stroke: "black"
    }), $(go.TextBlock, {
        font: "bold 8pt Helvetica, bold Arial, sans-serif",
        wrap: go.TextBlock.WrapFit,
        margin: 5
    }, new go.Binding("text","",tooltipTextConverter)));
    function genderBrushConverter(gender) {
        if (gender === "男") {
            return "#0099CC"
        }
        if (gender === "女") {
            return "#FF6666"
        }
        return "#FFA100"
    }
    myDiagram.nodeTemplate = $(go.Node, "Auto", new go.Binding("text","生年"), {
        toolTip: tooltiptemplate
    }, {
        doubleClick: nodeDoubleClick
    }, {
        mouseDragEnter: function(e, node, prev) {
            var diagram = node.diagram;
            var selnode = diagram.selection.first();
            if (!mayWorkFor(selnode, node)) {
                return
            }
            var shape = node.findObject("SHAPE");
            if (shape) {
                shape._prevFill = shape.fill;
                shape.fill = "darkred"
            }
        },
        mouseDragLeave: function(e, node, next) {
            var shape = node.findObject("SHAPE");
            if (shape && shape._prevFill) {
                shape.fill = shape._prevFill
            }
        },
        mouseDrop: function(e, node) {
            var diagram = node.diagram;
            var selnode = diagram.selection.first();
            if (mayWorkFor(selnode, node)) {
                var link = selnode.findTreeParentLink();
                if (link !== null) {
                    link.fromNode = node
                } else {
                    diagram.toolManager.linkingTool.insertLink(node, node.port, selnode, selnode.port)
                }
            }
        }
    }, new go.Binding("layerName","isSelected",function(sel) {
            return sel ? "Foreground" : ""
        }
    ).ofObject(), $(go.Shape, "Rectangle", {
        name: "SHAPE",
        fill: null,
        strokeWidth: 2,
        stroke: null,
        portId: "",
        fromLinkable: true,
        toLinkable: true,
        cursor: "pointer"
    }, new go.Binding("stroke","isHighlighted",function(h) {
            return h ? "white" : "#696969"
        }
    ).ofObject(), new go.Binding("fill","性别",genderBrushConverter)), $(go.Panel, "Horizontal", $(go.Panel, "Table", {
        maxSize: new go.Size(150,999),
        margin: new go.Margin(6,10,0,10),
        defaultAlignment: go.Spot.Left
    }, $(go.RowColumnDefinition, {
        column: 2,
        width: 4
    }), $(go.TextBlock, textStyle(), {
        row: 0,
        column: 0,
        columnSpan: 5,
        font: "12pt Segoe UI,sans-serif",
        editable: true,
        isMultiline: false,
        minSize: new go.Size(10,16)
    }, new go.Binding("text","名字").makeTwoWay()), $(go.TextBlock, textStyle(), {
        row: 1,
        column: 0
    }, new go.Binding("text","key",function(v) {
            return "key: " + v
        }
    )), $(go.TextBlock, textStyle(), {
        row: 1,
        column: 3,
    }, new go.Binding("text","parent",function(v) {
            return "parent: " + v
        }
    )), $(go.TextBlock, textStyle(), {
        row: 2,
        column: 0,
    }, new go.Binding("text","生年",function(v) {
            return "(" + v
        }
    )), $(go.TextBlock, textStyle(), {
        row: 2,
        column: 1,
    }, new go.Binding("text","卒年",function(v) {
            return " - " + (v ? v : "        ") + ")"
        }
    )), $(go.TextBlock, textStyle(), {
        row: 3,
        column: 0,
        columnSpan: 5,
        font: "italic 9pt sans-serif",
        wrap: go.TextBlock.WrapFit,
        editable: true,
        minSize: new go.Size(10,14)
    }, new go.Binding("text","备注").makeTwoWay()))));
    myDiagram.nodeTemplate.contextMenu = $(go.Adornment, "Vertical", $("ContextMenuButton", $(go.TextBlock, "-  斩断  -"), {
        click: function(e, obj) {
            var node = obj.part.adornedPart;
            if (node !== null) {
                var thisemp = node.data;
                myDiagram.startTransaction("斩断");
                myDiagram.model.setDataProperty(thisemp, "parent", "0");
                myDiagram.commitTransaction("斩断")
            }
        }
    }), $("ContextMenuButton", $(go.TextBlock, "-  除名  -"), {
        click: function(e, obj) {
            var node = obj.part.adornedPart;
            if (node !== null) {
                var thisemp = node.data;
                myDiagram.startTransaction("vacate");
                myDiagram.model.setDataProperty(thisemp, "名字", "(已除名)");
                myDiagram.commitTransaction("vacate")
            }
        }
    }), $("ContextMenuButton", $(go.TextBlock, "-  驱逐   -"), {
        click: function(e, obj) {
            var node = obj.part.adornedPart;
            if (node !== null) {
                myDiagram.startTransaction("reparent remove");
                var chl = node.findTreeChildrenNodes();
                while (chl.next()) {
                    var emp = chl.value;
                    myDiagram.model.setParentKeyForNodeData(emp.data, 0)
                }
                myDiagram.model.removeNodeData(node.data);
                myDiagram.commitTransaction("reparent remove")
            }
        }
    }), $("ContextMenuButton", $(go.TextBlock, "-  灭门  -"), {
        click: function(e, obj) {
            var node = obj.part.adornedPart;
            if (node !== null) {
                myDiagram.startTransaction("remove dept");
                myDiagram.removeParts(node.findTreeParts());
                myDiagram.commitTransaction("remove dept")
            }
        }
    }));
    myDiagram.linkTemplate = $(go.Link, {
        routing: go.Link.Orthogonal,
        corner: 5,
        selectable: false
    }, $(go.Shape, {
        strokeWidth: 3,
        stroke: "#00FF00"
    }));
    myDiagram.model = go.Model.fromJson({
        "class": "go.TreeModel",
        "nodeDataArray": []
    });
    if (window.Inspector) {
        myInspector = new Inspector("myInspector",myDiagram,{
            properties: {
                "key": {
                    readOnly: true
                },
                "备注": {},
                "parent": {}
            }
        })
    }
}
function doSave(value, type, name) {
    var blob;
    if (typeof window.Blob == "function") {
        blob = new Blob([value],{
            type: type
        })
    } else {
        var BlobBuilder = window.BlobBuilder || window.MozBlobBuilder || window.WebKitBlobBuilder || window.MSBlobBuilder;
        var bb = new BlobBuilder();
        bb.append(value);
        blob = bb.getBlob(type)
    }
    var URL = window.URL || window.webkitURL;
    var bloburl = URL.createObjectURL(blob);
    var anchor = document.createElement("a");
    if ("download"in anchor) {
        anchor.style.visibility = "hidden";
        anchor.href = bloburl;
        anchor.download = name;
        document.body.appendChild(anchor);
        var evt = document.createEvent("MouseEvents");
        evt.initEvent("click", true, true);
        anchor.dispatchEvent(evt);
        document.body.removeChild(anchor)
    } else {
        if (navigator.msSaveBlob) {
            navigator.msSaveBlob(blob, name)
        } else {
            location.href = bloburl
        }
    }
}
function Save() {
    doSave(myDiagram.model.toJson(), "text/latex", "家谱.json");
    myDiagram.isModified = false
}
function load(f) {
    if (typeof FileReader == "undefined") {
        alert("检测到您的浏览器不支持FileReader对象！")
    }
    var tmpFile = f[0];
    var reader = new FileReader();
    reader.readAsText(tmpFile);
    reader.onload = function(e) {
        myDiagram.model = go.Model.fromJson(e.target.result)
    }
}
function refresh() {
    myDiagram.model = go.Model.fromJson(myDiagram.model.toJson())
}
function fitBrowserWindow() {
    myDiagram.div.style.height = window.innerHeight + "px";
    myDiagram.requestUpdate()
}
function searchDiagram() {
    document.getElementById("answerCount").innerText = "";
    var input = document.getElementById("mySearch");
    if (!input) {
        return
    }
    input.focus();
    var regex = new RegExp(input.value,"i");
    myDiagram.startTransaction("highlight search");
    myDiagram.clearHighlighteds();
    if (input.value) {
        var queryObj = {};
        if (document.getElementById("query").value != "在世") {
            queryObj[document.getElementById("query").value] = regex
        } else {
            queryObj.生年 = function(n) {
                return n <= input.value && n != ""
            }
            ;
            queryObj.卒年 = function(n) {
                return n >= input.value | n == ""
            }
        }
        var results = myDiagram.findNodesByExample(queryObj);
        myDiagram.highlightCollection(results);
        if (results.count > 0) {
            myDiagram.centerRect(results.first().actualBounds)
        }
        document.getElementById("answerCount").innerText = "共找到" + results.count + "个结果"
    }
    myDiagram.commitTransaction("highlight search")
}
window.onload = function() {
    init();
    document.getElementById("mySearch").addEventListener("input", searchDiagram);
    document.getElementById("query").addEventListener("change", searchDiagram);
    document.getElementById("refresh").addEventListener("click", refresh)
}
;
window.onresize = fitBrowserWindow;