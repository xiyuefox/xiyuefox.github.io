import React, { useState } from 'react';

// 像素风格知识库组件
const Knowledge = () => {
  // 模拟知识卡片数据
  const [knowledgeCards, setKnowledgeCards] = useState([
    {
      id: 1,
      title: '营养 CH.3: 蛋白质需求',
      category: '健康与饮食',
      summary: '重点关注优质蛋白质来源: 瘦肉、豆类、鱼类。怀孕期每天增加25克蛋白质。',
      tags: ['#饮食', '#怀孕']
    },
    {
      id: 2,
      title: '睡眠模式与作息',
      category: '睡眠与作息',
      summary: '建立一致的睡眠习惯: 每天同一时间上床睡觉和起床。',
      tags: ['#睡眠', '#健康']
    },
    {
      id: 3,
      title: '正念练习',
      category: '正念与压力',
      summary: '每日深呼吸技巧。',
      tags: ['#正念', '#压力']
    }
  ]);

  const [newNote, setNewNote] = useState('');

  // 模拟添加新卡片
  const handleAddCard = () => {
    if (newNote.trim()) {
      const newCard = {
        id: knowledgeCards.length + 1,
        title: '新笔记',
        category: '未分类',
        summary: newNote.trim(),
        tags: ['#新笔记']
      };
      setKnowledgeCards([...knowledgeCards, newCard]);
      setNewNote('');
    }
  };

  // 模拟删除卡片
  const handleDeleteCard = (id) => {
    setKnowledgeCards(knowledgeCards.filter(card => card.id !== id));
  };

  // 像素风格容器
  const containerStyle = {
    display: 'flex',
    gap: '20px',
    backgroundColor: '#fff',
    padding: '15px',
    border: '2px solid #3e3065',
    boxShadow: '2px 2px 0 0 rgba(62, 48, 101, 0.5)'
  };

  // 侧边栏样式
  const sidebarStyle = {
    width: '250px',
    padding: '15px',
    backgroundColor: '#f0e6d2',
    border: '2px solid #3e3065',
    boxShadow: '2px 2px 0 0 rgba(62, 48, 101, 0.5)'
  };

  // 主内容区样式
  const mainContentStyle = {
    flex: 1,
    padding: '15px',
    backgroundColor: '#f0e6d2',
    border: '2px solid #3e3065',
    boxShadow: '2px 2px 0 0 rgba(62, 48, 101, 0.5)'
  };

  // 知识卡片样式
  const cardStyle = {
    marginBottom: '15px',
    padding: '15px',
    backgroundColor: '#fffef8',
    border: '2px solid #3e3065',
    boxShadow: '2px 2px 0 0 rgba(62, 48, 101, 0.5)'
  };

  // 按钮样式
  const buttonStyle = {
    padding: '5px 10px',
    marginRight: '5px',
    backgroundColor: '#8cc5a3',
    color: 'white',
    border: '2px solid #3e3065',
    boxShadow: '2px 2px 0 0 rgba(62, 48, 101, 0.5)',
    cursor: 'pointer',
    fontSize: '12px'
  };

  const deleteButtonStyle = {
    ...buttonStyle,
    backgroundColor: '#f27c7c'
  };

  return (
    <div>
      {/* 模块标题 */}
      <h2 style={{ textAlign: 'center', borderBottom: '2px dashed #3e3065', paddingBottom: '10px', marginBottom: '20px' }}>
        📚 知识库 (O'Reilly风格)
      </h2>

      {/* 主容器 */}
      <div style={containerStyle}>
        {/* 侧边栏 */}
        <div style={sidebarStyle}>
          {/* 导航 */}
          <div style={{ marginBottom: '20px' }}>
            <div style={{ fontSize: '14px', fontWeight: 'bold', marginBottom: '10px', color: '#3e3065' }}>
              <span style={{ fontSize: '16px', marginRight: '5px' }}>📋</span> 导航
            </div>
            <div style={{ marginBottom: '5px' }}>▶ 仪表盘</div>
            <div style={{ marginBottom: '5px' }}>▶ 每日任务</div>
            <div style={{ marginBottom: '5px' }}>▶ 膳食计划</div>
            <div style={{ marginBottom: '5px' }}>▶ 我的笔记 (O'Reilly)</div>
          </div>

          {/* 分类 */}
          <div>
            <div style={{ fontSize: '14px', fontWeight: 'bold', marginBottom: '10px', color: '#3e3065' }}>
              <span style={{ fontSize: '16px', marginRight: '5px' }}>📁</span> 分类
            </div>
            <div style={{ marginBottom: '5px' }}>▶ 健康与饮食</div>
            <div style={{ marginBottom: '5px' }}>▶ 睡眠与作息</div>
            <div style={{ marginBottom: '5px' }}>▶ 正念与压力</div>
          </div>
        </div>

        {/* 主内容区 */}
        <div style={mainContentStyle}>
          {/* 搜索栏 */}
          <div style={{ marginBottom: '20px' }}>
            <input
              type="text"
              placeholder="搜索笔记..."
              style={{
                width: '300px',
                padding: '8px',
                border: '2px solid #3e3065',
                backgroundColor: '#fff',
                boxShadow: '2px 2px 0 0 rgba(62, 48, 101, 0.5)',
                fontSize: '14px'
              }}
            />
          </div>

          {/* 知识库卡片 */}
          <div style={{ marginBottom: '20px' }}>
            <div style={{ fontSize: '14px', fontWeight: 'bold', marginBottom: '15px', color: '#3e3065' }}>
              <span style={{ fontSize: '16px', marginRight: '5px' }}>🗂️</span> 知识卡片
            </div>

            {knowledgeCards.map(card => (
              <div key={card.id} style={cardStyle}>
                <div style={{ fontSize: '14px', fontWeight: 'bold', marginBottom: '5px', color: '#3e3065' }}>
                  卡片 {card.id}: {card.title}
                </div>
                <div style={{ fontSize: '12px', marginBottom: '5px' }}>
                  <span style={{ fontWeight: 'bold' }}>分类:</span> {card.category}
                </div>
                <div style={{ fontSize: '12px', marginBottom: '5px' }}>
                  <span style={{ fontWeight: 'bold' }}>摘要:</span> {card.summary}
                </div>
                <div style={{ fontSize: '11px', marginBottom: '10px', color: '#666' }}>
                  <span style={{ fontWeight: 'bold' }}>标签:</span> {card.tags.join(' ')}
                </div>
                <div>
                  <button style={buttonStyle}>编辑</button>
                  <button style={deleteButtonStyle} onClick={() => handleDeleteCard(card.id)}>删除</button>
                </div>
              </div>
            ))}
          </div>

          {/* 新建卡片区域 */}
          <div>
            <div style={{ fontSize: '14px', fontWeight: 'bold', marginBottom: '15px', color: '#3e3065' }}>
              <span style={{ fontSize: '16px', marginRight: '5px' }}>✏️</span> 创建新卡片
            </div>

            <textarea
              value={newNote}
              onChange={(e) => setNewNote(e.target.value)}
              placeholder="在此粘贴您的O'Reilly笔记以创建新卡片..."
              style={{
                width: '100%',
                height: '100px',
                padding: '10px',
                border: '2px solid #3e3065',
                backgroundColor: '#fff',
                boxShadow: '2px 2px 0 0 rgba(62, 48, 101, 0.5)',
                fontSize: '14px',
                resize: 'none',
                boxSizing: 'border-box',
                marginBottom: '15px'
              }}
            />

            <button
              onClick={handleAddCard}
              style={{
                ...buttonStyle,
                fontSize: '14px',
                padding: '10px 20px'
              }}
            >
              [ + 添加像素卡片 ]
            </button>
          </div>
        </div>
      </div>

      {/* 状态栏 */}
      <div style={{
        marginTop: '20px',
        padding: '5px 15px',
        backgroundColor: '#3e3065',
        color: '#fff',
        fontSize: '12px',
        border: '2px solid #3e3065',
        boxShadow: '2px 2px 0 0 rgba(62, 48, 101, 0.5)'
      }}>
        O'REILLY笔记已加载，准备好快照分享。
      </div>
    </div>
  );
};

export default Knowledge;