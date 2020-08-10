//坐标机型：小米6X
//检查无障碍权限申请
auto.waitFor();
//设置屏幕宽度高度
setScreenMetrics(1080, 1920);
//常量设置
var AppName = "快手极速版";
var AppName_JB = "快手极速版脚本";

var 金币转圈 = id("redFloat");
var 金币转圈x = 127.5;
var 金币转圈y = 1218.5;
var 点赞 = id("like_button");
var 现金收益 = text("现金收益");
var 去签到 = text("去签到");
var 立即签到 = text("立即签到");
var 今天已签 = textContains("今天已签");
var 设置青少年模式 = text("设置青少年模式");
var 我知道了 = text("我知道了");
var 拖动滑块 = text("拖动滑块");
var 拖动滑块x = 123;
var 拖动滑块y = 976.5;
var 立即邀请 = text("立即邀请");

if (!requestScreenCapture()) {
    toast("请求截图失败");
    stop();
}
let count = 0;
let stop = setInterval("changeApp()",5000)
function changeApp(){
    AppName = A1
    count ++
}
if (count ===10){
    clearInterval()
}
app.launchApp(AppName);
//签到
// SignIn();
// sleep(random(1000,2000));
//滑动视频
slidingVideo();

/**
 * 签到
 */
function SignIn() {
    while (true) {
        sleep(random(1000, 2000));
        if (金币转圈.findOne(1000) != null) {
            console.log("金币转圈---已加载");
            sleep(random(1000, 2000));
            click(金币转圈x, 金币转圈y);
            console.log("金币转圈---已点击");
            while (true) {
                sleep(random(1000, 2000));
                if (现金收益.findOne(1000) != null) {
                    console.log("现金收益---已加载");
                    while (true) {
                        sleep(random(1000, 2000));
                        if (立即签到.findOne(1000) != null) {
                            sleep(random(1000, 2000));
                            立即签到.findOne().click();
                        } else if (今天已签.exists()) {
                            console.log("今天已签---已加载");
                            sleep(random(1000, 2000));
                            back();
                            console.log("金币转圈---已加载");
                            break;
                        }
                    }
                    break;
                }
            }
            break;
        }
    }
}

/**
 * 滑动视频
 */
function slidingVideo() {
    while (true) {
        //检测青少年模式
        if (设置青少年模式.findOne(1000) != null) {
            console.log("设置青少年模式");
            sleep(1000);
            我知道了.findOne().click();
        }
        //立即邀请
        if (立即邀请.findOne(1000) != null) {
            console.log("立即邀请");
            sleep(1000);
            back();
        }
        //检测滑块
        if (拖动滑块.findOne(1000) != null) {
            console.log("拖动滑块");
            dragSlider();
        }
        //开始滑动视频
        var x1 = random(255, 870);
        var y1 = random(1700, 1800);
        var x2 = random(255, 870);
        var y2 = random(222, 300);
        var time1 = random(3000, 6000);
        var time2 = random(500, 1000);
        sml_move(x1, y1, x2, y2, time2);
        sleep(time1);
    }
}

/**
 * 拖动滑块
 *
 */
function dragSlider() {
    for (var i = 0; i < 0; i++) {
        sleep(1000);
        log(i);
    }
    while (true) {
        img = images.captureScreen();
        if (img) {
            log("截图成功。进行识别滑块！");
            break;
        } else {
            log('截图失败,重新截图');
        }
    }
    var x = discernSlidingblock(img, device.width) + 65
    console.info("识别结果滑块X坐标：" + x);

    if (x > -1) {
        randomSwipe(拖动滑块x, 拖动滑块y, x, 拖动滑块y)
        return true;
    } else {
        return false;
        console.log("识别有误，请确认是否在滑块界面");
    }
}

/**
 * 计算滑块位置
 * @param {图片} img
 * @param {分辨率} ratio
 */
