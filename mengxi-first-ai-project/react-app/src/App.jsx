import { useState } from 'react';
import Home from './modules/Home/Home';
import Kitchen from './modules/Kitchen/Kitchen';
import Knowledge from './modules/Knowledge/Knowledge';
import FoodGuide from './modules/FoodGuide/FoodGuide';
import './App.css';

// 顶部 TabBar 组件
const TopBar = ({ currentTab, onTabChange }) => {
  const tabs = [
    { id: 'HOME', label: '👶 首页', color: '#3e3065' },
    { id: 'KITCHEN', label: '🍳 厨房', color: '#8cc5a3' },
    { id: 'KNOWLEDGE', label: '📚 知识库', color: '#f7d26e' },
    { id: 'WELLNESS', label: '💪 健康', color: '#f27c7c' },
    { id: 'FOOD_GUIDE', label: '📖 食物指南', color: '#9b59b6' }
  ];

  return (
    <div style={{ display: 'flex', justifyContent: 'center', padding: '20px 0', marginBottom: '20px' }}>
      {tabs.map(tab => (
        <button
          key={tab.id}
          onClick={() => onTabChange(tab.id)}
          style={{
            padding: '12px 24px',
            margin: '0 8px',
            borderRadius: '0',
            border: '2px solid #3e3065',
            backgroundColor: currentTab === tab.id ? tab.color : '#fff',
            color: currentTab === tab.id ? '#fff' : '#3e3065',
            fontSize: '14px',
            fontWeight: 'bold',
            cursor: 'pointer',
            boxShadow: currentTab === tab.id ? '4px 4px 0 0 rgba(62, 48, 101, 0.5)' : '2px 2px 0 0 rgba(62, 48, 101, 0.3)'
          }}
        >
          {tab.label}
        </button>
      ))}
    </div>
  );
};

function App() {
  const [currentTab, setCurrentTab] = useState('HOME');

  // 更新 renderContent 函数
  const renderContent = () => {
    switch (currentTab) {
      case 'HOME':
        return <Home />;
      case 'KITCHEN':
        return <Kitchen />;
      case 'KNOWLEDGE':
        return <Knowledge />;
      case 'WELLNESS':
        return <div style={{ textAlign: 'center', padding: '40px' }}><h2>Wellness Module (Coming Soon...)</h2></div>;
      case 'FOOD_GUIDE':
        return <FoodGuide />;
      default:
        return <Home />;
    }
  };

  return (
    <div style={{ maxWidth: '800px', margin: '0 auto', padding: '0 20px' }}>
      <TopBar currentTab={currentTab} onTabChange={setCurrentTab} />
      {renderContent()}
    </div>
  );
}

export default App
