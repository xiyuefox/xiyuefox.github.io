import React, { useState, useEffect } from 'react';
import dayjs from 'dayjs';
import {
  getCurrentWeekDays,
  formatDateForDisplay,
  formatDateForKey,
  isToday
} from '../../utils/dateHelper';
import { getData, setData } from '../../utils/storage';
import MealEditModal from './MealEditModal';

// 复用 Home 里的 PixelCard 组件 (实际项目中应提取到 shared 目录)
const PixelCard = ({ title, children, style, onClick }) => (
  <div className="pixel-border" onClick={onClick} style={{
    padding: '15px',
    backgroundColor: '#fffef8',
    marginBottom: '15px',
    cursor: onClick ? 'pointer' : 'default',
    ...style
  }}>
    {title && <h3 style={{ marginTop: 0, borderBottom: '2px solid #e0d6c2', paddingBottom: '10px' }}>{title}</h3>}
    {children}
  </div>
);

const Kitchen = () => {
  const [weekDays, setWeekDays] = useState([]);
  const [selectedDate, setSelectedDate] = useState(dayjs()); // 默认选中今天
  const [mealsData, setMealsData] = useState({}); // 存储所有加载过的食谱数据
  // 编辑弹窗状态
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingMeal, setEditingMeal] = useState({ type: null, value: '' });

  // 初始化：获取本周日期并加载数据
  useEffect(() => {
    const days = getCurrentWeekDays();
    setWeekDays(days);
    loadAllMealsData();
  }, []);

  // 加载所有已存储的食谱数据
  const loadAllMealsData = async () => {
    const savedMeals = await getData('meals') || {};
    setMealsData(savedMeals);
  };

  // 获取选中日期的食谱数据
  const selectedDateKey = formatDateForKey(selectedDate);
  const currentMeals = mealsData[selectedDateKey] || { breakfast: '', lunch: '', dinner: '' };

  // 处理日期点击
  const handleDateClick = (date) => {
    setSelectedDate(date);
  };

  // 打开编辑弹窗
  const openEditModal = (type, value) => {
    setEditingMeal({ type, value });
    setIsModalOpen(true);
  };

  // 保存编辑后的餐点
  const handleSaveMeal = async (type, newValue) => {
    const dateKey = formatDateForKey(selectedDate);
    // 更新状态
    const updatedMealsData = {
      ...mealsData,
      [dateKey]: {
        ...mealsData[dateKey],
        [type]: newValue,
      },
    };
    setMealsData(updatedMealsData);
    // 保存到本地存储
    await setData('meals', updatedMealsData);
  };

  // --- 快照分享核心逻辑 ---
  const handleSnapshotShare = async () => {
    // 1. 构建分享文本内容
    const dateStr = formatDateForDisplay(selectedDate);
    let shareText = `🌱 [小橙宝] 今日食谱快照 (${dateStr})\n\n`;

    shareText += `🌞 早餐: ${currentMeals.breakfast || '待定'}\n`;
    shareText += `☀️ 午餐: ${currentMeals.lunch || '待定'}\n`;
    shareText += `🌙 晚餐: ${currentMeals.dinner || '待定'}\n`;

    shareText += `\n(复制这条信息去买菜/做饭吧~ 📷)`;

    // 2. 写入系统剪贴板
    try {
      await navigator.clipboard.writeText(shareText);
      // 3. 给出简单的反馈 (像素风提示)
      alert('✅ 像素快照已生成！\n\n文本已复制到剪贴板，快去粘贴分享吧！');
    } catch (err) {
      console.error('复制失败:', err);
      alert('❌ 复制失败，请手动复制。');
    }
  };

  return (
    <div>
      {/* --- 顶部操作栏：周历 + 分享按钮 --- */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'start', marginBottom: '20px' }}>
        {/* 周历组件 */}
        <div className="pixel-border" style={{ display: 'flex', backgroundColor: '#f0e6d2' }}>
          {weekDays.map(date => {
            const isSelected = date.isSame(selectedDate, 'day');
            const isTodayDate = isToday(date);
            return (
              <div
                key={date.toString()}
                onClick={() => handleDateClick(date)}
                style={{
                  padding: '8px 12px',
                  cursor: 'pointer',
                  textAlign: 'center',
                  backgroundColor: isSelected ? '#3e3065' : 'transparent',
                  color: isSelected ? 'white' : (isTodayDate ? '#3e3065' : 'inherit'),
                  fontWeight: isSelected || isTodayDate ? 'bold' : 'normal',
                  borderRight: '2px solid #e0d6c2',
                  minWidth: '60px'
                }}
              >
                <div style={{ fontSize: '0.9em' }}>{formatDateForDisplay(date).split(' ')[0]}</div>
                <div>{formatDateForDisplay(date).split(' ')[1]}</div>
              </div>
            );
          })}
        </div>

        {/* 独立的快照分享按钮 */}
        <button className="pixel-border" onClick={handleSnapshotShare} style={{
          padding: '10px 15px',
          backgroundColor: '#8cc5a3', // 薄荷绿
          color: 'white',
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          height: '100%'
        }}>
          <span style={{ fontSize: '24px' }}>📷</span>
          <span style={{ fontSize: '10px', marginTop: '4px' }}>分享快照</span>
        </button>
      </div>

      {/* --- 每日餐点卡片 (可点击编辑) --- */}
      <h3 style={{ textAlign: 'center', marginBottom: '20px', borderBottom: '2px dashed #3e3065', paddingBottom: '10px' }}>
         今日菜单: {formatDateForDisplay(selectedDate)}
         <span style={{ fontSize: '0.7em', fontWeight: 'normal', marginLeft: '10px' }}>(点击卡片编辑)</span>
      </h3>

      {/* 早餐卡片 */}
      <PixelCard
        title="🌞 早餐 (Breakfast)"
        onClick={() => openEditModal('breakfast', currentMeals.breakfast)}
        style={{ backgroundColor: '#fff8e1' }} // 浅黄背景
      >
        <div style={{ minHeight: '30px', fontStyle: currentMeals.breakfast ? 'normal' : 'italic', color: currentMeals.breakfast ? 'inherit' : '#999' }}>
          {currentMeals.breakfast || '点击添加早餐...'}
        </div>
      </PixelCard>

      {/* 午餐卡片 */}
      <PixelCard
        title="☀️ 午餐 (Lunch)"
        onClick={() => openEditModal('lunch', currentMeals.lunch)}
        style={{ backgroundColor: '#e8f5e9' }} // 浅绿背景
      >
        <div style={{ minHeight: '30px', fontStyle: currentMeals.lunch ? 'normal' : 'italic', color: currentMeals.lunch ? 'inherit' : '#999' }}>
          {currentMeals.lunch || '点击添加午餐...'}
        </div>
      </PixelCard>

      {/* 晚餐卡片 */}
      <PixelCard
        title="🌙 晚餐 (Dinner)"
        onClick={() => openEditModal('dinner', currentMeals.dinner)}
        style={{ backgroundColor: '#e3f2fd' }} // 浅蓝背景
      >
        <div style={{ minHeight: '30px', fontStyle: currentMeals.dinner ? 'normal' : 'italic', color: currentMeals.dinner ? 'inherit' : '#999' }}>
          {currentMeals.dinner || '点击添加晚餐...'}
        </div>
      </PixelCard>

      {/* 编辑弹窗 */}
      <MealEditModal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        onSave={handleSaveMeal}
        mealType={editingMeal.type}
        initialValue={editingMeal.value}
        dateStr={formatDateForDisplay(selectedDate)}
      />
    </div>
  );
};

export default Kitchen;