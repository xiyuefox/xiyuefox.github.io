import React, { useState } from 'react';

const FoodQuest = () => {
  // 游戏状态
  const [currentHealth, setCurrentHealth] = useState(100);
  const [itemsCollected, setItemsCollected] = useState(0);
  const [animatingItem, setAnimatingItem] = useState(null);

  // 音效播放辅助函数
  const playSound = (audioId) => {
    try {
      const audioElement = document.getElementById(audioId);
      if (audioElement) {
        audioElement.currentTime = 0;
        const playPromise = audioElement.play();
        if (playPromise) {
          playPromise.catch(() => {
            // 自动播放被浏览器阻止时的静默失败
          });
        }
      }
    } catch (error) {
      // 忽略音效播放错误
    }
  };

  // 处理食物点击
  const handleFoodClick = (itemId, itemType) => {
    // 设置动画状态
    setAnimatingItem(itemId);

    // 播放相应音效
    if (itemType === 'good') {
      playSound('sfx-good');
    } else {
      playSound('sfx-bad');
    }

    // 更新游戏状态
    if (itemType === 'good') {
      setCurrentHealth(prev => Math.min(100, prev + 5));
      setItemsCollected(prev => prev + 1);
    } else {
      setCurrentHealth(prev => Math.max(0, prev - 10));
    }

    // 移除动画状态
    setTimeout(() => {
      setAnimatingItem(null);
    }, 500);
  };

  // 处理鼠标悬停
  const handleMouseEnter = () => {
    playSound('sfx-hover');
  };

  return (
    <div className="food-quest-container">
      {/* 音效资源预加载 */}
      <audio id="sfx-hover" src="https://via.placeholder.com/1" preload="auto"></audio>
      <audio id="sfx-good" src="https://via.placeholder.com/1" preload="auto"></audio>
      <audio id="sfx-bad" src="https://via.placeholder.com/1" preload="auto"></audio>

      {/* 顶部标题栏 */}
      <header className="header pixel-box">
        <div className="header-left">
          <img src="https://via.placeholder.com/48x48?text=Mom" alt="Mom Avatar" className="avatar" />
          <div>
            <div>PLAYER 1:</div>
            <div>PREGNANT</div>
          </div>
        </div>
        <h1 className="title">PIXEL FOOD QUEST</h1>
        <div className="status">WEEK: 12</div>
      </header>

      {/* 主体内容区 (三栏布局) */}
      <main className="main-container">
        {/* 左列：绿色安全区 */}
        <section className="pixel-box zone-green">
          <div className="zone-header">✔ LEVEL 1: SAFE</div>
          <div className="food-grid">
            {/* 食物项 1 - 硬奶酪 */}
            <div
              className="food-item"
              onMouseEnter={handleMouseEnter}
              onClick={() => handleFoodClick('cheese', 'good')}
            >
              <img
                src="https://via.placeholder.com/64x64?text=Cheese"
                alt="Hard Cheese"
                className={`food-icon ${animatingItem === 'cheese' ? 'collect-success' : ''}`}
              />
              <div className="food-name">HARD/PAST. CHEESE</div>
              {/* 详情弹窗 */}
              <div className="tooltip-box">
                <div className="tooltip-title">巴氏杀菌乳品</div>
                <div className="tooltip-content">
                  <img src="https://via.placeholder.com/32x32?text=Cow" alt="" className="tooltip-sprite" />
                  <div>安全! 硬奶酪(如Cheddar)水分少。软奶酪只要是巴氏杀菌(Pasteurized)均可食用。</div>
                </div>
              </div>
            </div>

            {/* 食物项 2 - 熟鸡肉 */}
            <div
              className="food-item"
              onMouseEnter={handleMouseEnter}
              onClick={() => handleFoodClick('chicken', 'good')}
            >
              <img
                src="https://via.placeholder.com/64x64?text=Chicken"
                alt="Cooked Meat"
                className={`food-icon ${animatingItem === 'chicken' ? 'collect-success' : ''}`}
              />
              <div className="food-name">COOKED MEAT</div>
              <div className="tooltip-box">
                <div className="tooltip-title">彻底煮熟的肉类</div>
                <div className="tooltip-content">
                  <img src="https://via.placeholder.com/32x32?text=Thermometer" alt="" className="tooltip-sprite" />
                  <div>无粉红色! 必须煮至滚烫，肉汁清澈。冷吃熟肉也是安全的。</div>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* 中列：红色危险区 */}
        <section className="pixel-box zone-red">
          <div className="zone-header">❌ LEVEL 2: AVOID</div>
          <div className="food-grid">
            {/* 食物项 3 - 发霉软奶酪 */}
            <div
              className="food-item"
              onMouseEnter={handleMouseEnter}
              onClick={() => handleFoodClick('moldy-cheese', 'bad')}
            >
              <img
                src="https://via.placeholder.com/64x64?text=Moldy+Cheese"
                alt="Moldy Cheese"
                className={`food-icon ${animatingItem === 'moldy-cheese' ? 'collect-fail' : ''}`}
              />
              <div className="food-name">MOULDY SOFT CHEESE</div>
              <div className="tooltip-box tooltip-box--red">
                <div className="tooltip-title tooltip-title--red">发霉成熟软奶酪</div>
                <div className="tooltip-content">
                  <img src="https://via.placeholder.com/32x32?text=Slime" alt="Listeria" className="tooltip-sprite" />
                  <div>危险BOSS: Brie, Blue Cheese。可能藏有李斯特菌。除非高温烤熟!</div>
                </div>
              </div>
            </div>

            {/* 食物项 4 - 生肉 */}
            <div
              className="food-item"
              onMouseEnter={handleMouseEnter}
              onClick={() => handleFoodClick('raw-meat', 'bad')}
            >
              <img
                src="https://via.placeholder.com/64x64?text=Raw+Meat"
                alt="Raw Meat"
                className={`food-icon ${animatingItem === 'raw-meat' ? 'collect-fail' : ''}`}
              />
              <div className="food-name">RAW MEAT/EGGS</div>
              <div className="tooltip-box tooltip-box--red">
                <div className="tooltip-title tooltip-title--red">生食/半生食</div>
                <div className="tooltip-content">
                  <img src="https://via.placeholder.com/32x32?text=Bacteria" alt="Bacteria" className="tooltip-sprite" />
                  <div>陷阱! 避免生鸡蛋、半熟牛排。风险: 沙门氏菌和弓形虫感染。</div>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* 右列：黄色谨慎区 */}
        <section className="pixel-box zone-yellow">
          <div className="zone-header">! LEVEL 3: MODERATE</div>
          <div className="food-grid">
            {/* 食物项 5 - 油性鱼类 */}
            <div
              className="food-item"
              onMouseEnter={handleMouseEnter}
              onClick={() => handleFoodClick('oily-fish', 'caution')}
            >
              <img
                src="https://via.placeholder.com/64x64?text=Fish"
                alt="Oily Fish"
                className={`food-icon ${animatingItem === 'oily-fish' ? 'collect-fail' : ''}`}
              />
              <div className="food-name">OILY FISH (Limit)</div>
              <div className="tooltip-box tooltip-box--yellow">
                <div className="tooltip-title tooltip-title--yellow">富含油脂鱼类</div>
                <div className="tooltip-content">
                  <img src="https://via.placeholder.com/32x32?text=Omega3" alt="Omega-3" className="tooltip-sprite" />
                  <div>三文鱼等富含Omega-3。因污染物风险，**每周限额: 最多2份**。</div>
                </div>
              </div>
            </div>

            {/* 食物项 6 - 咖啡 */}
            <div
              className="food-item"
              onMouseEnter={handleMouseEnter}
              onClick={() => handleFoodClick('coffee', 'caution')}
            >
              <img
                src="https://via.placeholder.com/64x64?text=Coffee"
                alt="Caffeine"
                className={`food-icon ${animatingItem === 'coffee' ? 'collect-fail' : ''}`}
              />
              <div className="food-name">CAFFEINE (Limit)</div>
              <div className="tooltip-box tooltip-box--yellow">
                <div className="tooltip-title tooltip-title--yellow">咖啡因计量槽</div>
                <div className="tooltip-content">
                  <img src="https://via.placeholder.com/32x32?text=Heart" alt="Heart" className="tooltip-sprite" />
                  <div>每日限额: 200mg! 计算所有来源: 咖啡, 茶, 可乐, 巧克力。不要超标!</div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>

      {/* 底部状态与攻略栏 */}
      <footer className="footer-container">
        {/* 玩家状态/库存栏 */}
        <div className="player-stats pixel-box">
          <div className="stat-item">
            <span className="stat-label">HEALTH:</span>
            {/* 健康血条 */}
            <div className="health-bar-container">
              <div
                id="health-bar"
                className="health-bar-fill"
                style={{
                  width: `${currentHealth}%`,
                  backgroundColor: currentHealth > 50 ? '#2ecc71' : currentHealth > 20 ? '#f1c40f' : '#e74c3c'
                }}
              ></div>
            </div>
            <span id="health-text">{currentHealth}%</span>
          </div>
          <div className="stat-item">
            <span className="stat-label">INVENTORY:</span>
            <span id="inventory-count">{itemsCollected} ITEMS</span>
          </div>
        </div>

        {/* 滚动攻略栏 */}
        <div className="footer pixel-box">
          <div className="scrolling-text">
            *** GAME TIP: 如有疑问，使用终极技能：彻底煮熟 (COOK THOROUGHLY)! *** 保持手部卫生! *** 酒精是绝对禁忌的Debuff! *** 咨询你的NPC医生获取建议! ***
          </div>
        </div>
      </footer>

      <style jsx>{`
        /* --- 全局像素风格设置 --- */
        :root {
            --bg-color: #2c3e50; /* 深色背景，模拟游戏机卡带 */
            --text-color: #ecf0f1;
            --green-zone: #2ecc71;
            --red-zone: #e74c3c;
            --yellow-zone: #f1c40f;
            --border-color: #34495e;
            --pixel-size: 2px; /* 控制整体像素颗粒感大小 */
        }

        .food-quest-container {
            font-family: 'Press Start 2P', cursive, monospace; /* 使用像素字体 */
            background-color: var(--bg-color);
            color: var(--text-color);
            padding: 20px;
            line-height: 1.5;
            image-rendering: pixelated; /* 关键：强制图片像素化渲染，不模糊 */
        }

        /* 通用像素边框样式 */
        .pixel-box {
            background-color: #34495e;
            border: calc(var(--pixel-size) * 2) solid var(--border-color);
            padding: 15px;
            box-shadow:
                inset calc(var(--pixel-size) * -1) calc(var(--pixel-size) * -1) 0 0 #2c3e50,
                inset var(--pixel-size) var(--pixel-size) 0 0 #7f8c8d;
        }

        /* --- 顶部标题栏 --- */
        .header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 20px;
            background-color: #2980b9;
            padding: 10px 20px;
        }

        .header-left {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .avatar {
            width: 48px;
            height: 48px;
            background-color: #ddd;
            border-radius: 4px;
        }

        .title {
            font-size: 1.2rem;
            text-align: center;
            flex-grow: 1;
            margin: 0;
        }

        .status {
            font-size: 0.8rem;
        }

        /* --- 主体布局 (响应式) --- */
        .main-container {
            display: grid;
            grid-template-columns: 1fr; /* 移动端默认单列 */
            gap: 20px;
        }

        /* 桌面端切换为三列 */
        @media (min-width: 768px) {
            .main-container {
                grid-template-columns: 1fr 1fr 1fr;
            }
        }

        /* --- 区域样式 (Zone Styles) --- */
        .zone-header {
            font-size: 1rem;
            margin-bottom: 15px;
            padding: 10px;
            text-align: center;
            color: #000;
            border-bottom: calc(var(--pixel-size) * 2) solid rgba(0,0,0,0.2);
        }

        .zone-green .zone-header {
            background-color: var(--green-zone);
        }

        .zone-red .zone-header {
            background-color: var(--red-zone);
        }

        .zone-yellow .zone-header {
            background-color: var(--yellow-zone);
        }

        /* --- 食物图标网格 --- */
        .food-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(80px, 1fr));
            gap: 15px;
        }

        /* --- 食物项与弹窗交互 --- */
        .food-item {
            position: relative; /* 为绝对定位的弹窗做参照 */
            display: flex;
            flex-direction: column;
            align-items: center;
            cursor: pointer;
            text-align: center;
        }

        .food-icon {
            width: 64px;
            height: 64px;
            background-color: rgba(0,0,0,0.3); /* 图标占位背景 */
            margin-bottom: 8px;
            border: var(--pixel-size) solid rgba(255,255,255,0.3);
            transition: transform 0.1s;
        }

        .food-item:hover .food-icon {
            transform: scale(1.05); /* 悬停轻微放大效果 */
            border-color: #fff;
        }

        .food-name {
            font-size: 0.7rem;
        }

        /* --- 详情弹窗 (Tooltip Box) --- */
        .tooltip-box {
            visibility: hidden; /* 默认隐藏 */
            opacity: 0;
            position: absolute;
            bottom: 100%; /* 显示在图标上方 */
            left: 50%;
            transform: translateX(-50%);
            width: 220px;
            background-color: #2c3e50;
            border: calc(var(--pixel-size) * 2) solid #fff;
            padding: 10px;
            z-index: 10;
            font-size: 0.7rem;
            text-align: left;
            transition: opacity 0.2s, visibility 0.2s;
            pointer-events: none; /* 防止鼠标滑到弹窗上导致闪烁 */
            box-shadow: 0 4px 8px rgba(0,0,0,0.5);
        }

        /* 鼠标悬停在食物项上时显示弹窗 */
        .food-item:hover .tooltip-box {
            visibility: visible;
            opacity: 1;
        }

        /* 红色和黄色弹窗样式 */
        .tooltip-box--red {
            border-color: var(--red-zone);
        }

        .tooltip-box--yellow {
            border-color: var(--yellow-zone);
        }

        /* 弹窗内部样式 */
        .tooltip-title {
            font-size: 0.8rem;
            color: var(--yellow-zone);
            margin-bottom: 8px;
            border-bottom: var(--pixel-size) dashed #7f8c8d;
            padding-bottom: 5px;
        }

        .tooltip-title--red {
            color: var(--red-zone);
        }

        .tooltip-title--yellow {
            color: var(--yellow-zone);
        }

        .tooltip-content {
            display: flex;
            align-items: flex-start;
            gap: 10px;
        }

        .tooltip-sprite {
            width: 32px;
            height: 32px;
            background-color: rgba(255,255,255,0.1); /* 占位 */
            flex-shrink: 0;
        }

        /* --- 底部容器调整 --- */
        .footer-container {
            margin-top: 20px;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        /* 玩家状态栏 */
        .player-stats {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #222;
            color: #fff;
            font-size: 0.8rem;
        }
        .stat-item {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .stat-label { color: var(--yellow-zone); }

        /* 像素血条 */
        .health-bar-container {
            width: 150px;
            height: 16px;
            background-color: #555;
            border: var(--pixel-size) solid #000;
            overflow: hidden;
        }
        .health-bar-fill {
            height: 100%;
            transition: width 0.3s, background-color 0.3s;
        }

        /* 点击反馈动画 */
        @keyframes pulse-green {
            0% { box-shadow: 0 0 0 0 rgba(46, 204, 113, 0.7); }
            70% { box-shadow: 0 0 0 15px rgba(46, 204, 113, 0); }
            100% { box-shadow: 0 0 0 0 rgba(46, 204, 113, 0); }
        }
        @keyframes shake-red {
            0% { transform: translate(1px, 1px) rotate(0deg); }
            10% { transform: translate(-1px, -2px) rotate(-1deg); }
            20% { transform: translate(-3px, 0px) rotate(1deg); }
            30% { transform: translate(3px, 2px) rotate(0deg); }
            40% { transform: translate(1px, -1px) rotate(1deg); }
            50% { transform: translate(-1px, 2px) rotate(-1deg); }
            60% { transform: translate(-3px, 1px) rotate(0deg); }
            70% { transform: translate(3px, 1px) rotate(-1deg); }
            80% { transform: translate(-1px, -1px) rotate(1deg); }
            90% { transform: translate(1px, 2px) rotate(0deg); }
            100% { transform: translate(1px, -2px) rotate(-1deg); }
        }

        /* 点击成功/失败的类 */
        .collect-success {
            animation: pulse-green 0.5s linear;
            border-color: var(--green-zone);
        }
        .collect-fail {
            animation: shake-red 0.5s linear;
            border-color: var(--red-zone);
        }

        /* --- 底部状态栏 --- */
        .footer {
            margin-top: 20px;
            background-color: #000;
            color: var(--green-zone);
            padding: 10px;
            font-size: 0.7rem;
            white-space: nowrap;
            overflow: hidden;
        }

        /* 简单的滚动文字动画 */
        .scrolling-text {
            display: inline-block;
            padding-left: 100%;
            animation: scroll 20s linear infinite;
        }

        @keyframes scroll {
            0% {
                transform: translateX(0);
            }
            100% {
                transform: translateX(-100%);
            }
        }
      `}</style>
    </div>
  );
};

export default FoodQuest;