function discernSlidingblock(img, ratio) {
    //创建识别变量
    var temp, temp2, x, y, num, color, p, temp3, arr1;
    //分析设备分辨率
    if (ratio == 720) {
        var tb = [348, 253, 691, 638, 81]
        log("您的设备分辨率为：720p");
    } else if (ratio == 1080) {
        var tb = [463, 387, 912, 831, 125]
        log("您的设备分辨率为：1080p");
    } else {
        log("当前设备分辨率不符合规范")
        return -2
    }
    num = Math.ceil(tb[4] / 3.3 - 4);

    //计算滑块位置
    for (var k = 29; k <= 40; k++) {
        temp2 = "";
        color = "#" + k + "" + k + "" + k + "";
        for (var i = 1; i <= num; i++) {
            temp2 = temp2 + "0|" + i + "|" + color + ",";
            temp2 = temp2 + i + "|0|" + color + ",";
            temp2 = temp2 + "1|" + i + "|" + color + ",";
            temp2 = temp2 + i + "|1|" + color + ",";
            temp2 = temp2 + "2|" + i + "|" + color + ",";
            temp2 = temp2 + i + "|2|" + color + ",";
        }
        x = 0;
        while (x > -2) {
            y = 0;
            while (y > -2) {
                temp = "";
                for (var i = 1; i <= num; i += 2) {
                    temp = temp + "0|" + (tb[4] + y - i - 1) + "|" + color + ",";
                    temp = temp + (tb[4] + x) + "|" + i + "|" + color + ",";
                    temp = temp + (tb[4] + x) + "|" + (tb[4] + y - i - 1) + "|" + color + ",";
                    temp = temp + (tb[4] + x - i - 1) + "|0|" + color + ",";
                    temp = temp + i + "|" + (tb[4] + y) + "|" + color + ",";
                    temp = temp + (tb[4] + x - i - 1) + "|" + (tb[4] + y) + "|" + color + ",";
                    temp = temp + "1|" + (tb[4] + y - i - 1) + "|" + color + ",";
                    temp = temp + (tb[4] + x - 1) + "|" + i + "|" + color + ",";
                    temp = temp + (tb[4] + x - 1) + "|" + (tb[4] + y - i - 1) + "|" + color + ",";
                    temp = temp + (tb[4] + x - i - 1) + "|1|" + color + ",";
                    temp = temp + i + "|" + (tb[4] + y - 1) + "|" + color + ",";
                    temp = temp + (tb[4] + x - i - 1) + "|" + (tb[4] + y - 1) + "|" + color + ",";
                }
                temp = temp + temp2 + "0|0|" + color;
                arr1 = temp.split(",");
                var arr2 = new Array();
                for (var i = 0; i < arr1.length - 1; i++) {
                    arr2[i] = new Array();
                    temp3 = arr1[i].split("|");
                    arr2[i] = [Number(temp3[0]), Number(temp3[1]), temp3[2]];
                }
                try {
                    p = images.findMultiColors(img, color, arr2, {
                        region: [tb[0], tb[1], tb[2] - tb[0], tb[3] - tb[1]],
                        threshold: (Math.floor(k / 10) * 16 + k % 10)
                    });
                    if (p) {
                        img.recycle();
                        return p.x
                    }
                } catch (error) {
                    //出错
                    console.log("识别失败，错误原因：" + error);
                    return -1;
                }
                y = --y;
            }
            x = --x;
        }
    }
    try {
        img.recycle();
    } catch (error) {
        console.log("识别失败，错误原因：" + error);
    }
    return -1;
}

/**
 * 真人模拟滑动函数 （滑块滑动）
 * @param {起点x} sx
 * @param {起点y} sy
 * @param {终点x} ex
 * @param {终点y} ey
 */
function randomSwipe(sx, sy, ex, ey) {
    //设置随机滑动时长范围
    var timeMin = 1000
    var timeMax = 3000
    //设置控制点极限距离
    var leaveHeightLength = 500

    //根据偏差距离，应用不同的随机方式
    if (Math.abs(ex - sx) > Math.abs(ey - sy)) {
        var my = (sy + ey) / 2
        var y2 = my + random(0, leaveHeightLength)
        var y3 = my - random(0, leaveHeightLength)

        var lx = (sx - ex) / 3
        if (lx < 0) {
            lx = -lx
        }
        var x2 = sx + lx / 2 + random(0, lx)
        var x3 = sx + lx + lx / 2 + random(0, lx)
    } else {
        var mx = (sx + ex) / 2
        var y2 = mx + random(0, leaveHeightLength)
        var y3 = mx - random(0, leaveHeightLength)

        var ly = (sy - ey) / 3
        if (ly < 0) {
            ly = -ly
        }
        var y2 = sy + ly / 2 + random(0, ly)
        var y3 = sy + ly + ly / 2 + random(0, ly)
    }

    //获取运行轨迹，及参数
    var time = [0, random(timeMin, timeMax)]
    var track = bezierCreate(sx, sy, x2, y2, x3, y3, ex, ey)


    log("随机控制点A坐标：" + x2 + "," + y2)
    log("随机控制点B坐标：" + x3 + "," + y3)
    log("随机滑动时长：" + time[1])

    //滑动
    gestures(time.concat(track))
}

