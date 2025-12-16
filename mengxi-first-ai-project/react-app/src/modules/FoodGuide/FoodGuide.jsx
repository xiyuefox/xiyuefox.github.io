import React, { useState } from 'react';

const FoodGuide = () => {
  const [searchTerm, setSearchTerm] = useState('');

  // 食物指南数据结构
  const foodGuideData = [
    {
      letter: 'A',
      items: [
        {
          name: '添加剂 (Additives)',
          status: '⚠️',
          description: '英国食品标准局（FSA）认为英国使用的所有添加剂在孕期食用都是安全的。在评估任何添加剂的安全性时，FSA会考察化学物质的生殖毒性及其改变遗传物质的能力。虽然单个添加剂的安全性经过测试，但人们担忧同时摄入多种不同添加剂可能产生的"鸡尾酒效应"。另一个问题是，含有大量添加剂的食品通常过度加工，脂肪、盐和糖含量高，而必需维生素和矿物质含量低。理想情况下，应尽量减少含添加剂的食品，多吃水果、蔬菜、豆类和全谷物等未加工食品。另见人工甜味剂、亚硝酸盐和亚硫酸盐。'
        },
        {
          name: '杏仁 (Almonds)',
          status: '✅',
          description: '蛋白质、铜、烟酸、核黄素和维生素E的良好来源。除非您对杏仁过敏，否则无需避免。'
        },
        {
          name: '凤尾鱼 (Anchovies)',
          status: '⚠️',
          description: '这是一种油性鱼类，是omega-3脂肪酸的良好来源，与三文鱼或沙丁鱼相似。孕期可以食用熟凤尾鱼，但每周不应超过两份油性鱼。罐装凤尾鱼也是安全的，但往往含盐量很高，因此不建议大量摄入。从超市密封盒中购买的腌制凤尾鱼也应该没问题，但如果您在西班牙小吃吧、熟食店或对食品储存或卫生不太放心的地方，最好避免。披萨上的凤尾鱼同样如此，虽然是罐装的，但可能开封太久或未冷藏保存。'
        },
        {
          name: '人工甜味剂 (Artificial sweeteners)',
          status: '⚠️',
          description: '这些被广泛用作糖的低热量或零热量替代品。有些可能被认为是"天然的"，因为它们是从叶子或糖中提取的。这里列出的所有甜味剂都经过欧洲食品安全局（EFSA）评估，并被批准作为健康饮食的一部分在食品和饮料中安全使用。一些专家对人工甜味剂的安全性，特别是在孕期使用表示担忧，但没有真正的证据支持这些说法。欧盟安全评估还检查添加剂（包括甜味剂）是否具有致癌性或毒性，是否对孕妇或儿童构成风险。理想情况下，最好吃未加工的食品，喝水而不是无糖饮料，但如果您很难减少糖的摄入量，那么适量食用人工甜味的食品和饮料可能会有所帮助。'
        }
      ]
    },
    {
      letter: 'B',
      items: [
        {
          name: '香蕉 (Bananas)',
          status: '✅',
          description: '如果孕期或哺乳期能量下降，这是一种很好的健康零食。有些女性发现香蕉会导致胃灼热，但除此之外没有必要避免。'
        },
        {
          name: '烧烤食品 (Barbecued food)',
          status: '⚠️',
          description: '确保所有肉类、汉堡、香肠、鱼类等都正确烹饪，否则有食物中毒的风险。即使表面看起来熟了，也要检查中心是否滚烫。此外，尽量避免过度烧焦的食物：烹饪过程会产生多环芳烃（PAHs）和杂环胺（HAs），包括一些可能在孕期有害的致癌化学物质。最好将摄入量保持在最低限度，尽管尚未确定安全水平。在烧烤时，还要检查沙拉是否彻底清洗，并避免在外面放置太久的食物，因为食物中毒细菌在温暖天气中繁殖迅速。'
        },
        {
          name: '罗勒 (Basil)',
          status: '✅',
          description: '正常量食用是安全的。然而，当浓缩或大量使用时，它是几种具有子宫刺激作用的草药之一。因此，孕期应避免使用罗勒油（常用于芳香疗法）。'
        },
        {
          name: '豆芽 (Bean sprouts)',
          status: '⚠️',
          description: '孕期应避免食用生豆芽，因为有沙门氏菌风险。如果想吃，应彻底加热至滚烫。这包括标注为"即食"的豆芽。FSA在2010年发布此建议，此前发现100多例与生豆芽可能相关的沙门氏菌Bareilly病例。'
        },
        {
          name: '贝阿恩酱/伯那西酱 (Béarnaise sauce)',
          status: '❌',
          description: '通常含有半熟蛋黄，因此应避免，因为有沙门氏菌中毒风险。可以用巴氏杀菌蛋制作贝阿恩酱，这种情况下是安全的。'
        },
        {
          name: '啤酒 (Beer)',
          status: '❌',
          description: '曾被认为有益于母乳喂养，但研究表明这是一个误解。关于孕期安全，请参阅第49页的酒精信息。'
        },
        {
          name: '苦柠檬水 (Bitter lemon)',
          status: '✅',
          description: '孕期饮用苦柠檬水是安全的。另见奎宁。'
        },
        {
          name: '黑布丁/血肠 (Black pudding)',
          status: '⚠️',
          description: '孕期可以食用黑布丁，前提是它已冷藏保存并彻底煮熟。它是铁的良好来源，但盐和饱和脂肪含量也很高，因此不宜大量食用。'
        },
        {
          name: '麸皮 (Bran)',
          status: '⚠️',
          description: '谷物（如小麦和大米）的外层称为麸皮。它是膳食纤维的浓缩形式。在食物上撒麸皮可能有助于缓解便秘，但也会减少某些维生素和矿物质的吸收，包括铁和锌。更好的选择是吃富含纤维的食物，如全谷物（如全麦面包、糙米）、豆类（如扁豆、豆类）以及水果和蔬菜，因为这些含有更高水平的必需营养素。'
        },
        {
          name: '早餐麦片 (Breakfast cereal)',
          status: '✅',
          description: '早餐吃麦片是很好的，它也是健康的零食。尝试吃添加了维生素和矿物质的麦片，包括叶酸和铁，因为这些在此时特别重要。有机麦片在英国不添加营养强化剂，一些廉价系列麦片也不添加，所以要查看标签。选择高纤维早餐麦片也是个好主意，有助于预防便秘。'
        },
        {
          name: '布里奶酪 (Brie)',
          status: '❌',
          description: '应避免，因为有李斯特菌风险，可能伤害未出生的婴儿。这包括用巴氏杀菌或未杀菌牛奶制成的布里奶酪。然而，像炸布里奶酪这样的菜肴，如果奶酪滚烫，是安全的，因为任何李斯特菌都会在烹饪过程中被杀死。有关李斯特菌的更多信息，请参阅第45页。'
        }
      ]
    },
    {
      letter: 'C',
      items: [
        {
          name: '凯撒沙拉 (Caesar salad)',
          status: '⚠️',
          description: '凯撒沙拉的酱汁通常含有生蛋，有沙门氏菌风险，因此孕期最好避免。有关沙门氏菌的更多信息，请参阅第47页。然而，超市出售的瓶装凯撒沙拉酱是用巴氏杀菌蛋制成的，因此被认为是安全的。'
        },
        {
          name: '卡拉巴粉笔 (Calabash chalk)',
          status: '❌',
          description: '这是一种粉笔（也称为卡拉巴石、La Craie、Argile、Nzu和Mabele），用于缓解孕吐。传统上由西非妇女使用，从非洲进口到英国。然而，不建议使用，因为发现它含有高水平的铅，可能伤害婴儿发育中的神经系统。'
        },
        {
          name: '卡门贝尔奶酪 (Camembert)',
          status: '❌',
          description: '这是一种软奶酪，孕期应避免，因为有李斯特菌风险。这包括用巴氏杀菌或未杀菌牛奶制成的卡门贝尔。然而，像炸卡门贝尔这样的菜肴，如果奶酪滚烫，是安全的，因为任何李斯特菌都会在烹饪过程中被杀死。有关李斯特菌的更多信息，请参阅第45页。'
        },
        {
          name: '卡博纳拉酱 (Carbonara sauce)',
          status: '⚠️',
          description: '孕期应避免用自制卡博纳拉酱制作的意大利面或其他面食，因为它通常用生蛋制成。如果您从超市购买卡博纳拉酱，无论是冷藏的还是罐装的，都可以安全食用，因为它们含有巴氏杀菌蛋或不含蛋。大多数餐厅，包括Bella Italia和Prezzo，也用巴氏杀菌蛋制作酱汁，但在更高档或传统的意大利餐厅，最好确认一下。'
        },
        {
          name: '粉笔 (Chalk)',
          status: '⚠️',
          description: '白色粉笔是纯钙，身体可以像食物中的钙一样使用。如果您对粉笔或任何其他通常不被视为食物或饮料的东西有强烈渴望，这被称为"异食癖"（见第17页）。少量食用白色粉笔不太可能造成伤害。然而，大量食用可能导致血液中钙水平过高，可能对您和宝宝造成问题。不建议食用彩色粉笔，因为其中的色素可能与食品色素不同，且未经测试是否可以安全食用。'
        },
        {
          name: '切达奶酪 (Cheddar cheese)',
          status: '✅',
          description: '这是一种硬奶酪，无论是用巴氏杀菌还是未杀菌牛奶制成的，都可以安全食用。'
        },
        {
          name: '奶酪 (Cheese)',
          status: '⚠️',
          description: '孕期不应食用某些奶酪，因为它们可能被李斯特菌污染。这适用于软质霉菌成熟奶酪（如布里）和软质蓝纹奶酪（如丹麦蓝纹奶酪），无论它们是用巴氏杀菌还是未杀菌牛奶制成的。您还应该避免用未杀菌的山羊奶和绵羊奶制成的软奶酪（如Chèvre）。然而，彻底加热可以杀死李斯特菌。因此，如果这些奶酪是热菜的一部分（如在披萨上或在酱汁中），应该是安全的——您只需要确保它们被正确烹饪并且整个都滚烫。'
        },
        {
          name: '芝士蛋糕 (Cheesecake)',
          status: '⚠️',
          description: '可以食用烘焙过的芝士蛋糕（有时描述为烤芝士蛋糕）。您也可以安全食用超市和类似商店出售的芝士蛋糕，因为它们应该是用巴氏杀菌蛋制成的，这消除了沙门氏菌风险。芝士蛋糕有时用瑞可塔或马斯卡彭奶酪制成，这两种在孕期都可以安全食用。您应该避免食用未烘焙的自制芝士蛋糕。这些含有明胶，放入冰箱凝固。它们有沙门氏菌风险，因为含有未煮熟的蛋。如果您不确定自制芝士蛋糕或餐厅的芝士蛋糕是如何制作的，最好询问。'
        },
        {
          name: '奶酪酱 (Cheese spread)',
          status: '✅',
          description: '加工奶酪酱，如Dairylea、笑牛、Primula以及超市类似自有品牌产品，可以安全食用。另见奶油奶酪。'
        },
        {
          name: '鸡肉 (Chicken)',
          status: '✅',
          description: '是蛋白质、铁和B族维生素的良好来源。食用前务必检查是否彻底煮熟，直到汁水透明，否则可能导致沙门氏菌食物中毒。有关沙门氏菌的更多信息，请参阅第47页。'
        },
        {
          name: '巧克力 (Chocolate)',
          status: '⚠️',
          description: '芬兰的一项研究发现，孕期经常吃巧克力的母亲生的宝宝微笑和笑得更多。美国的另一项研究结果表明，巧克力可能降低先兆子痫的风险，尽管目前没有足够的证据来确定这是否属实。尽管有这些可能的好处，您应该避免吃太多巧克力，因为它含有咖啡因以及糖和脂肪，可能导致体重增加过多。'
        },
        {
          name: '苹果醋 (Cider vinegar/apple cider vinegar)',
          status: '⚠️',
          description: '为了治疗孕吐，有些人建议在一杯冷水或温水中滴几滴或加一茶匙苹果醋。这种疗法在美国似乎比英国更受欢迎。支持者认为，在用餐时或全天小口喝这种饮料有助于减少恶心。可以加一茶匙蜂蜜使味道更好。它也被认为对胃灼热或胃酸反流有效。没有科学证据证明它有效，但一些女性相信它有帮助，尝试一下肯定没有坏处。一些爱好者认为只有未经巴氏杀菌的苹果醋才有效。然而，由于食物中毒风险，最好避免。'
        },
        {
          name: '肉桂 (Cinnamon)',
          status: '⚠️',
          description: '孕期食用肉桂是可以的，包括肉桂味的粥或早餐麦片，以及肉桂卷和其他蛋糕和饼干等烘焙食品。事实上，在粥等食物中添加肉桂可能是有益的，因为它有甜味，因此您不需要添加那么多糖。然而，应避免服用肉桂补充剂，最好不要吃很大量——例如，每天超过一茶匙的肉桂。'
        },
        {
          name: '粘土 (Clay)',
          status: '❌',
          description: '有时被称为sikor或shikor mati。烤粘土被一些人认为在孕期有益，但在2011年，FSA警告妇女不要食用。他们发现它含有高水平的铅（可能影响婴儿的大脑发育）和砷（增加肺癌、皮肤癌和膀胱癌的风险）。'
        },
        {
          name: '咖啡 (Coffee)',
          status: '⚠️',
          description: '孕期和哺乳期饮用咖啡是安全的，但每天不应超过约两杯速溶咖啡或两杯现磨咖啡。'
        },
        {
          name: '可乐 (Cola)',
          status: '⚠️',
          description: '孕前、孕期和哺乳期饮用可乐是安全的，但不应过量。每330毫升罐含有约40毫克咖啡因，因此需要与茶和咖啡一起计算。普通（非无糖）品种每罐还含有约140千卡热量，因此如果大量饮用，可能会在没有给宝宝提供所需维生素和矿物质的情况下体重增加过多。无糖、低脂和淡味品种含有与普通可乐相同的咖啡因，除非您特别选择无咖啡因产品。它们还含有人工甜味剂。'
        },
        {
          name: '卷心菜沙拉 (Coleslaw)',
          status: '⚠️',
          description: '用罐装沙拉酱或蛋黄酱新鲜制作的卷心菜沙拉可以安全食用。卷心菜沙拉制作后应存放在冰箱中。FSA认为英国出售的现成卷心菜沙拉也是安全的。在其他一些国家，包括美国和澳大利亚，建议妇女避免预制的卷心菜沙拉，特别是在熟食柜台出售的，因为有李斯特菌风险。用自制蛋黄酱制作的卷心菜沙拉应该避免，因为它含有生蛋，可能导致沙门氏菌中毒。'
        },
        {
          name: '蟹 (Crab)',
          status: '⚠️',
          description: '如果蟹被正确烹饪并趁热食用是可以的——例如，蟹饼或蟹肉玉米汤。每周不应超过两份蟹，因为它可能含有与油性鱼类相似水平的污染物。如果不确定最近的烹饪时间和储存方式，最好避免冷食的蟹。它可能被李斯特菌或其他食物中毒细菌污染。'
        }
      ]
    },
    {
      letter: 'D',
      items: [
        {
          name: '熟食店食品 (Deli foods)',
          status: '⚠️',
          description: '美国、澳大利亚和新西兰的建议是，如果您怀孕了，不要吃熟食店或柜台的食物。英国没有具体的指南。然而，尽可能选择预包装食品而不是熟食产品是明智的。这是因为未包装的食品可能被其他产品的李斯特菌污染。低风险食品如火腿可能与处理高风险食品（如萨拉米）使用的相同器具接触过。此外，您无法知道熟食食品是否超过了保质期。'
        },
        {
          name: '无糖饮料 (Diet drinks)',
          status: '⚠️',
          description: '孕期或哺乳期被认为是安全的。然而，没有人知道高摄入人工甜味剂是否会产生长期影响，因此适量是明智的。另见人工甜味剂。'
        },
        {
          name: '蘸酱 (Dips)',
          status: '⚠️',
          description: '预包装的蘸酱如鹰嘴豆泥、黄瓜酸奶酱、萨尔萨酱和酸奶油或酸奶基产品在孕期应该是安全食用的。在熟食柜台出售的蘸酱最好避免，因为有交叉污染风险和对保质期的不确定性。任何含有蓝纹奶酪的蘸酱应该避免。'
        },
        {
          name: '鸭蛋 (Duck eggs)',
          status: '⚠️',
          description: '孕期可以安全食用鸭蛋，前提是蛋黄和蛋白都煮至凝固。任何含有鸭蛋的菜肴都应该煮至整个都滚烫。2010年，FSA发布官方警告，提醒人们在烹饪和处理鸭蛋时要注意卫生。这是由于与鸭蛋相关的鸭型沙门氏菌DT8爆发，涉及63例病例，包括一例死亡。'
        }
      ]
    },
    {
      letter: 'E',
      items: [
        {
          name: '艾登奶酪 (Edam)',
          status: '✅',
          description: '孕期可以安全食用艾登奶酪。'
        },
        {
          name: '蛋酒 (Eggnog)',
          status: '❌',
          description: '除了酒精，新鲜蛋酒还含有未煮熟的蛋，可能含有沙门氏菌。最好避免。'
        },
        {
          name: '鸡蛋 (Eggs)',
          status: '⚠️',
          description: 'FSA目前建议孕妇避免生的或半熟的鸡蛋，因为它们可能含有沙门氏菌。煮至蛋白和蛋黄都凝固的鸡蛋是安全食用的。这将破坏可能存在的任何沙门氏菌。所以，如果彻底煮熟，您可以吃煮蛋、煎蛋或炒蛋。'
        },
        {
          name: '班尼迪克蛋 (Eggs Benedict)',
          status: '❌',
          description: '这道菜含有水煮蛋（蛋黄是流动的）和荷兰酱（用仅部分煮熟的鸡蛋制成）。应该避免，因为可能含有沙门氏菌。'
        },
        {
          name: '能量饮料 (Energy drinks)',
          status: '⚠️',
          description: '如果您感到疲倦需要提神，能量饮料可能看起来是答案。然而，大多数都添加了咖啡因或瓜拉那（也含有咖啡因）。就像咖啡或可乐一样，这些饮料计入您孕期每日200毫克的咖啡因限量。一些能量饮料还含有可能影响您或宝宝的草药。如果您不确定，最好避免。'
        },
        {
          name: '蜗牛 (Escargot)',
          status: '⚠️',
          description: '经过安全采购、加工和烹饪的蜗牛在孕期应该是安全食用的。然而，最好不要吃您自己采集的蜗牛，因为它们不受相同的卫生法规约束，可能被有害细菌或化学物质污染。'
        }
      ]
    },
    {
      letter: 'F',
      items: [
        {
          name: '茴香茶 (Fennel tea)',
          status: '⚠️',
          description: '不建议孕期饮用，因为它被认为具有轻度激素作用并且是子宫刺激剂。没有关于摄入量的官方建议，但有些人建议孕期完全避免茴香茶，而另一些人建议每天最多两杯应该没问题。'
        },
        {
          name: '菲达奶酪 (Feta cheese)',
          status: '⚠️',
          description: '孕期可以安全食用菲达奶酪，前提是用巴氏杀菌牛奶制成。'
        },
        {
          name: '鱼 (Fish)',
          status: '⚠️',
          description: '建议孕妇、哺乳期妇女或计划怀孕的妇女每周至少吃两份鱼，包括一份油性鱼。一份约为140克煮熟的鱼，相当于烹饪前约170克。吃鱼时，确保正确烹饪以避免食物中毒风险。'
        },
        {
          name: '碳酸饮料 (Fizzy drinks)',
          status: '⚠️',
          description: '孕期偶尔喝碳酸饮料是安全的，尽管它们不是健康的选择，特别是如果您喝含糖的并且有妊娠糖尿病。一些还含有人工甜味剂，可乐和能量饮料都含有咖啡因。'
        },
        {
          name: '亚麻籽 (Flaxseeds)',
          status: '⚠️',
          description: '也称为亚麻仁，是α-亚麻酸（ALA）的良好来源，这是一种短链omega-3脂肪酸。然而，关于整粒亚麻籽有一些问题，选择亚麻籽油而不是整粒种子可能更好。'
        },
        {
          name: '法式鲜奶酪 (Fromage frais)',
          status: '✅',
          description: '孕期可以安全食用法式鲜奶酪，前提是用巴氏杀菌牛奶制成。'
        },
        {
          name: '水果 (Fruit)',
          status: '✅',
          description: '水果是任何健康饮食的重要组成部分，如果您怀孕、哺乳或考虑要孩子，这尤其如此。水果富含重要的维生素、矿物质和植物化学物质。您每天应该至少吃五份水果和蔬菜。'
        },
        {
          name: '果汁 (Fruit juice)',
          status: '⚠️',
          description: '纯果汁算作您每天推荐的五份水果和蔬菜中的一份——但无论您喝多少，它永远不能算作超过一份。这是因为它不像整个水果那样含有那么多纤维，而且它含有游离糖，会损害牙齿并导致血糖水平急剧上升。一般建议每天不要喝超过150毫升的果汁或果昔。'
        }
      ]
    },
    {
      letter: 'G',
      items: [
        {
          name: '野味 (Game)',
          status: '❌',
          description: '孕期应避免食用用铅弹射杀的野味，因为它可能含有不健康水平的铅，可能伤害婴儿发育中的大脑和神经系统。'
        },
        {
          name: '大蒜 (Garlic)',
          status: '✅',
          description: '孕期吃大蒜或服用大蒜补充剂被一些人认为有助于预防高血压和先兆子痫。然而，没有进行足够的研究来确定它是否有效。它不太可能造成伤害，报告的唯一副作用是"气味"。'
        },
        {
          name: '生姜 (Ginger)',
          status: '✅',
          description: '生姜是孕期孕吐和恶心的传统疗法。它的有效性已经在多项研究中进行了测试，结果表明，与安慰剂相比，它显著减少了恶心感。'
        },
        {
          name: '山羊奶酪 (Goats\' cheese)',
          status: '⚠️',
          description: '有几种不同类型的山羊奶酪可供选择。当我们想到山羊奶酪时，我们通常指的是Chèvre。这是一种有白色外皮的软奶酪，类似于布里奶酪。像其他霉菌成熟的奶酪一样，因为有李斯特菌风险，孕期应该避免。然而，如果它被彻底烹饪并趁热食用，任何李斯特菌都会被破坏。'
        },
        {
          name: '绿茶 (Green tea)',
          status: '⚠️',
          description: '没有足够的信息来确定孕期饮用绿茶是否安全，因此NHS建议孕妇每天饮用不超过四杯。绿茶含有咖啡因，就像普通红茶一样，因此在估计您的每日咖啡因摄入量时应包括它，并确保不超过每天200毫克的限量。'
        }
      ]
    },
    {
      letter: 'H',
      items: [
        {
          name: '羊杂碎 (Haggis)',
          status: '❌',
          description: '羊杂碎的成分之一是肝脏，因此由于其高维生素A含量应该避免。见肝脏。'
        },
        {
          name: '哈罗米奶酪 (Halloumi cheese)',
          status: '✅',
          description: '孕期可以安全食用哈罗米奶酪，前提是用巴氏杀菌牛奶制成。'
        },
        {
          name: '火腿 (Ham)',
          status: '✅',
          description: '孕期可以安全食用预包装熟火腿。这通常被描述为烤制、水煮或蜂蜜烤火腿。'
        },
        {
          name: '草药茶 (Herbal teas)',
          status: '⚠️',
          description: '这些包括由根、浆果、花、种子或茶叶以外的叶子制成的任何茶。女性在孕期和哺乳期可能选择饮用它们来减少咖啡因摄入量，但NHS建议孕妇每天饮用不超过四杯草药茶或绿茶。'
        },
        {
          name: '荷兰酱 (Hollandaise sauce)',
          status: '❌',
          description: '这通常含有半熟蛋黄，因此孕期应避免，因为有沙门氏菌风险。然而，如果您从超市购买速成混合包或罐装荷兰酱，孕期可以安全食用。'
        },
        {
          name: '蜂蜜 (Honey)',
          status: '✅',
          description: '孕期和哺乳期可以安全食用蜂蜜。蜂蜜偶尔会含有肉毒杆菌孢子，婴儿的肠道可能无法处理，导致婴儿肉毒杆菌中毒。因此，12个月以下的婴儿不应吃蜂蜜。'
        }
      ]
    },
    {
      letter: 'I',
      items: [
        {
          name: '冰淇淋 (Ice cream)',
          status: '⚠️',
          description: '可以安全食用超市或类似商店预包装出售的盒装或单个冰淇淋。自制冰淇淋通常含有生的或半熟的鸡蛋，因此孕期应该避免，因为它可能含有沙门氏菌。'
        },
        {
          name: '糖霜 (Icing)',
          status: '⚠️',
          description: '大多数类型的糖霜在孕期都可以安全食用。从超市和面包店购买的食品上的糖霜应该没问题。这包括软黄油糖霜、用奶油奶酪制成的糖霜（如胡萝卜蛋糕上的）和皇家糖霜。然而，自制皇家糖霜是用生蛋白制成的，因此应该避免，因为有沙门氏菌风险。'
        }
      ]
    },
    {
      letter: 'J',
      items: [
        {
          name: '雅尔斯堡奶酪 (Jarlsberg)',
          status: '✅',
          description: '孕期可以安全食用雅尔斯堡奶酪。'
        }
      ]
    },
    {
      letter: 'K',
      items: [
        {
          name: '海带 (Kelp)',
          status: '⚠️',
          description: '见海藻。'
        }
      ]
    },
    {
      letter: 'L',
      items: [
        {
          name: '柠檬凝乳 (Lemon curd)',
          status: '⚠️',
          description: '从超市购买的商业制备柠檬凝乳在孕期可以安全食用。自制柠檬凝乳含有半熟蛋，孕期应避免，因为有沙门氏菌风险。'
        },
        {
          name: '生菜 (Lettuce)',
          status: '✅',
          description: '孕期可以安全食用生菜，前提是您彻底清洗它。您甚至应该清洗袋装购买的预洗沙拉叶，以避免李斯特菌和沙门氏菌风险。'
        },
        {
          name: '甘草 (Liquorice)',
          status: '⚠️',
          description: '根据NHS，孕期可以安全食用甘草。然而，适量食用是明智的，因为每周食用超过约250克与早产风险增加有关（37周前出生）。'
        },
        {
          name: '肝脏 (Liver)',
          status: '❌',
          description: '孕期应避免肝脏和用肝脏制成的食品，如肝酱、肝肠和羊杂碎。它们含有高水平的视黄醇形式的维生素A，可能伤害宝宝的发育。'
        },
        {
          name: '乐加力 (Lucozade)',
          status: '⚠️',
          description: '孕期饮用乐加力被认为是安全的，但一些品种含有咖啡因，一些糖含量极高。'
        }
      ]
    },
    {
      letter: 'M',
      items: [
        {
          name: '鲭鱼 (Mackerel)',
          status: '⚠️',
          description: '这是一种油性鱼，是长链omega-3脂肪酸的良好来源。然而，每周不应超过两份（每份140克）。'
        },
        {
          name: '麦芽热饮 (Malted hot drinks)',
          status: '✅',
          description: '好立克和阿华田在孕期都可以安全饮用。它们添加了维生素和矿物质，包括维生素A，但维生素A的量符合孕期建议。'
        },
        {
          name: '蛋黄酱 (Mayonnaise)',
          status: '⚠️',
          description: '孕期可以安全食用从超市或类似商店购买的罐装蛋黄酱。在室温下出售（而不是冷藏）的蛋黄酱是用巴氏杀菌蛋制成的。孕期应避免自制蛋黄酱，因为它含有生的未经巴氏杀菌的蛋，可能含有沙门氏菌。'
        },
        {
          name: '肉类 (Meat)',
          status: '⚠️',
          description: '大多数肉类和家禽是可以的，只要它们被正确烹饪，没有粉红色。应避免煮成三分熟的肉排和牛排。同样，如果您吃预制餐，确保它被正确加热，整个都滚烫。'
        },
        {
          name: '牛奶 (Milk)',
          status: '✅',
          description: '孕期饮用经过热处理杀死有害细菌的牛奶是安全的。这意味着您可以饮用巴氏杀菌、UHT、灭菌和奶粉。'
        },
        {
          name: '慕斯 (Mousse)',
          status: '⚠️',
          description: '孕期可以安全食用从超市或大型零售商购买的慕斯。它含有的任何鸡蛋都应该是巴氏杀菌的。自制慕斯通常含有生蛋，孕期应避免，因为有沙门氏菌风险。'
        },
        {
          name: '马苏里拉奶酪 (Mozzarella)',
          status: '✅',
          description: '孕期可以安全食用马苏里拉奶酪，前提是用巴氏杀菌牛奶制成。无论是用巴氏杀菌还是未杀菌牛奶制成的披萨或其他热菜上的熟马苏里拉都是可以的。'
        },
        {
          name: '贻贝 (Mussels)',
          status: '⚠️',
          description: '如果贻贝被正确烹饪并作为滚烫菜肴的一部分食用，如白葡萄酒贻贝、海鲜汤或鱼派，是可以食用的。罐装贻贝也是可以的。最好避免冷食的贻贝，除非您确定它们是新鲜烹饪和冷却的。'
        }
      ]
    },
    {
      letter: 'N',
      items: [
        {
          name: '荨麻茶 (Nettle tea)',
          status: '⚠️',
          description: '荨麻叶含有几种维生素和矿物质，包括叶酸、铁和钙。然而，荨麻茶被发现几乎不含或完全不含这些营养素。一些草药师推荐荨麻茶用于孕期，声称它提供各种好处：增强肾脏、减少腿部抽筋和分娩疼痛以及预防痔疮。没有证据支持这一点，但孕期饮用荨麻茶通常被认为是安全的。'
        },
        {
          name: '坚果 (Nuts)',
          status: '✅',
          description: '孕期可以安全食用杏仁、巴西坚果、榛子、花生、山核桃、核桃和其他种类的坚果，除非您对它们过敏。这适用于您怀孕、备孕或哺乳期间。'
        }
      ]
    },
    {
      letter: 'O',
      items: [
        {
          name: '油性鱼 (Oily fish)',
          status: '⚠️',
          description: '根据FSA，孕妇、哺乳期妇女或备孕妇女每周应吃一到两份油性鱼。油性鱼，如三文鱼和沙丁鱼，富含有益的omega-3脂肪酸，提供蛋白质和必需的维生素和矿物质。然而，您不应该吃太多，因为油性鱼可能含有高水平的二恶英和多氯联苯（PCBs）。'
        },
        {
          name: '橄榄 (Olives)',
          status: '⚠️',
          description: '孕期可以食用黑橄榄和绿橄榄，但它们往往含盐量很高，所以吃太多不是个好主意。'
        },
        {
          name: '生蚝 (Oysters)',
          status: '❌',
          description: '生蚝通常生吃，应该避免，因为有食物中毒风险。与其他生贝类一样，它们偶尔可能含有甲型肝炎。'
        }
      ]
    },
    {
      letter: 'P',
      items: [
        {
          name: '木瓜 (Papaya/pawpaw)',
          status: '✅',
          description: '木瓜是维生素A（作为β-胡萝卜素）和维生素C的良好来源，孕期或哺乳期间没有必要避免。'
        },
        {
          name: '帕玛森奶酪 (Parmesan cheese)',
          status: '✅',
          description: '无论是用巴氏杀菌还是未杀菌牛奶制成的，孕期都被认为是安全食用的。这是因为它是酸性的，含水量低，所以不是李斯特菌等细菌生长的合适环境。'
        },
        {
          name: '肝酱 (Pâté)',
          status: '❌',
          description: '孕期应避免任何含有肝脏的肝酱，因为它含有高水平的维生素A。其他类型的新鲜或冷藏肝酱，包括蔬菜肝酱，也应该避免，因为它们可能含有李斯特菌。'
        },
        {
          name: '花生 (Peanuts)',
          status: '✅',
          description: '也称为花生和猴子坚果。目前的政府建议是，如果您想在孕期或哺乳期吃花生，作为健康均衡饮食的一部分是可以的。'
        },
        {
          name: '薄荷茶 (Peppermint tea)',
          status: '✅',
          description: '孕期饮用薄荷茶是安全的。一些女性发现它有助于缓解消化不良、胃灼热、恶心和孕吐。'
        },
        {
          name: '费城奶酪 (Philadelphia cheese)',
          status: '✅',
          description: '孕期可以安全食用费城奶酪和其他品牌的奶油奶酪。'
        },
        {
          name: '菠萝 (Pineapple)',
          status: '✅',
          description: '您可能听说孕期应该避免菠萝，因为它可能导致流产，或者在孕晚期应该吃它来催产。事实是，在孕期任何阶段正常食用菠萝都极不可能产生任何影响。'
        },
        {
          name: '披萨 (Pizza)',
          status: '⚠️',
          description: '如果所有配料都正确烹饪，通常可以安全食用任何种类的披萨。这包括用山羊奶酪、斯蒂尔顿、戈尔根佐拉和任何其他种类的奶酪制作的披萨，前提是它们被煮至滚烫。应避免加帕尔马火腿的披萨，因为火腿是在烹饪后添加的，有食物中毒风险。'
        },
        {
          name: '虾 (Prawns)',
          status: '⚠️',
          description: '如果虾被正确烹饪并作为热餐的一部分食用，例如在咖喱或炒菜中，是安全食用的。如果沙拉或三明治中的冷虾已经煮熟然后冷却并保持冷藏直到食用，应该是安全的。'
        },
        {
          name: '益生菌 (Probiotics)',
          status: '✅',
          description: '这些是对健康有益的活微生物。孕期和哺乳期间饮用含有益生菌的产品是安全的。'
        }
      ]
    },
    {
      letter: 'Q',
      items: [
        {
          name: '乳蛋饼 (Quiche)',
          status: '⚠️',
          description: '商业制备的乳蛋饼孕期应该是安全食用的。如果您有任何疑问，不要冷食而是按照制造商的指南加热，并确保它整个都滚烫。自制乳蛋饼也应该仔细烹饪，以确保鸡蛋变得凝固。'
        },
        {
          name: '奎宁 (Quinine)',
          status: '⚠️',
          description: '汤力水和苦柠檬含有奎宁，孕期适量饮用是可以的。奎宁是一种用于治疗疟疾的药物，关于孕期是否应该使用存在一些争议。然而，汤力水中的含量与疟疾治疗使用的量相比微不足道。'
        },
        {
          name: '夸恩素肉 (Quorn)',
          status: '✅',
          description: '所有夸恩产品都含有真菌蛋白，适合素食者。与来自大豆的豆腐不同，真菌蛋白是真菌家族的一部分，像蘑菇一样。夸恩产品是植物蛋白的良好来源，脂肪含量低，还提供纤维。没有任何迹象表明夸恩产品不适合孕期或哺乳期间。'
        }
      ]
    },
    {
      letter: 'R',
      items: [
        {
          name: '覆盆子叶茶 (Raspberry leaf tea)',
          status: '⚠️',
          description: '在孕晚期服用覆盆子叶茶被认为有助于为分娩做好准备。覆盆子叶是子宫刺激剂，被认为可以增强子宫肌肉，这样当您有宫缩时，它们更有效，分娩更容易。不建议在怀孕约32周之前服用覆盆子叶茶。'
        },
        {
          name: '米饭 (Rice)',
          status: '⚠️',
          description: '一般来说，吃米饭是安全的，但要注意米饭沙拉和含有重新加热米饭的菜肴，如印度香饭、印度香饭和蛋炒饭。米饭可能含有蜡样芽孢杆菌的孢子，如果菜肴在室温下放置，孢子就会萌发。最好吃刚煮好的米饭。'
        },
        {
          name: '瑞可塔奶酪 (Ricotta)',
          status: '✅',
          description: '孕期可以安全食用瑞可塔奶酪，前提是用巴氏杀菌牛奶制成。'
        },
        {
          name: '罗克福奶酪 (Roquefort cheese)',
          status: '❌',
          description: '这是一种软蓝纹奶酪，孕期应避免，因为有李斯特菌风险。'
        }
      ]
    },
    {
      letter: 'S',
      items: [
        {
          name: '鼠尾草 (Sage)',
          status: '⚠️',
          description: '孕期或哺乳期间食用含有鼠尾草的食物是可以的。鼠尾草被认为具有类似雌激素的作用，大量服用时可能刺激子宫，因此孕期应避免鼠尾草油（用于芳香疗法）。'
        },
        {
          name: '沙拉 (Salad)',
          status: '⚠️',
          description: '沙拉是健康的选择，但重要的是所有成分都要彻底清洗，以降低食物中毒风险。袋装购买的预包装沙拉也应该清洗，即使它标注为已清洗和即食。'
        },
        {
          name: '三文鱼 (Salmon)',
          status: '⚠️',
          description: '三文鱼提供蛋白质、铁、维生素B6、B12和D，以及对宝宝有益的长链omega-3。然而，由于所有油性鱼都含有微量污染物，建议每周不要超过两份。'
        },
        {
          name: '沙丁鱼 (Sardines)',
          status: '⚠️',
          description: '这是一种油性鱼，是长链omega-3、铁、锌和维生素B12的良好来源。一罐沙丁鱼约含三分之二份油性鱼。因此，如果您不吃任何其他油性鱼，每周最多可以吃三罐沙丁鱼。'
        },
        {
          name: '海鲜 (Seafood)',
          status: '⚠️',
          description: '见贝类。'
        },
        {
          name: '海鲜棒 (Seafood sticks)',
          status: '✅',
          description: '有时被称为蟹棒或鱼棒。它们通常由加工过的白鱼和蟹味调味料等其他添加剂制成。只要保持冷藏，它们应该是安全食用的。'
        },
        {
          name: '贝类 (Shellfish)',
          status: '⚠️',
          description: '如果彻底煮熟并作为热餐的一部分食用，孕期可以食用贝类（包括虾、蛤蜊、扇贝、贻贝、小龙虾、海螺和小虾）。通常生吃的贝类，如生蚝、海螺和蛤蜊，应该避免，因为它们可能被有害细菌和病毒污染。'
        },
        {
          name: '烟熏鱼 (Smoked fish)',
          status: '⚠️',
          description: '在英国，孕期食用烟熏鱼被认为是安全的，包括烟熏三文鱼、烟熏鲭鱼和烟熏鳟鱼。然而，在2013年和2014年，FSA召回了几批烟熏三文鱼，因为发现它们含有李斯特菌。'
        },
        {
          name: '大豆 (Soya)',
          status: '✅',
          description: '作为正常健康饮食的一部分，食用大豆或豆腐和豆浆等产品没有问题。人们对大豆可能对胎儿发育产生的不良影响表示担忧，但这些并没有充分根据。'
        },
        {
          name: '菠菜 (Spinach)',
          status: '✅',
          description: '可以安全食用，是β-胡萝卜素、叶酸和维生素C的良好来源。然而，菠菜是铁的良好来源是一个误解：菠菜含有草酸，它与铁紧密结合，使大部分铁无法被吸收。'
        },
        {
          name: '斯蒂尔顿奶酪 (Stilton)',
          status: '⚠️',
          description: '这是一种蓝纹奶酪，但FSA认为孕期可以安全食用，因为它是硬的。这意味着它不像软奶酪那样含有那么多水分，所以细菌很难在里面生长。'
        },
        {
          name: '寿司 (Sushi)',
          status: '⚠️',
          description: '生养殖鱼在孕期被认为是安全食用的，但生野生鱼在食用前必须冷冻。冷冻会杀死野生鱼中可能存在的任何微小寄生虫，否则可能会让您生病。'
        },
        {
          name: '剑鱼 (Swordfish)',
          status: '❌',
          description: '剑鱼中发现了高水平的汞，建议孕妇完全不要食用。如果您正在哺乳，建议每周可以食用一份但不能更多。'
        }
      ]
    },
    {
      letter: 'T',
      items: [
        {
          name: '茶 (Tea)',
          status: '⚠️',
          description: '适量饮用普通红茶是可以的。然而，每杯含有约50毫克咖啡因，因此孕期每天不应超过约四杯。'
        },
        {
          name: '提拉米苏 (Tiramisu)',
          status: '⚠️',
          description: '孕期可以安全食用从超市或类似商店购买的提拉米苏。它含有的任何鸡蛋和奶油都将是巴氏杀菌的。自制提拉米苏的奶油配料中可能含有生蛋，因此应该避免。'
        },
        {
          name: '豆腐 (Tofu)',
          status: '✅',
          description: '孕期和哺乳期间食用豆腐是可以的。'
        },
        {
          name: '金枪鱼 (Tuna)',
          status: '⚠️',
          description: '适量食用金枪鱼是安全的。建议孕期每周不要超过两份新鲜金枪鱼（每份140克）或四罐200克罐头。'
        }
      ]
    },
    {
      letter: 'W',
      items: [
        {
          name: '水 (Water)',
          status: '✅',
          description: '所有成年人每天需要喝至少六到八杯液体。孕期您可能会注意到自己变得更渴。母乳喂养绝对是非常容易口渴的工作。'
        },
        {
          name: '葡萄酒 (Wine)',
          status: '❌',
          description: '不建议孕期饮用葡萄酒。'
        }
      ]
    }
  ];

  // 过滤食物数据
  const filteredFoods = foodGuideData.flatMap(category =>
    category.items.filter(item =>
      item.name.toLowerCase().includes(searchTerm.toLowerCase())
    )
  );

  return (
    <div className="food-guide-container">
      <div className="search-container">
        <input
          type="text"
          placeholder="搜索食物或食材..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="search-input"
        />
      </div>

      <div className="guide-content">
        {searchTerm ? (
          // 搜索结果展示
          <div className="search-results">
            <h2>搜索结果</h2>
            {filteredFoods.length > 0 ? (
              <div className="food-cards">
                {filteredFoods.map((food, index) => (
                  <div key={index} className={`food-card ${food.status}`}>
                    <div className="food-header">
                      <div className="food-name">{food.name}</div>
                      <div className="food-status">{food.status}</div>
                    </div>
                    <div className="food-description">{food.description}</div>
                  </div>
                ))}
              </div>
            ) : (
              <div className="no-results">
                <p>未找到匹配的食物或食材</p>
              </div>
            )}
          </div>
        ) : (
          // 完整A-Z指南展示
          <div className="full-guide">
            {foodGuideData.map((category, index) => (
              <div key={index} className="letter-section">
                <h2 className="letter-header">{category.letter}</h2>
                <div className="food-cards">
                  {category.items.map((food, foodIndex) => (
                    <div key={foodIndex} className={`food-card ${food.status}`}>
                      <div className="food-header">
                        <div className="food-name">{food.name}</div>
                        <div className="food-status">{food.status}</div>
                      </div>
                      <div className="food-description">{food.description}</div>
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      <style jsx>{`
        .food-guide-container {
          font-family: 'Arial', sans-serif;
          padding: 20px;
        }

        .search-container {
          margin-bottom: 20px;
        }

        .search-input {
          width: 100%;
          padding: 10px;
          font-size: 16px;
          border: 1px solid #ddd;
          border-radius: 5px;
        }

        .guide-content {
          max-width: 800px;
          margin: 0 auto;
        }

        .letter-section {
          margin-bottom: 40px;
        }

        .letter-header {
          font-size: 24px;
          font-weight: bold;
          color: #3e3065;
          margin-bottom: 20px;
          padding-bottom: 10px;
          border-bottom: 2px solid #3e3065;
        }

        .food-cards {
          display: grid;
          grid-template-columns: 1fr;
          gap: 15px;
        }

        .food-card {
          background-color: #fff;
          border: 2px solid #ddd;
          border-radius: 8px;
          padding: 15px;
          box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }

        .food-card.✅ {
          border-left: 5px solid #2ecc71;
        }

        .food-card.❌ {
          border-left: 5px solid #e74c3c;
        }

        .food-card.⚠️ {
          border-left: 5px solid #f1c40f;
        }

        .food-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin-bottom: 10px;
        }

        .food-name {
          font-size: 18px;
          font-weight: bold;
        }

        .food-status {
          font-size: 24px;
        }

        .food-description {
          line-height: 1.6;
          color: #555;
        }

        .search-results h2 {
          color: #3e3065;
        }

        .no-results {
          text-align: center;
          padding: 40px;
          color: #888;
        }

        @media (min-width: 768px) {
          .food-cards {
            grid-template-columns: 1fr 1fr;
          }
        }
      `}</style>
    </div>
  );
};

export default FoodGuide;