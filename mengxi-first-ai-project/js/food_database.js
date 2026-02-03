const foodDatabase = [
    {
        name: "苹果",
        gi: 36,
        gl: 5,
        cal: 53,
        traffic_light: "green",
        category: "水果",
        tips: "苹果是低GI水果的代表，富含果胶。建议作为上午或下午的加餐食用，带皮吃纤维更丰富。"
    },
    {
        name: "西瓜 (1片)",
        gi: 72,
        gl: 4,
        cal: 31,
        traffic_light: "yellow",
        category: "水果",
        tips: "虽然GI高（升糖快），但水分大，碳水含量低。控制在200g（约一片）以内是安全的。切记千万不要榨汁喝！"
    },
    {
        name: "白米饭",
        gi: 83,
        gl: 21,
        cal: 116,
        traffic_light: "red",
        category: "主食",
        tips: "精制碳水，升糖极快。建议用杂粮饭（糙米、燕麦、黑米）代替，或者煮饭时加入1/3的粗粮。如果必须吃，请最后吃，并减少分量。"
    },
    {
        name: "杂粮饭",
        gi: 55,
        gl: 14,
        cal: 120,
        traffic_light: "green",
        category: "主食",
        tips: "优秀的控糖主食。建议黑米、糙米、红豆与白米以1:1或1:2比例搭配，饱腹感强且升糖慢。"
    },
    {
        name: "黄瓜",
        gi: 15,
        gl: 1,
        cal: 16,
        traffic_light: "green",
        category: "蔬菜",
        tips: "完美的负卡路里食物，作为加餐或正餐配菜都极佳，几乎不升糖。"
    },
    {
        name: "全麦面包",
        gi: 50,
        gl: 10,
        cal: 250,
        traffic_light: "green",
        category: "主食",
        tips: "选择配料表第一位是'全麦粉'的真正全麦面包。避开添加了大量糖和油的'伪'全麦。"
    },
    {
        name: "油条",
        gi: 75,
        gl: 25,
        cal: 388,
        traffic_light: "red",
        category: "早餐",
        tips: "高糖高油高热量，'糖妈'的天敌。建议完全避免，想吃中式早餐可选豆浆+无糖杂粮馒头。"
    },
    {
        name: "牛奶 (纯)",
        gi: 27,
        gl: 1.3,
        cal: 54,
        traffic_light: "green",
        category: "乳制品",
        tips: "补钙首选，GI非常低。建议每天300-500ml。乳糖不耐受可选无糖酸奶。"
    },
    {
        name: "红薯 (煮)",
        gi: 54,
        gl: 13,
        cal: 86,
        traffic_light: "yellow",
        category: "主食",
        tips: "煮红薯比烤红薯GI低很多！它可以代替部分米饭，但不能作为蔬菜吃，要算作主食分量。"
    },
    {
        name: "荔枝",
        gi: 70,
        gl: 11,
        cal: 71,
        traffic_light: "red",
        category: "水果",
        tips: "含糖量高且多为果糖，极易引起血糖波动。孕期建议慎吃或仅尝1-2颗。"
    },
    {
        name: "鸡蛋 (水煮)",
        gi: 0,
        gl: 0,
        cal: 143,
        traffic_light: "green",
        category: "蛋白质",
        tips: "几乎不含碳水，优质蛋白来源。每天1-2个，是控糖餐盘的定海神针。"
    },
    {
        name: "南瓜 (老)",
        gi: 75,
        gl: 4,
        cal: 23,
        traffic_light: "yellow",
        category: "蔬菜/主食",
        tips: "老南瓜虽然甜，但碳水密度不高。如果作为菜吃，请相应减少几口米饭。嫩南瓜则可以随便吃。"
    },
    {
        name: "西红柿",
        gi: 15,
        gl: 0.6,
        cal: 18,
        traffic_light: "green",
        category: "蔬菜/水果",
        tips: "既是蔬菜也是水果，含糖量极低，饿了随时可以作为一个大西红柿加餐。"
    },
    {
        name: "馒头 (白面)",
        gi: 88,
        gl: 42,
        cal: 223,
        traffic_light: "red",
        category: "主食",
        tips: "GI值甚至高于白糖！发酵面食消化极快。必须搭配大量蔬菜和肉类一起吃，严禁空腹单吃。"
    },
    {
        name: "坚果 (原味)",
        gi: 20,
        gl: 5,
        cal: 600,
        traffic_light: "yellow",
        category: "零食",
        tips: "优质脂肪，饱腹感强。但热量极高，每天一小把（25g）即可，建议选原味未加工的。"
    },
    {
        name: "燕麦片 (即食)",
        gi: 55,
        gl: 13,
        cal: 370,
        traffic_light: "green",
        category: "主食",
        tips: "选择配料表只有'燕麦'的生燕麦或快煮燕麦，避免'麦片'或'营养麦片'（通常含糖）。"
    },
    {
        name: "可乐",
        gi: 65,
        gl: 16,
        cal: 43,
        traffic_light: "red",
        category: "饮料",
        tips: "液态糖，吸收速度最快，血糖杀手。想喝气泡水请选择0糖0卡的气泡水。"
    },
    {
        name: "猕猴桃",
        gi: 52,
        gl: 6,
        cal: 61,
        traffic_light: "green",
        category: "水果",
        tips: "虽然酸甜，但GI适中，富含维生素C。适合两餐之间食用。"
    },
    {
        name: "猪肉 (瘦)",
        gi: 0,
        gl: 0,
        cal: 143,
        traffic_light: "green",
        category: "蛋白质",
        tips: "主要提供蛋白质和脂肪，不升糖。但要注意烹饪方式，避免红烧（加糖）或油炸。"
    },
    {
        name: "土豆 (炒)",
        gi: 60,
        gl: 16,
        cal: 80,
        traffic_light: "yellow",
        category: "蔬菜/主食",
        tips: "土豆是主食！如果这顿菜有土豆丝，请务必不吃或少吃米饭。"
    }
];

// 如果需要导出给模块化环境使用
if (typeof module !== 'undefined' && module.exports) {
    module.exports = foodDatabase;
}