/**
 * 计算滑动轨迹
 */
function bezierCreate(x1, y1, x2, y2, x3, y3, x4, y4) {
    //构建参数
    var h = 100;
    var cp = [{x: x1, y: y1 + h}, {x: x2, y: y2 + h}, {x: x3, y: y3 + h}, {x: x4, y: y4 + h}];
    var numberOfPoints = 100;
    var curve = [];
    var dt = 1.0 / (numberOfPoints - 1);

    //计算轨迹
    for (var i = 0; i < numberOfPoints; i++) {
        var ax, bx, cx;
        var ay, by, cy;
        var tSquared, tCubed;
        var result_x, result_y;

        cx = 3.0 * (cp[1].x - cp[0].x);
        bx = 3.0 * (cp[2].x - cp[1].x) - cx;
        ax = cp[3].x - cp[0].x - cx - bx;
        cy = 3.0 * (cp[1].y - cp[0].y);
        by = 3.0 * (cp[2].y - cp[1].y) - cy;
        ay = cp[3].y - cp[0].y - cy - by;

        var t = dt * i
        tSquared = t * t;
        tCubed = tSquared * t;
        result_x = (ax * tCubed) + (bx * tSquared) + (cx * t) + cp[0].x;
        result_y = (ay * tCubed) + (by * tSquared) + (cy * t) + cp[0].y;
        curve[i] = {
            x: result_x,
            y: result_y
        };
    }

    //轨迹转路数组
    var array = [];
    for (var i = 0; i < curve.length; i++) {
        try {
            var j = (i < 100) ? i : (199 - i);
            xx = parseInt(curve[j].x)
            yy = parseInt(Math.abs(100 - curve[j].y))
        } catch (e) {
            break
        }
        array.push([xx, yy])
    }

    return array
}

/**
 * 仿真随机带曲线滑动  (视频滑动)
 * @param {起点x} qx
 * @param {起点y} qy
 * @param {终点x} zx
 * @param {终点y} zy
 * @param {过程耗时单位毫秒} time
 */
function sml_move(qx, qy, zx, zy, time) {
    var xxy = [time];
    var point = [];
    var dx0 = {
        "x": qx,
        "y": qy
    };

    var dx1 = {
        "x": random(qx - 100, qx + 100),
        "y": random(qy, qy + 50)
    };
    var dx2 = {
        "x": random(zx - 100, zx + 100),
        "y": random(zy, zy + 50),
    };
    var dx3 = {
        "x": zx,
        "y": zy
    };
    for (var i = 0; i < 4; i++) {

        eval("point.push(dx" + i + ")");

    }
    ;
    log(point[3].x)

    for (let i = 0; i < 1; i += 0.08) {
        xxyy = [parseInt(bezier_curves(point, i).x), parseInt(bezier_curves(point, i).y)]

        xxy.push(xxyy);

    }

    log(xxy);
    gesture.apply(null, xxy);
};

function bezier_curves(cp, t) {
    cx = 3.0 * (cp[1].x - cp[0].x);
    bx = 3.0 * (cp[2].x - cp[1].x) - cx;
    ax = cp[3].x - cp[0].x - cx - bx;
    cy = 3.0 * (cp[1].y - cp[0].y);
    by = 3.0 * (cp[2].y - cp[1].y) - cy;
    ay = cp[3].y - cp[0].y - cy - by;

    tSquared = t * t;
    tCubed = tSquared * t;
    result = {
        "x": 0,
        "y": 0
    };
    result.x = (ax * tCubed) + (bx * tSquared) + (cx * t) + cp[0].x;
    result.y = (ay * tCubed) + (by * tSquared) + (cy * t) + cp[0].y;
    return result;
};